print("Olá, seja bem-vindo ao curso de Python!")
print("Vamos aprender os conceitos básicos da linguagem.\n")

nome = "João"
idade = 17
altura = 1.75
estudando = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Está estudando?", estudando)
print()

print("Tipo da variável nome:", type(nome))
print("Tipo da variável idade:", type(idade))
print("Tipo da variável altura:", type(altura))
print("Tipo da variável estudando:", type(estudando))
print()

numero1 = 10
numero2 = 5

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print()

cidade = input("Digite sua cidade: ")
print("Você mora em:", cidade)
print()

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade_usuario = 2026 - ano_nascimento

print("Sua idade aproximada é:", idade_usuario)
print()

nota = 8

print("Nota maior que 7?", nota > 7)
print("Nota menor que 5?", nota < 5)
print("Nota igual a 8?", nota == 8)
print()

idade = 20
possui_carteira = True

print("Pode dirigir?", idade >= 18 and possui_carteira)
print()

media = float(input("Digite sua média: "))

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")

print()

print("Contagem de 1 até 5:")

for numero in range(1, 6):
    print(numero)

print()

contador = 1

while contador <= 5:
    print("Número:", contador)
    contador += 1

print()

frutas = ["Maçã", "Banana", "Laranja"]

print("Lista de frutas:")

for fruta in frutas:
    print(fruta)

print()

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo.")

saudacao("Maria")
print()

print("===== DESAFIO FINAL =====")

valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))

print("Soma:", valor1 + valor2)
print("Subtração:", valor1 - valor2)
print("Multiplicação:", valor1 * valor2)

if valor2 != 0:
    print("Divisão:", valor1 / valor2)
else:
    print("Não é possível dividir por zero.")

print("\nFim do módulo 01!")



















