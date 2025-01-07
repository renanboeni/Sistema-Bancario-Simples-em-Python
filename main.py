menu = """
\033[34mSelecione uma opção do menu:\033[0m
[1] 💸 Sacar
[2] 💰 Depositar
[3] 📄 Extrato
[4] 🚪 Sair\n
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

MENSAGENS = {
    "saldo_insuficiente": "\nOperação não concluída! Saldo insuficiente.",
    "limite_excedido": "\nOperação não concluída! O valor excede o seu limite.",
    "saques_excedidos": "\nOperação não concluída! Quantidade de saques diários excedido.",
    "valor_invalido": "\nOperação não concluída! Valor informado é inválido.",
    "saque_sucesso": "\nSeu saque foi realizado com sucesso!",
    "nao_movimentacoes": "Não foram realizadas movimentações.",
    "sair": "\nObrigado por usar nosso sistema bancário!\n"
}

while True:

    opcao = input(menu).strip()

    if opcao == "1": #SAQUE          
        valor = round(float(input("Informe o valor de saque: \nR$ ")), 2)

        exceder_saldo = valor > saldo
        exceder_limite = valor > limite
        exceder_saques = numero_saques >= LIMITE_SAQUES

        if exceder_saldo:
            print(MENSAGENS["saldo_insuficiente"])
        elif exceder_limite:
            print(MENSAGENS["limite_excedido"])
        elif exceder_saques:
            print(MENSAGENS["saques_excedidos"])

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(MENSAGENS["saque_sucesso"])
        
        else:
            print("Operação não concluída! Valor informado é inválido.")

    elif opcao == "2": #DEPOSITO
        valor = round(float(input("Informe o valor do depósito: \nR$ ")), 2)
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não concluída! O valor informado é inválido.")    
    
    elif opcao == "3": #EXTRATO
        print("\n\033[33m-=-=-=-=-=-=-\033[0m \033[36mEXTRATO\033[0m \033[33m-=-=-=-=-=-=-\033[0m")
        print(MENSAGENS["nao_movimentacoes"] if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[0m")
    
    elif opcao == "4": #SAIR
        print(MENSAGENS["sair"])
        break

    else:
        print("Operação não concluída, por favor selecione novamente a operação desejada.")