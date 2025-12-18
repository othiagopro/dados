def contarPalavras(txt):
    temp = txt.split()
    princ = []
    for palavra in temp:
        if len(palavra) > 10:
            princ.append(palavra)
        else:
            print('Nenhuma palavra longa foi encontrada no texto')
    palavras_longas = " ".join(princ)
    print(f'Palavras longas encontradas: {palavras_longas}')
    
    
frase = input('Digite um texto: ')
contarPalavras(frase)
