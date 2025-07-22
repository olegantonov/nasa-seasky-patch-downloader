import os
import time
import csv
import requests
from bs4 import BeautifulSoup

def get_patch_links(page_url):
    """Retorna a lista de URLs individuais de cada patch na galeria."""
    resp = requests.get(page_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = []
    for a in soup.select('.hds-gallery-item-link'):
        href = a.get('href')
        if href and href.startswith('https://www.nasa.gov/image-detail'):
            links.append(href)
    return links

def get_all_patch_links(base_url_pattern):
    """
    Itera pelas páginas numeradas, coletando todos os links de patch.
    Para quando uma página não retornar nenhum link.
    """
    all_links = []
    page = 1
    while True:
        url = base_url_pattern.format(page)
        print(f"Procurando patches em: {url}")
        links = get_patch_links(url)
        if not links:
            print("— não há mais patches; finalizando coleta.")
            break
        all_links.extend(links)
        page += 1
    return all_links

def parse_patch_page(patch_url):
    """Extrai download link, nome da missão e descrição de uma página de patch."""
    resp = requests.get(patch_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    img = soup.select_one('.hds-attachment-single__image img')
    download_link = img['src'] if img else ''
    title = soup.select_one('.hds-attachment-single__title')
    mission_name = title.get_text(strip=True) if title else ''
    desc = soup.select_one('.hds-attachment-single__caption')
    description = desc.get_text(strip=True) if desc else ''
    return download_link, mission_name, description

def main():
    base_pattern = 'https://www.nasa.gov/gallery/human-spaceflight-mission-patches/page/{}/'
    output_file = 'patches.csv'

    # Carrega links já processados (se o CSV existir)
    processed = set()
    if os.path.exists(output_file):
        with open(output_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                processed.add(row['patch_url'])
        mode = 'a'
        write_header = False
    else:
        mode = 'w'
        write_header = True

    # Obtem todos os links de patch
    patch_urls = get_all_patch_links(base_pattern)
    print(f"Total de patches encontrados: {len(patch_urls)}")

    # Abre CSV para gravação (append ou write)
    with open(output_file, mode, newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['patch_url', 'download_link', 'mission_name', 'description'])

        for url in patch_urls:
            if url in processed:
                print(f"🔹 Já processado, pulando: {url}")
                continue
            try:
                dl, name, desc = parse_patch_page(url)
                writer.writerow([url, dl, name, desc])
                print(f"✅ Gravado: {name}")
            except Exception as e:
                print(f"❌ Erro em {url}: {e}")
            time.sleep(1)  # breve pausa para gentileza ao servidor

if __name__ == '__main__':
    main()
