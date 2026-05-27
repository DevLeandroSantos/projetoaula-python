def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))
    if idade < 18:
        print("Entrada não permitida! Menores não podem entrar.")
    else:
        print(f"{nome} cadastrado com sucesso!")

def calcular_consumo():
    consumos = []
    qtd = int(input("Quantos itens foram consumidos? "))
    for i in range(qtd):
        valor = float(input(f"Digite o valor do item {i+1}: R$ "))
        consumos.append(valor)
    total = sum(consumos)
    print(f"Total da conta: R$ {total:.2f}")

def validar_vip():
    codigo = input("Digite o código VIP: ")
    if codigo == "VIP123":
        print("Acesso liberado à área VIP!")
    else:
        print("Código inválido.")

def menu():
    while True:
        print("\n--- MENU BOATE ---")
        print("1 - Cadastrar cliente")
        print("2 - Calcular consumo")
        print("3 - Validar VIP")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            calcular_consumo()
        elif opcao == "3":
            validar_vip()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

menu()
