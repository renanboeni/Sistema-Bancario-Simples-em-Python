import textwrap

MENSAGENS = {
    "saldo_insuficiente": "\nOperação não concluída! Saldo insuficiente.",
    "limite_excedido": "\nOperação não concluída! O valor excede o seu limite.",
    "saques_excedidos": "\nOperação não concluída! Quantidade de saques diários excedido.",
    "valor_invalido": "\nOperação não concluída! Valor informado é inválido.",
    "saque_sucesso": "\nSeu saque foi realizado com sucesso!",
    "nao_movimentacoes": "Não foram realizadas movimentações.",
    "sair": "\nObrigado por usar nosso sistema bancário!\n"
}

def menu():
    menu = """
    \033[34m=-=-= Selecione uma opção do menu: =-=-=\033[0m
    [1]\tSacar
    [2]\tDepositar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta 
    [6]\tListar contas
    [7]\tSair
    => """
    return input(textwrap.dedent(menu)).strip() #retorna a opção que o usuario escolheu

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print("=== Operação concluída! Depósito realizado com sucesso. ===")

    else:
        print(MENSAGENS["valor_invalido"]) 
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    exceder_saldo = valor > saldo
    exceder_limite = valor > limite
    exceder_saques = numero_saques >= limite_saques

    if exceder_saldo:
        print(MENSAGENS["saldo_insuficiente"])
    elif exceder_limite:
        print(MENSAGENS["limite_excedido"])
    elif exceder_saques:
        print(MENSAGENS["saques_excedidos"])
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Operação concluída! Saque realizado com sucesso. ===")
    
    else:
        print(MENSAGENS["valor_invalido"]) 

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n\033[33m-=-=-=-=-=-=-\033[0m \033[36mEXTRATO\033[0m \033[33m-=-=-=-=-=-=-\033[0m")
    print(MENSAGENS["nao_movimentacoes"] if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[0m")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return
    
    nome = str(input("Informe seu nome completo: "))
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, criação de conta encerrada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("-=-" * 35)
        print(textwrap.dedent(linha)) 

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1": #saque
            valor = round(float(input("Informe o valor de saque: \nR$ ")), 2)

            saldo, extrato = sacar(
              saldo=saldo,
              valor=valor,
              extrato=extrato,
              limite=limite,
              numero_saques=numero_saques,
              limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "2": #deposito
            valor = round(float(input("Informe o valor do depósito: \nR$ ")), 2)

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "3": #extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4": #criar usuario
            criar_usuario(usuarios)

        elif opcao == "5": #criar conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6": #listar usuario
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação não concluída, por favor selecione novamente a operação desejada.")
            
main()