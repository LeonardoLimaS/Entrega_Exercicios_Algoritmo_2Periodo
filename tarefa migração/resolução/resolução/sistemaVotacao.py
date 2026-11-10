opcoes = ["Opção 1", "Opção 2", "Opção 3"]
votos = [0] * len(opcoes)

print("=== SISTEMA DE VOTAÇÃO ===")
print("As opções são:")
for i, opcao in enumerate(opcoes):
    print(f"{i + 1} - {opcao}")

while True:
    entrada = input(f"\nEscolha uma opção (1-{len(opcoes)}) ou 0 para encerrar: ")

    if not entrada.isdigit():
        print("Entrada inválida. Digite apenas números.")
        continue

    escolha = int(entrada)

    if escolha == 0:
        break
    elif 1 <= escolha <= len(opcoes):
        votos[escolha - 1] += 1
        print(f"Você votou na {opcoes[escolha - 1]}")
    else:
        print("Opção inválida. Tente novamente.")

print("\n=== RESULTADOS FINAIS ===")
for i, opcao in enumerate(opcoes):
    print(f"{opcao}: {votos[i]} voto(s)")
