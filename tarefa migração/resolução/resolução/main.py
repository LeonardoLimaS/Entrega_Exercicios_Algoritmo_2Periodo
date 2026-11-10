class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

funcionarios = []

def adicionarFuncionario():
    if (len(funcionarios) >= 100):
        print("Limite atingido!")
        return

    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")

    funcionarios.append(Funcionario(nome, cargo, salario))
    print("Funcionário cadastrado!\n")

def listarFuncionarios():
    if (len(funcionarios) == 0):
        print("Nenhum funcionário cadastrado.\n")
        return

    print("\nLista de funcionários:\n")
    for i in range(len(funcionarios)):
        print("%d) %s - %s - R$ %.2f\n" % (i + 1, funcionarios[i].nome, funcionarios[i].cargo, float(funcionarios[i].salario)))

def buscarFuncionario():
    nomeBusca = input("Nome do funcionário: ")

    for i in range(len(funcionarios)):
        if (funcionarios[i].nome == nomeBusca):
            print("Cargo: %s | Salário: R$ %.2f\n" % (funcionarios[i].cargo, float(funcionarios[i].salario)))
            return
    
    print("Funcionário não encontrado.\n")


while True:
    print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("0 - Sair")
    print("Escolha uma opção: ")
    opcao = int(input())

    match (opcao):
        case 1: 
            adicionarFuncionario()
        case 2: 
            listarFuncionarios()
        case 3: 
            buscarFuncionario()
        case 0: 
            print("Encerrando...\n")
        case _: 
            print("Opção inválida!\n")

    if (opcao == 0):
        break

