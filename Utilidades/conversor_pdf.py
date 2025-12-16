import pdfplumber
import pandas as pd
import re

# ==============================================================================
# CAMINHO DO ARQUIVO
# ==============================================================================
caminho_do_pdf = r"C:\Users\thiago\Desktop\Planilha Master\tipi.pdf"
# ==============================================================================

def limpar_texto(texto):
    if not texto: return ""
    return re.sub(r'\s+', ' ', texto).strip()

def processar_tipi_v5(caminho):
    print("Iniciando leitura V5 (Com suporte a NCMs curtos como 9615.1)...")
    
    dados_finais = []
    
    ncm_atual = None
    descricao_linhas = []
    aliquota_atual = None
    lendo_descricao = False 

    # -------------------------------------------------------------------------
    # 1. ATUALIZAÇÃO DA REGEX (A parte importante)
    # -------------------------------------------------------------------------
    # Explicação:
    # \d{2}\.?\d{2}       -> Pega os 4 primeiros dígitos (ex: 9615)
    # (?:\.\d{1,3})* -> Pega grupos de ponto + 1 a 3 dígitos (ex: .1, .10, .00, .5)
    #                      Isso permite 9615.1, 9615.10, 9615.10.00, etc.
    # |Ex\s*\d+           -> Ou pega exceções (Ex 01)
    # -------------------------------------------------------------------------
    regex_ncm = re.compile(r'^\s*(\d{2}\.?\d{2}(?:\.\d{1,3})*|Ex\s*\d+)\s+')

    # 2. IDENTIFICA ALÍQUOTA (Final da linha)
    regex_aliq = re.compile(r'\s+(NT|[\d,]+)\s*$')

    # 3. LISTA DE BLOQUEIO (Títulos e sujeira que não devem ir para a descrição)
    termos_bloqueio = [
        "SEÇÃO", "Seção", "CAPÍTULO", "Capítulo", 
        "OBJETOS DE ARTE", "MERCADORIAS E PRODUTOS", 
        "Notas", "Nota.", "Nota Complementar", 
        "Ressalvadas", "Consideram-se", "O presente Capítulo",
        "_____", "O IPI incide", "Ficam reduzidas", "Na acepção"
    ]

    with pdfplumber.open(caminho) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            print(f"Lendo página {i+1}/{total}...", end='\r')
            
            text = page.extract_text()
            if not text: continue
            
            linhas = text.split('\n')
            
            for linha in linhas:
                linha_limpa = linha.strip()
                
                # --- NOVO NCM ---
                match_ncm = regex_ncm.match(linha)

                if match_ncm:
                    # Salva o anterior
                    if ncm_atual:
                        dados_finais.append([ncm_atual, limpar_texto(" ".join(descricao_linhas)), aliquota_atual])

                    # Inicia o novo
                    ncm_atual = match_ncm.group(1).strip()
                    descricao_linhas = []
                    aliquota_atual = None
                    lendo_descricao = True

                    # Processa o resto da linha
                    resto = linha[match_ncm.end():]
                    
                    # Tenta pegar alíquota na mesma linha
                    match_aliq_linha = regex_aliq.search(resto)
                    if match_aliq_linha:
                        aliquota_atual = match_aliq_linha.group(1)
                        resto = resto[:match_aliq_linha.start()]
                    
                    # Verifica bloqueio na mesma linha
                    for termo in termos_bloqueio:
                        if termo in resto:
                            resto = resto.split(termo)[0]
                            lendo_descricao = False
                            break

                    if resto.strip():
                        descricao_linhas.append(resto)

                else:
                    # --- CONTINUAÇÃO ---
                    if not lendo_descricao:
                        continue

                    if ncm_atual:
                        # Verifica se a linha inteira é um bloqueio (Títulos de Seção, etc)
                        bloquear_agora = False
                        for termo in termos_bloqueio:
                            if termo in linha_limpa:
                                bloquear_agora = True
                                break
                        
                        if bloquear_agora:
                            lendo_descricao = False
                            continue

                        # Tenta achar alíquota final
                        match_aliq_final = regex_aliq.search(linha)
                        if match_aliq_final:
                            aliquota_atual = match_aliq_final.group(1)
                            texto = linha[:match_aliq_final.start()]
                            if texto.strip():
                                descricao_linhas.append(texto)
                        else:
                            descricao_linhas.append(linha)

        # Salva o último
        if ncm_atual:
            dados_finais.append([ncm_atual, limpar_texto(" ".join(descricao_linhas)), aliquota_atual])

    print("\nSalvando Excel...")
    df = pd.DataFrame(dados_finais, columns=['NCM', 'Descrição', 'Alíquota (%)'])
    df = df[df['NCM'].notna()]
    
    # Limpeza final de alíquotas presas na descrição
    def limpar_nt(x):
        if isinstance(x, str) and x.endswith('NT'):
            return x.replace('NT', '').strip()
        return x
        
    df['Descrição'] = df['Descrição'].apply(limpar_nt)
    
    df.to_excel("tabela_tipi_v5_completa.xlsx", index=False)
    print("Concluído!")

if __name__ == "__main__":
    processar_tipi_v5(caminho_do_pdf)