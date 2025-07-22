\# Patch Downloaders – NASA e SeaSky



Este repositório contém dois scripts em Python para download automatizado de patches de missões espaciais.  

É destinado exclusivamente a fins \*\*educacionais\*\* e de \*\*demonstração de técnicas de web scraping com `requests` e `BeautifulSoup`\*\*.



---



\## 📂 Estrutura



DOWNLOAD PATCHS/

│

├── NASA/ # Imagens e script da NASA

│ └── patch\_downloader.py

│

├── SEASKY/ # Imagens e script do site Sea and Sky

│ └── seasky\_downloader.py

│

├── venv/ # Ambiente virtual (não subir no GitHub)

│

├── requirements.txt # Bibliotecas necessárias

└── README.md # (este arquivo)



---



\## 🧪 Instalação



Recomendado usar um ambiente virtual:



```bash

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt





▶️ Uso

NASA

Para baixar os patches da NASA:



bash

Copiar

Editar

cd NASA

python patch\_downloader.py

Sea and Sky

Para baixar os patches do site Sea and Sky:



bash

Copiar

Editar

cd SEASKY

python seasky\_downloader.py

⚠️ Aviso Legal

NASA

O conteúdo do site da NASA está, em geral, em domínio público. Mais detalhes:

🔗 https://www.nasa.gov/multimedia/guidelines/



Sea and Sky

All content on this site is Copyright © 1998 - 2016 by Sea and Sky.

Content from this Website may not be used in any form without written permission.



🛑 Este script não deve ser utilizado para redistribuição pública das imagens obtidas do site Sea and Sky sem autorização expressa. Este projeto é apenas uma ferramenta técnica para fins educacionais.



📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE.





---



\### ✅ 2. `LICENSE` (MIT)



```text

MIT License



Copyright (c) 2025 João Eduardo



Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the “Software”), to deal

in the Software without restriction...



\[texto completo da licença MIT — posso gerar ele 100% se quiser, é só pedir]



✅ 3. .gitignore (para não subir venv nem imagens)

gitignore

Copiar

Editar

\# Ignorar ambiente virtual

venv/



\# Ignorar imagens

NASA/\*.jpg

NASA/\*.png

SEASKY/\*.jpg

SEASKY/\*.png



\# Cache do Python

\_\_pycache\_\_/

\*.pyc

