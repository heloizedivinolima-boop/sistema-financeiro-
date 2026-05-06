entradas = []
saidas = []

def adicionar_entrada():
    valor = float(input("Digite o valor da entrada: R$ "))
    descricao = input("Descrição: ")
    entradas.append({"valor": valor, "descricao": descricao})
    print("Entrada adicionada!\n")

def adicionar_saida():
    valor = float(input("Digite o valor da saída: R$ "))
    descricao = input("Descrição: ")
    saidas.append({"valor": valor, "descricao": descricao})
    print("Saída adicionada!\n")

def ver_saldo():
    total_entradas = sum(e["valor"] for e in entradas)
    total_saidas = sum(s["valor"] for s in saidas)
    saldo = total_entradas - total_saidas

    print(f"\nTotal de entradas: R$ {total_entradas:.2f}")
    print(f"Total de saídas: R$ {total_saidas:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}\n")

def listar_movimentacoes():
    print("\n--- ENTRADAS ---")
    for e in entradas:
        print(f"R$ {e['valor']:.2f} - {e['descricao']}")

    print("\n--- SAÍDAS ---")
    for s in saidas:
        print(f"R$ {s['valor']:.2f} - {s['descricao']}")
    print()

def menu():
    while True:
        print("=== SISTEMA FINANCEIRO ===")
        print("1 - Adicionar entrada")
        print("2 - Adicionar saída")
        print("3 - Ver saldo")
        print("4 - Listar movimentações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_entrada()
        elif opcao == "2":
            adicionar_saida()
        elif opcao == "3":
            ver_saldo()
        elif opcao == "4":
            listar_movimentacoes()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

# Executar sistema
menu()