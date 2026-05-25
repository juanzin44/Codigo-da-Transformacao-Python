print("Bem-vindo ao Módulo 02 - Lógica de Programação")
print()

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número zero")

print()

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print()

senha = input("Digite a senha: ")

if senha == "python123":
    print("Acesso permitido")
else:
    print("Senha incorreta")

print()

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

print()

for i in range(1, 11):
    print(i)

print()

for i in range(2, 21, 2):
    print("Número par:", i)

print()

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1

print()

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print()

soma = 0

for i in range(1, 6):
    valor = int(input(f"Digite o {i}º valor: "))
    soma += valor

print("Soma total:", soma)
print()

nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Lista de nomes:")

for nome in nomes:
    print(nome)

print()

numeros = [10, 20, 30, 40, 50]

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Soma da lista:", sum(numeros))
print()

numero = int(input("Digite um número para verificar: "))

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")

print()

contador = 10

while contador >= 1:
    print(contador)
    contador -= 1

print("Fim da contagem!")
print()

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso")
else:
    print("Usuário ou senha inválidos")

print()

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

print()

for i in range(1, 6):
    if i == 4:
        break

    print(i)

print()

def calcular_area(base, altura):
    area = base * altura
    return area

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

resultado = calcular_area(base, altura)

print("Área:", resultado)
print()

def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

idade = int(input("Digite sua idade: "))

print(verificar_maioridade(idade))
print()

print("===== DESAFIO FINAL =====")

numero_secreto = 7

tentativa = int(input("Tente adivinhar o número: "))

while tentativa != numero_secreto:
    print("Número incorreto")
    tentativa = int(input("Tente novamente: "))

print("Parabéns! Você acertou o número.")
