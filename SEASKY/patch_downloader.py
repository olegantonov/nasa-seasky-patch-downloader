import os
import time
import csv
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

MENU_URL = 'http://www.seasky.org/space-exploration/mission-patches-menu.html'
OUTPUT_FILE = 'seasky_patches.csv'
BACKUP_FILE = 'seasky_patches_backup.csv'

def get_category_links(menu_url):
    """Retorna todas as URLs das categorias (Project Mercury, Gemini, etc.)."""
    resp = requests.get(menu_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = []
    for a in soup.select('div.menu-text-patch a.links-lg'):
        href = a.get('href')
        if href:
            links.append(urljoin(menu_url, href))
    return links

def parse_category_page(cat_url):
    """
    Para cada categoria, extrai:
     - program_desc: descrição do programa (intro-patch)
     - Para cada imagem/texto de patch:
         * patch_url: URL completa da imagem
         * mission_name: texto do <h3>
         * description: program_desc
         * launch_date: texto após 'Launch:' se existir
    Retorna uma lista de dicts.
    """
    resp = requests.get(cat_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    # descrição geral do programa
    desc_tag = soup.select_one('#intro-patch p')
    program_desc = desc_tag.get_text(strip=True) if desc_tag else ''

    patches = []
    image_rows = soup.find_all('div', class_='image-row')
    text_rows  = soup.find_all('div', class_='text-row')

    for img_row, txt_row in zip(image_rows, text_rows):
        imgs  = img_row.find_all('img')
        texts = txt_row.find_all('div', class_='cellbox')

        for img, txt in zip(imgs, texts):
            src = img.get('src', '')
            patch_url = urljoin(cat_url, src)

            # extrai mission_name do <h3>, juntando linhas
            h3 = txt.find('h3')
            mission_name = ' '.join(h3.stripped_strings) if h3 else ''

            # extrai a data de lançamento
            launch_match = re.search(r'Launch:\s*(.+)', txt.get_text(separator=' ', strip=True))
            launch_date = launch_match.group(1).strip() if launch_match else ''

            patches.append({
                'patch_url':     patch_url,
                'mission_name':  mission_name,
                'description':   program_desc,
                'launch_date':   launch_date
            })
    return patches

def load_processed(output_file):
    """Retorna um set de patch_url já gravados (e faz backup se formato antigo)."""
    if not os.path.exists(output_file):
        return set(), 'w', True

    # lê cabeçalho
    with open(output_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        old_header = next(reader, [])

    # se não tem coluna patch_url, faz backup e recomeça
    if 'patch_url' not in old_header:
        os.replace(output_file, BACKUP_FILE)
        print(f"⚠️ Formato antigo detectado — renomeado para {BACKUP_FILE}")
        return set(), 'w', True

    # caso normal, carrega URLs já processadas
    processed = set()
    with open(output_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            processed.add(row['patch_url'])
    return processed, 'a', False

def main():
    # 1) Carrega histórico
    processed, mode, write_header = load_processed(OUTPUT_FILE)

    # 2) Pega todas as categorias
    categories = get_category_links(MENU_URL)
    print(f"🗂️  Encontradas {len(categories)} categorias.")

    # 3) Abre CSV para gravação
    with open(OUTPUT_FILE, mode, newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['patch_url', 'mission_name', 'description', 'launch_date'])

        # 4) Para cada categoria e cada patch
        for cat_url in categories:
            print(f"🔍 Processando categoria: {cat_url}")
            try:
                patches = parse_category_page(cat_url)
            except Exception as e:
                print(f"❌ Falha ao abrir {cat_url}: {e}")
                continue

            for p in patches:
                if p['patch_url'] in processed:
                    print(f"⏭️  Já processado: {p['mission_name']}")
                    continue
                writer.writerow([
                    p['patch_url'],
                    p['mission_name'],
                    p['description'],
                    p['launch_date']
                ])
                processed.add(p['patch_url'])
                print(f"✅ Gravado: {p['mission_name']}")
                time.sleep(0.5)  # pausa leve

if __name__ == '__main__':
    main()
