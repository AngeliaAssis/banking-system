#Otimizando o sistema bancario com funções
def menu():
    menu = """\n
    Menu
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuario
    [q] Sair
    => """
    return input(menu)

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso")
    else:
        print("Operação falhou. O valor informado é inválido")

    return saldo, extrato

def sacar(valor, saldo, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou. O valor de saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou. Número máximo de saque excedido")

        else:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print("\nSaque realizado com sucesso")

    else:
        print("Operação falhou. O valor informado é inválido")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print('\nExtrato')
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuario com esse CPF")
        return
    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("Usuario criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado")

def main():
    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            print("Depósito")
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == 's':
            print('Saque')
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, limite, numero_saques, limite_saques)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida. Por favor, selecione novamente a operação desejada')


main()
