# 📌 Mini Projeto - Cadastro de Pessoa e Cálculo de IMC
# Crie um programa em Python que:

# 1. Peça ao usuário:
#    - Nome
#    - Idade
#    - Peso (em kg)
#    - Altura (em metros).

print("\n############## CÁLCULO DE IMC ##############")

nome_usuario = input("\nDigite o seu nome completo: ")
idade_usuario = int(input("Digite a sua idade: "))
peso_usuario = float(input("Digite o seu peso em kg: "))
altura_usuario = float(input("Digite a sua altura em metros: "))

# 2. Calcule o IMC usando a fórmula:
#    IMC = peso / (altura ** 2)

imc = peso_usuario / (altura_usuario ** 2)
print(f"\nO cálculo de IMC da(o) {nome_usuario} é: {imc:.2f}")

# 3. Armazene todas as informações em um dicionário chamado "pessoa":
#    - nome
#    - idade
#    - peso
#    - altura
#    - imc

pessoa = {
    "nome": nome_usuario,
    "idade": idade_usuario,
    "peso": peso_usuario,
    "altura": altura_usuario,
    "imc": imc
}

# 4. Exiba todas as informações na tela de forma organizada

print(
    f"\nDados do usuário:"
    f"\nNome: {pessoa['nome']}"
    f"\nIdade: {pessoa['idade']}"
    f"\nPeso: {pessoa['peso']}"
    f"\nAltura: {pessoa['altura']}"
    f"\nIMC: {pessoa['imc']:.2f}"
)

print("\n########################################################")