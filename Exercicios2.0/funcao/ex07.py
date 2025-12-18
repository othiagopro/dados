def contarVogais(txt):
    qtd_vogais = 0
    vogais = 'Aaeiouãéíóúá'
    for letra in txt:
        if letra in vogais:
            qtd_vogais = qtd_vogais + 1
    print(f'A frase {txt} tem {qtd_vogais}!')

frase = input('Digite uma frase: ')
contarVogais(frase)
    
