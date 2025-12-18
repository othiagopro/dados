def linha():
    print('-=' * 20)
def gorjeta(a, b):
    gor = (a * b) / 100
    tot = a + gor
    print(f'Valor da gorjeta: R${gor}')
    print(f'Total a pagar: R${tot}')

linha()
print('                  CAIXA \n')
linha()
valor = float(input('Digite o valor da conta: '))
porcentagem = float(input('Digite a porcentagem da gorjeta: '))
gorjeta(valor, porcentagem)
linha()