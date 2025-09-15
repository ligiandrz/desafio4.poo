def adicionar_pessoa(filas):
    nome = input("Insira nome: ").strip()

    while True:
        try:
            idade = int(input("Idade: ").strip())
            if idade < 0:
                print("Idade inválida,digite um número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida,digite apenas números para a idade.")

    genero = input("Gênero: ").strip().lower()

    gestante = "não"
    if genero == "mulher" and idade >= 17:
        gestante = input("É gestante? (sim/não): ").strip().lower()
    pcd = input("É PCD? (sim/não): ").strip().lower()
    pessoa = {"nome": nome, "idade": idade, "gestante": gestante, "pcd": pcd}

    if idade >= 60 or gestante == "sim" or pcd == "sim":
        filas["prioritarios"].append(pessoa)
        print(f"{nome} foi adicionado na fila PRIORITÁRIA.")
    else:
        filas["normais"].append(pessoa)
        print(f"{nome} foi adicionado na fila NORMAL.")


def listar_filas(filas):
    print("\n FILA DE ATENDIMENTO:")
    if not filas["prioritarios"] and not filas["normais"]:
        print("Nenhuma pessoa na fila.")
    else:
        if filas["prioritarios"]:
            print("\nPrioritários:")
            for i, pessoa in enumerate(filas["prioritarios"], 1):
                print(f"{i}. {pessoa['nome']} ({pessoa['idade']} anos)")
        if filas["normais"]:
            print("\nNormais:")
            for i, pessoa in enumerate(filas["normais"], 1):
                print(f"{i}. {pessoa['nome']} ({pessoa['idade']} anos)")
    print()


def atender_proximo(filas):
    if filas["prioritarios"]:
        pessoa = filas["prioritarios"].pop(0)
        print(f" Atendendo prioritário: {pessoa['nome']}")
    elif filas["normais"]:
        pessoa = filas["normais"].pop(0)
        print(f" Atendendo normal: {pessoa['nome']}")
    else:
        print(" Nenhuma pessoa na fila.")
        return
    filas["atendidos"] += 1


def relatorio(filas):
    total_fila = len(filas["prioritarios"]) + len(filas["normais"])
    total_prioritarios = len(filas["prioritarios"])
    total_normais = len(filas["normais"])

    print("\nRELATÓRIO:")
    print(f"Total atendidos: {filas['atendidos']}")
    print(f"Pessoas na fila prioritária: {total_prioritarios}")
    print(f"Pessoas na fila normal: {total_normais}")
    if total_fila > 0:
        perc_prioritarios = (total_prioritarios / total_fila) * 100
        print(f"Percentual de prioritários na fila: {perc_prioritarios:.2f}%")
    else:
        print("Não há pessoas na fila.")
    print()

filas = {"prioritarios": [], "normais": [], "atendidos": 0}

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar pessoa")
    print("2 - Listar filas")
    print("3 - Atender próximo")
    print("4 - Relatório")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_pessoa(filas)
    elif opcao == "2":
        listar_filas(filas)
    elif opcao == "3":
        atender_proximo(filas)
    elif opcao == "4":
        relatorio(filas)
    elif opcao == "5":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 5.")
