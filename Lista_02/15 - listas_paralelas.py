'''
Listas paralelas
Crie duas listas: uma com 5 nomes de alunos e outra com suas respectivas notas. Percorra as listas
simultaneamente e exiba o nome, a nota e a situação de cada aluno, considerando aprovação com
nota maior ou igual a 6.
'''
alunos = ["Alice", "Bob", "Charlie", "David", "Eve"]
notas = [7.5, 8.0, 5.5, 9.0, 6.5]

for i in range(len(alunos)):
    nome = alunos[i]
    nota = notas[i]
    if nota >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"Nome: {nome}, Nota: {nota}, Situação: {situacao}")