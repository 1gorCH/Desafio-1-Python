menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.1")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaçao falhou! Não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operaçao falhou! O valor do saco excede o limite")
        elif excedeu_saques:
            print("Operaçao falhou! Número máximo de saques atingidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operaçao falhou! O valor informado é invalido.")
    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")
    elif opcao == "q":
        break

    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA!")