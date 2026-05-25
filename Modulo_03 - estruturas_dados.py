print("Bem-vindo ao Módulo 03 - Estruturas de Dados")
print()

nomes = ["Ana", "Carlos", "Marina", "João"]

print("Lista de nomes:")
for nome in nomes:
    print(nome)

print()

numeros = [10, 20, 30, 40, 50]

print("Primeiro número:", numeros[0])
print("Último número:", numeros[-1])

print()

numeros.append(60)

print("Lista após adicionar elemento:")
print(numeros)

print()

numeros.remove(20)

print("Lista após remover elemento:")
print(numeros)

print()

print("Quantidade de elementos:", len(numeros))
print()

for numero in numeros:
    print("Número:", numero)

print()

soma = sum(numeros)

print("Soma dos números:", soma)
print()

maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)
print()

numeros.sort()

print("Lista em ordem crescente:")
print(numeros)

print()

numeros.sort(reverse=True)

print("Lista em ordem decrescente:")
print(numeros)

print()

tupla = ("Python", "Java", "C#", "JavaScript")

print("Elementos da tupla:")

for linguagem in tupla:
    print(linguagem)

print()

print("Quantidade de itens da tupla:", len(tupla))
print()

aluno = {
    "nome": "Lucas",
    "idade": 18,
    "curso": "Python"
}

print("Dados do aluno:")
print(aluno)

print()

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])

print()

aluno["idade"] = 19

print("Dicionário atualizado:")
print(aluno)

print()

aluno["cidade"] = "São Paulo"

print("Novo campo adicionado:")
print(aluno)

print()

for chave, valor in aluno.items():
    print(chave, ":", valor)

print()

frutas = {"maçã", "banana", "uva", "laranja"}

print("Elementos do conjunto:")

for fruta in frutas:
    print(fruta)

print()

frutas.add("melancia")

print("Conjunto atualizado:")
print(frutas)

print()

frutas.discard("banana")

print("Conjunto após remoção:")
print(frutas)

print()

lista_numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

print("Lista digitada:")
print(lista_numeros)

print()

print("Maior valor:", max(lista_numeros))
print("Menor valor:", min(lista_numeros))
print("Soma:", sum(lista_numeros))

print()

pares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Números pares:")
print(pares)

print()

produtos = []

for i in range(3):
    produto = input("Digite o nome do produto: ")
    produtos.append(produto)

print("Produtos cadastrados:")

for produto in produtos:
    print(produto)

print()

estoque = {
    "Notebook": 5,
    "Mouse": 10,
    "Teclado": 7
}

print("Controle de estoque:")

for produto, quantidade in estoque.items():
    print(produto, "-", quantidade)

print()

estoque["Monitor"] = 4

print("Estoque atualizado:")
print(estoque)

print()

notas = {
    "Ana": 8.5,
    "Carlos": 7.0,
    "Marina": 9.2
}

media = sum(notas.values()) / len(notas)

print("Média das notas:", media)
print()

for aluno, nota in notas.items():
    if nota >= 7:
        print(aluno, "aprovado")
    else:
        print(aluno, "reprovado")

print()

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")

for linha in matriz:
    print(linha)

print()

print("Elemento da posição [1][2]:", matriz[1][2])
print()

print("===== DESAFIO FINAL =====")

alunos = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    aluno = {
        "nome": nome,
        "nota": nota
    }

    alunos.append(aluno)

print()

print("Lista de alunos:")

for aluno in alunos:
    print(aluno["nome"], "-", aluno["nota"])

print()

media_turma = 0

for aluno in alunos:
    media_turma += aluno["nota"]

media_turma /= len(alunos)

print("Média da turma:", media_turma)
