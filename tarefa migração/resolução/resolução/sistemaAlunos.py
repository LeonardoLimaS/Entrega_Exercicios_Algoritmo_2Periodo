notas = {}
lista_nomes = []


def adicionar_aluno():
    nome = input("Nome do aluno: ")
    nota = float(input("Nota final: "))
    notas[nome] = nota
    lista_nomes.append(nome)
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if not lista_nomes:
        print("Nenhum aluno cadastrado.")
        return
    print("\nLista de alunos:")
    for nome in lista_nomes:
        print(f"- {nome} | Nota: {notas[nome]:.2f}")


def buscar_nota():
    nome = input("Nome do aluno: ")
    if nome in notas:
        print(f"Nota de {nome}: {notas[nome]:.2f}")
    else:
        print("Aluno não encontrado.")


while True:
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar nota")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            buscar_nota()
        case 0:
            print("Encerrando...")
            break
        case _:
            print("Opção inválida!")
