'''
Problema real — Análise de vendas
Uma empresa registrou as vendas de uma semana na lista vendas = [1250, 980, 1430, 2100, 1750,
890, 1620]. Desenvolva um programa que calcule o total vendido, a média diária, a maior e a menor
venda, quantos dias ficaram acima da média e o percentual de dias acima da média.
'''



# Dados das vendas da semana (Segunda a Domingo)
vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]

# 1. Total vendido
total_vendido = sum(vendas)

# 2. Média diária
media_diaria = total_vendido / len(vendas)

# 3. Maior e menor venda (usando float('-inf') e float('inf'))
maior_venda = float("-inf")
menor_venda = float("inf")

for valor in vendas:
    if valor > maior_venda:
        maior_venda = valor
    if valor < menor_venda:
        menor_venda = valor

# 4. Dias acima da média
dias_acima_media = 0
for valor in vendas:
    if valor > media_diaria:
        dias_acima_media += 1

# 5. Percentual de dias acima da média
percentual_acima = (dias_acima_media / len(vendas)) * 100

# Exibição dos resultados
print("=== RELATÓRIO DE VENDAS DA SEMANA ===")
print(f"Total vendido:               R$ {total_vendido:.2f}")
print(f"Média diária de vendas:      R$ {media_diaria:.2f}")
print(f"Maior venda registrada:      R$ {maior_venda:.2f}")
print(f"Menor venda registrada:      R$ {menor_venda:.2f}")
print(f"Dias acima da média:         {dias_acima_media} dia(s)")
print(f"Percentual acima da média:   {percentual_acima:.2f}%")