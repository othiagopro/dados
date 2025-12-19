import pdfplumber

CAMINHO_PDF = r"C:\Users\thiago\Desktop\dp.pessoal\Extrato Mensal.pdf"

with pdfplumber.open(CAMINHO_PDF) as pdf:
    # Pega apenas a primeira página para teste
    page = pdf.pages[0] 
    
    # 1. Tente extração simples
    text = page.extract_text()
    print("--- TEXTO BRUTO (EXTRACT_TEXT) ---")
    print(text)
    print("-" * 30)

    # 2. Tente preservando o layout (bom para colunas)
    text_layout = page.extract_text(layout=True)
    print("--- TEXTO COM LAYOUT (LAYOUT=TRUE) ---")
    print(text_layout)