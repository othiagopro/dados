def verificarCPF(cpf):
    if not cpf.isdigit():
        print('Erro: O CPF deve conter apenas números!')
    elif len(cpf) != 11:
        print('Erro: O CPF deve conter exatamente 11 digitos')
    else:
        print('CPF valido!')

cpf = input('Digite seu CPF: ')
verificarCPF(cpf)
