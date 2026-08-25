'''
Problema real — Controle de estoque
Uma pequena loja possui os produtos ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"] e as
respectivas quantidades [12, 25, 4, 3, 8]. Desenvolva um programa que permita consultar um produto,
alterar sua quantidade e listar os produtos com estoque inferior a 5 unidades. Ao final, informe qual
produto possui a maior quantidade em estoque.
'''
# Dados iniciais do estoque
produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
quantidades = [12, 25, 4, 3, 8]


def consultar_produto():
    nome = input("\nDigite o nome do produto: ").strip()

    # Busca ignorando maiúsculas/minúsculas
    for i in range(len(produtos)):
        if produtos[i].lower() == nome.lower():
            print(f"-> Estoque de {produtos[i]}: {quantidades[i]} unidade(s).")
            return

    print("-> Produto não encontrado no cadastro.")


def alterar_quantidade():
    nome = input("\nDigite o nome do produto a alterar: ").strip()

    for i in range(len(produtos)):
        if produtos[i].lower() == nome.lower():
            try:
                nova_qtd = int(
                    input(f"Digite a nova quantidade para {produtos[i]}: ")
                )
                if nova_qtd < 0:
                    print("-> A quantidade não pode ser negativa.")
                    return
                quantidades[i] = nova_qtd
                print(
                    f"-> Quantidade de {produtos[i]} atualizada para {quantidades[i]}."
                )
                return
            except ValueError:
                print("-> Erro: Por favor, digite um número inteiro válido.")
                return

    print("-> Produto não encontrado no cadastro.")


def listar_baixo_estoque():
    print("\n--- Produtos com estoque baixo (< 5 unidades) ---")
    encontrou = False

    for i in range(len(produtos)):
        if quantidades[i] < 5:
            print(f"- {produtos[i]}: {quantidades[i]} unidade(s)")
            encontrou = True

    if not encontrou:
        print("-> Nenhum produto com estoque inferior a 5 unidades.")


def produto_maior_estoque():
    if not quantidades:
        print("-> Estoque vazio.")
        return

    # Usando float('-inf') para garantir a comparação correta do maior valor
    maior_qtd = float("-inf")
    indice_maior = -1

    for i in range(len(quantidades)):
        if quantidades[i] > maior_qtd:
            maior_qtd = quantidades[i]
            indice_maior = i

    print(
        f"\n-> Produto com maior estoque: {produtos[indice_maior]} ({quantidades[indice_maior]} unidades)"
    )


# Loop principal do menu
while True:
    print("\n" + "=" * 35)
    print("      SISTEMA DE ESTOQUE")
    print("=" * 35)
    print("1 - Consultar produto")
    print("2 - Alterar quantidade de um produto")
    print("3 - Listar produtos com estoque baixo (< 5)")
    print("4 - Mostrar produto com maior estoque")
    print("5 - Sair")

    opcao = input("Escolha uma opção (1-5): ").strip()

    if opcao == "1":
        consultar_produto()
    elif opcao == "2":
        alterar_quantidade()
    elif opcao == "3":
        listar_baixo_estoque()
    elif opcao == "4":
        produto_maior_estoque()
    elif opcao == "5":
        print("\nSaindo do programa. Até logo!")
        break
    else:
        print("\n-> Opção inválida! Digite um número de 1 a 5.")

