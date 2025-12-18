import pandas as pd
from fuzzywuzzy import process

# Substitua 'planilha_a.xlsx' e 'planilha_b.xlsx' pelos nomes dos seus arquivos
df_a = pd.read_excel('planilha_a.xlsx')
df_b = pd.read_excel('planilha_b.xlsx')

# Crie uma lista para armazenar os resultados
resultados = []

# Crie uma lista com todos os nomes de produtos da Planilha A
nomes_a = df_a['Nome_Produto'].tolist()

# Itere sobre cada linha (produto) da Planilha B
for index, row in df_b.iterrows():
    nome_produto_b = row['Nome_Produto']

    # Use o fuzzywuzzy para encontrar a melhor correspondência
    # 'limit=1' retorna apenas o melhor resultado
    # 'score_cutoff=85' define um limite mínimo de similaridade para considerar como correspondência
    melhor_correspondencia = process.extractOne(nome_produto_b, nomes_a, score_cutoff=85)

    if melhor_correspondencia:
        nome_encontrado_a, similaridade = melhor_correspondencia
        # Pegue o código do produto na Planilha A
        codigo_produto_a = df_a.loc[df_a['Nome_Produto'] == nome_encontrado_a, 'Codigo_Produto'].iloc[0]

        # Adicione o resultado à sua lista
        resultados.append({
            'Nome_Produto_B': nome_produto_b,
            'Nome_Produto_A_Correspondente': nome_encontrado_a,
            'Codigo_Produto_A': codigo_produto_a,
            'Similaridade': similaridade
        })

# Crie um novo DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Exiba o DataFrame de resultados
print(df_resultados)

# Se quiser salvar os resultados em um novo arquivo Excel
df_resultados.to_excel('resultados_correspondencia.xlsx', index=False)
