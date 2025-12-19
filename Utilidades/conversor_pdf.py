import pdfplumber
import pandas as pd
import re
import os

CAMINHO_PDF = r"C:\Users\thiago\Desktop\dp.pessoal\Extrato Mensal.pdf"

# ==============================================================================
# NOVOS PADRÕES (SIMPLIFICADOS)
# ==============================================================================

# Regex apenas para limpar o prefixo do ID (remove "Empr.:", "Contr:", pontos e espaços)
REGEX_LIMPA_PREFIXO = re.compile(r'^(?:Empr|Contr|Empresa)[:\.\s]*', re.IGNORECASE)

# Regex de Rubrica (Mantido pois é robusto)
# Aceita: "1HORAS", "1 HORAS", valores colados "2.500,00P"
REGEX_RUBRICA = re.compile(r'\b(\d{1,4})\s*([A-ZÀ-Ú0-9\.\%\/\-\(\)\s]+?)\s+(\d+(?:[.,]\d+)?)\s+(\d{1,3}(?:\.\d{3})*,\d{2})\s*([PD])')

# Regex de Competência
REGEX_COMPETENCIA = re.compile(r'Competência:\s*(\d{2}/\d{4})')

def limpar_valor(valor_str):
    if not valor_str: return 0.0
    limpo = valor_str.replace('.', '').replace(',', '.')
    try: return float(limpo)
    except: return 0.0

def processar_folha_blindada(caminho):
    dados = []
    print(f"Lendo arquivo: {caminho}")

    if not os.path.exists(caminho):
        print("ERRO: Arquivo não encontrado!")
        return

    with pdfplumber.open(caminho) as pdf:
        competencia_atual = "Indefinida"

        for i, page in enumerate(pdf.pages):
            # Tenta extração crua primeiro (às vezes layout=True separa demais as letras do nome)
            texto = page.extract_text() 
            if not texto: continue

            # Atualiza competência
            match_comp = REGEX_COMPETENCIA.search(texto)
            if match_comp:
                competencia_atual = match_comp.group(1)

            linhas = texto.split('\n')
            
            id_func = None
            nome_func = None

            for linha in linhas:
                linha = linha.strip()
                if not linha: continue

                # --- 1. Lógica "Blindada" de Funcionário ---
                # Verifica se a linha tem "Situação" (que é padrão nesse layout)
                # E se tem "CPF" (para garantir que é cabeçalho de func)
                if "Situação" in linha and "CPF" in linha:
                    try:
                        # Pega tudo que vem ANTES de "Situação"
                        parte_esquerda = linha.split("Situação")[0].strip()
                        
                        # Remove o prefixo "Empr.:" ou "Contr:"
                        parte_limpa = REGEX_LIMPA_PREFIXO.sub("", parte_esquerda).strip()
                        
                        # Agora parte_limpa deve ser algo como "96ALZIRA..." ou "1 CAMILA..."
                        # Vamos separar o primeiro número (ID) do resto (Nome)
                        match_id_nome = re.search(r'^(\d+)\s*(.*)', parte_limpa)
                        
                        if match_id_nome:
                            id_func = match_id_nome.group(1)
                            nome_func = match_id_nome.group(2).strip()
                            print(f"Funcinário encontrado: ID {id_func} - {nome_func}")
                        else:
                            # Caso de falha estranha, reseta para não misturar
                            print(f"Aviso: Linha de funcionário detectada mas não processada: {parte_esquerda}")
                            id_func = None 
                    except Exception as e:
                        print(f"Erro ao processar linha de func: {e}")
                    continue

                # --- 2. Rubricas ---
                if id_func:
                    matches = REGEX_RUBRICA.finditer(linha)
                    for match in matches:
                        desc = match.group(2).strip()
                        if len(desc) < 2: continue # Ignora lixo
                        
                        # Ignora anos soltos que o regex possa pegar
                        if match.group(1) in ["2024", "2025"]: continue

                        dado = {
                            "Competencia": competencia_atual,
                            "ID": int(id_func), # Converte para int para ordenar melhor no Excel
                            "Nome": nome_func,
                            "Rubrica_Cod": int(match.group(1)),
                            "Descricao": desc,
                            "Referencia": match.group(3),
                            "Valor": limpar_valor(match.group(4)),
                            "Tipo": "Provento" if match.group(5) == 'P' else "Desconto"
                        }
                        dados.append(dado)

    # --- Exportação ---
    if dados:
        df = pd.DataFrame(dados)
        
        # Ordenação: Competência -> Nome -> Tipo (Provento primeiro) -> Código
        df = df.sort_values(by=['Competencia', 'Nome', 'Tipo', 'Rubrica_Cod'], ascending=[True, True, False, True])
        
        print(f"\nSucesso total! {len(df)} registros extraídos.")
        print(df.tail())
        
        df.to_csv("folha_final_corrigida.csv", index=False, sep=';', encoding='utf-8-sig')
        print("Salvo em: folha_final_corrigida.csv")
    else:
        print("\nNenhum dado extraído.")
        print("DICA: Se ainda falhar, mande o print do comando abaixo:")
        print("print(pdf.pages[0].extract_text())")

if __name__ == "__main__":
    processar_folha_blindada(CAMINHO_PDF)