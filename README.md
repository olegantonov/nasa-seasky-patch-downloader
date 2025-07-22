# 🛰️ NASA & SeaSky Patch Downloader

Este repositório contém dois scripts Python automatizados para download de **emblemas de missões espaciais** dos sites oficiais da NASA e SeaSky.  
Os scripts percorrem as galerias de imagens, salvam os patches localmente e registram os links em arquivos `.csv` para evitar duplicações.

---

## 📁 Estrutura de Diretórios

```
D:\Usuários\dgms\Desktop\DOWNLOAD PATCHS
├── NASA
│   ├── patch_downloader.py
│   └── patches.csv
├── SEASKY
│   ├── patch_downloader.py
│   └── seasky_patches.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📦 Requisitos

- Python 3.8 ou superior
- Internet ativa
- Git (opcional, para versionamento)
- Ambiente virtual (venv)

---

## 🧪 Criar e ativar ambiente virtual

Abra o PowerShell no diretório `DOWNLOAD PATCHS` e execute:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Você verá o prefixo `(venv)` no terminal, indicando que o ambiente está ativo.

---

## 📥 Instalar dependências

Com o ambiente virtual ativado, rode:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executar o script da NASA

Este script percorre todas as páginas da galeria oficial de patches da NASA, baixa as imagens e salva o controle em `patches.csv`.

```bash
cd NASA
python patch_downloader.py
```

**Fonte de dados:**  
[https://www.nasa.gov/gallery/human-spaceflight-mission-patches](https://www.nasa.gov/gallery/human-spaceflight-mission-patches)

---

## ▶️ Executar o script do SeaSky

Este script coleta os patches de missões Apollo, Gemini, Mercury e Skylab do site SeaSky.org.

```bash
cd ..\SEASKY
python patch_downloader.py
```

**Fonte de dados:**  
[https://www.seasky.org/space-exploration/space-patch-gallery.html](https://www.seasky.org/space-exploration/space-patch-gallery.html)

---

## 🧠 Funcionamento

- As imagens são baixadas apenas se ainda não estiverem listadas no respectivo `.csv`.
- Cada script pode ser executado novamente sem gerar duplicatas.
- As imagens são salvas nas pastas `NASA/patches/` e `SEASKY/patches/`.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Contribuições

Sinta-se à vontade para abrir *issues* ou *pull requests* com melhorias, ajustes ou novos sites de patches!

---

## 🌌 Autor

Desenvolvido por **Daniel Marques** 
