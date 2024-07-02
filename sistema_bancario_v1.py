import os, time
extrato_bancario = []
saques = []
depositar = False
saque = False
saldo = 0
def menu():
    os.system('cls')
    while True:
        menu = input( """
                    Bem vindo ao sistema bancario!
                    Selecione uma opcao abaixo:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """)

        if menu == "1":
            depositar(extrato_bancario)
        elif menu == "2":
            sacar()
        elif menu == "3":
            extrato(extrato_bancario)
        elif menu == "4":
            break
        else:
            print("Opção invalida, tente novamente")
        
def depositar(extrato_bancario):
    global saldo, depositar
    i=0
    while True:
        os.system('cls')
        deposito = float(input("Digite o valor a ser depositado(o valor nao pode ser negativo): R$"))
        if deposito > 0 :
            saldo += deposito
            depositar = True
            print(f"Deposito de R${deposito:.2f} realizado com sucesso! Seu saldo atual é de: R${saldo:.2f}")
            i+=1
            extrato_bancario.append(deposito)
            while True:
                os.system('cls')
                sair = str(input("Deseja realizar um novo deposito ou sair? (s/n): ").strip().lower())
                if sair == "s":
                    break
                elif sair == "n":
                    menu()
                else:
                    print("Opção invalida, tente novamente!!")
                    time.sleep(2)
        else:
            print("Valor invalido, tente novamente!!")
            time.sleep(2)

def extrato(extrato_bancario):
    os.system('cls')
    global depositar, saque
    j=0
    k=0
    if depositar == True:
        print("Extrato do Banco:\nDepositos:")
        for i in range(len(extrato_bancario)):
            print(f"Valor do deposito {i+1}: R${extrato_bancario[j]}")
            j+=1
        if saque == True:
            print("\nSaques:")
            for i in range(len(saques)):
                print(f"Valor do saque {i+1}: R${saques[k]}")
                k+=1
            print("Saldo final = R$",saldo)
        else:
            print(f"Saldo final = R${saldo:.2f}")
            print("Retornando ao menu principal...")
            time.sleep(3)
            menu()
    else:
        print("Nao foram realizadas movimentacoes!!")

def sacar():
    LIMITE_SAQUE = 3
    global saldo, saque
    i = 0
    os.system('cls')
    if depositar == True:
        while True:
            print("Bem vindo a operacao de saque!!")
            valor_saque = float(input("Digite o valor a ser sacado(valor menor que R$500): R$"))
            if valor_saque > 0 and valor_saque < saldo:
                if valor_saque <= 500:
                    saldo -= valor_saque
                    saque = True
                    saques.append(valor_saque)
                    i+=1
                    print(f"Saque de R${valor_saque:.2f} realizado com sucesso!\nSeu saldo atual e de: R${saldo}")
                    if i == LIMITE_SAQUE:
                        print("Você alcançou o limite de saques diarios. Tente novamente amanha!\nRetornando ao menu principal...")
                        time.sleep(3)
                        break
                else:
                    print("Saldo abaixo do valor do saque, tente novamente")
                    time.sleep(2)
            else:
                print("Valor invalido, tente novamente!!")
                time.sleep(2)
            sair = input(f"Deseja realizar mais algum saque? Restam apenas {3-i} saques: (s/n)")
            if sair == "s":
                continue
            elif sair == "n":
                break
            else:
                print("insira uma opcao valida!!")
    else:
        while True:
            print("Nenhum deposito realizado, conta vazia!!")
            time.sleep(4)
            break
    
        

menu()