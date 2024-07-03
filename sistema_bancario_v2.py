import os, time
extrato_bancario = []
saques = []
depositar = False
saque = False
saldo = 0
agencia = "0001"
usuarios = []
contas= []
def menu():
    os.system('cls')
    while True:
        menu = input( """
                    Bem vindo ao sistema bancario!
                    Selecione uma opcao abaixo:
                          [1] Depositar
                          [2] Sacar
                          [3] Extrato
                          [4] Cadastrar usuario
                          [5] Nova conta
                          [6] Listar usuarios
                          [7] Listar contas
                          [8] Sair


=> """)

        if menu == "1":
            depositar(extrato_bancario)
        elif menu == "2":
            sacar()
        elif menu == "3":
            extrato(extrato_bancario)
        elif menu == "4":
            cadastrar_usuario()
        elif menu == "5":
            criar_conta()
        elif menu == "6":
            listar_usuarios()
        elif menu == "7":
            listar_contas()
        elif menu == "8":
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
    
def cadastrar_usuario():
    while True:
        cpf_usuario = input("Por favor informe seu CPF: ")
        if not cpf_usuario:
            print("Campo nao pode estar vazio")
        else:
            usuario = filtrar(cpf_usuario)
            if usuario:
                print("Erro! Usuario ja cadastrado!!!!")
                return
            break
    while True:
        nome = input("Por favor informe seu nome: ")
        if not nome:
            print("Campo nao pode estar vazio")
        else:
            break
    while True:
        dt_nasc = input("Agora informe sua data de nascimento (dd/mm/aaaa): ")
        if not dt_nasc:
            print("Campo nao pode estar vazio")
        else:
            break
    while True:
        endereco = input("Informe seu endereco (cidade - bairro): ")
        if not endereco:
            print("Campo nao pode estar vazio")
        else:
            break
    usuarios.append({"nome": nome, "data de nascimento": dt_nasc, "CPF": cpf_usuario, "endereco": endereco})
    os.system('cls')
    print("Usuario cadastrado com sucesso!!!")

def filtrar(cpf_usuario): 
    usuario_filtrado = [usuario for usuario in usuarios if usuario["CPF"] == cpf_usuario]      
    return usuario_filtrado[0] if usuario_filtrado else None

def listar_usuarios():
    if usuarios:
        for i in range(len(usuarios)):
            print(usuarios[i])
    else:
        print("Nenhum usuario encontrado!")

def criar_conta():
    cpf_usuario = input("Por favor informe seu CPF: ")
    usuario = filtrar(cpf_usuario)
    if usuario:
        print("Conta criada com sucesso!!")
        num_conta = len(contas)+1
        contas.append({"Agencia": agencia, "numero_conta": num_conta, "usuario": usuario})
    print("Usuario nao encontrado")

def listar_contas():
    if contas:
        for i in range(len(contas)):
            print(contas[i])
    else:
        print("Nenhuma conta encontrada!")
menu()