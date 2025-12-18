print("--------------- Loja Meteoro ----------------\n")
print("Formas de pagamento:")
print("[1] A vista dinheiro/cheque: 10% de desconto\n[2] A vista no cartão: 5% de desconto\n[3] 2x no cartão: preço normal\n[4] 3x ou mais no cartão: 20% de juros\n")

valor = int(input("Digite o valor a ser pago: "))
forma = int(input("Digite a forma de pagamento: "))

if forma == 1:
    desconto = valor * 0.1
    total = valor - desconto
    print(f"O valor da sua compra ficou R${total}.")
elif forma == 2:
    desconto = valor * 0.05
    total = valor - desconto
    print(f"O valor da sua compra ficou R${total}.")
elif forma == 3:
    total = valor / 2
    print(f"O valor da sua compra ficou 2 x de R${total}.")
elif forma == 4:
    juros = valor * 0.2
    total = (valor + juros) / 3
    print(f"O valor da sua compra ficou 3 x de R${total}.")

