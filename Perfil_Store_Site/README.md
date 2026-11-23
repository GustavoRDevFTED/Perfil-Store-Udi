# Loja Premium — base inicial

Base de uma loja virtual com Flask, HTML, CSS e JavaScript. A identidade visual é premium, elegante e minimalista. O nome e as fotografias dos produtos são provisórios e poderão ser substituídos depois.

## Executar localmente

1. Instale Python 3.10 ou superior.
2. Abra o terminal nesta pasta.
3. Crie e ative um ambiente virtual:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **Linux/macOS**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Inicie:
   ```bash
   python app.py
   ```
6. Acesse http://127.0.0.1:5000

## Estrutura

```text
loja_premium/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
        └── products/
```

## Próximas etapas

- Definir o nome e a identidade final da marca.
- Substituir os espaços reservados pelas fotos reais.
- Criar catálogo, filtros e página individual de produto.
- Implementar carrinho persistente, cadastro/login, estoque e checkout.
- Integrar banco de dados quando as regras da loja estiverem definidas.

Os valores exibidos nesta versão são apenas marcadores visuais, não preços reais.