########### Exercício 1 ###########
# Escreva um programa que peça ao usuário para digitar seu nome e, em seguida, imprima uma mensagem de boas-vindas com o nome fornecido.

nome_usuario = input("Por favor, digite seu nome: ")
print(f"Olá, {nome_usuario}! Seja muito bem vindo(a)!")

########### Exercício 2 ###########
# Crie duas variáveis, numero1 e numero2, e atribua a elas valores inteiros. Calcule a soma, subtração, multiplicação e divisão dessas variáveis e imprima os resultados.

numero1 = 10
numero2 = 17

soma_resultado = numero1 + numero2 
print(f"A soma dos números é: {soma_resultado}")

subtracao_resultado = numero1 - numero2 
print(f"A subtração dos números é: {subtracao_resultado}")

multiplicacao_resultado = numero1 * numero2 
print(f"A multiplicação dos números é: {multiplicacao_resultado}")

divisao_resultado = numero1 / numero2 
print(f"A divisão dos números é: {divisao_resultado}")

########### Exercício 3 ###########
# Qual é a principal diferença entre uma variável de escopo local e uma de escopo global?

# Uma variável global pode ser chamada em qualquer momento dentro do código. Já a variável local, só pode ser chamada dentro de onde ela foi criada, por ex: dentro de uma função.

########### Exercício 4 ###########
# Crie uma variável chamada saldo com o valor 500.50 (float). Em seguida, crie uma variável saque com o valor 200.25 (float). Subtraia o saque do saldo e imprima o saldo final formatado para duas casas decimais.

saldo = 500.50
saque = 200.25

saque_do_saldo = saldo - saque
print(f"O saldo final é de: {saque_do_saldo:.2f}")

########### Exercício 5 ###########
# Declare uma variável booleana chamada tem_carteira_de_motorista e atribua a ela o valor True. Imprima uma mensagem que diga "Pode dirigir" se a variável for verdadeira e "Não pode dirigir" caso contrário.

tem_carteira_motorista = True
print(f"Pode dirigir. {tem_carteira_motorista}")

########### Exercício 6 ###########
# Crie duas variáveis:
idade_ana = 25
idade_beto = 30

# Use operadores de comparação para verificar se a idade de Ana é menor que a de Beto e imprima o resultado booleano.
print(f"O resultado é: {idade_ana < idade_beto}")

########### Exercício 7 ###########
# Receba um número inteiro do usuário e use o operador de módulo (%) para verificar se o número é par ou ímpar. Imprima o resultado.

numero_digitado_str = input("Digite um número inteiro.")
numero_digitado_int = int(numero_digitado_str)
modulo_num = numero_digitado_int % 2
print(f"O número digitado é: {numero_digitado_int}. E o módulo dele é: {modulo_num}")

########### Exercício 8 ###########
# Crie duas variáveis booleanas:

esta_chovendo = True
guarda_chuva = False

# Use operadores lógicos para verificar se uma pessoa vai se molhar (se está chovendo E ela não tem guarda-chuva).
print(f"A pessoa vai se molhar? {esta_chovendo and not guarda_chuva}")

########### Exercício 9 ###########
# Calcule a potência de 2 elevado a 10 e imprima o resultado.

a = 2
b = 10
potencia = a ** b

print(f"A potência de {a}, elevado a {b} é: {potencia}")

########### Exercício 10 ###########
# Converta a string "2026" para um tipo inteiro e armazene-a em uma variável chamada ano. Em seguida, some 1 a essa variável e imprima o novo ano.

ano_str = "2026"
ano = int(ano_str)

ano_novo = ano + 1
print(f'Feliz {ano_novo}!')

########### Exercício 11 ###########
# Crie a string:
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "

frase_sem_espaco = frase.strip()
print(frase_sem_espaco)

########### Exercício 12 ###########
frase_maiuscula = frase_sem_espaco.upper()
print(frase_maiuscula)

########### Exercício 13 ###########
print(f"Subtituindo palavras: {frase_sem_espaco.replace('poderosa', 'incrível')}")

########### Exercício 14 ###########
print(f"O tamanho da frase inteira é: {len(frase_sem_espaco)}")

########### Exercício 15 ###########
print(f"Fatiamento da frase: {frase_sem_espaco[0:6]}")

########### Exercício 16 ###########
lista_compras = ["arroz", "feijão", "macarrão", "carne"]
print(f"A lista de compras tem: {lista_compras}")

########### Exercício 17 ###########
lista_compras.append("leite")
print(lista_compras)

########### Exercício 18 ###########
print(lista_compras[1])

########### Exercício 19 ###########
lista_compras.remove("macarrão")
print(lista_compras)

########### Exercício 20 ###########
numeros = [1, 2, 3, 4, 5]
print(f"A lista contém {len(numeros)} índices.")

########### Exercício 21 ###########
meses = ("Janeiro", "Fevereiro", "Março")

########### Exercício 22 ###########
# Tupla é imutável, não pode ser alterada depois de criada.

########### Exercício 23 ###########
print(f"O primeiro mês do ano é {meses[0]}")

########### Exercício 24 ###########
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}

########### Exercício 25 ###########
print(f"O ano de lançamento do filme é: {filme.get('ano')}")

########### Exercício 26 ###########
filme["genero"] = "Drama"
print(filme)

########### Exercício 27 ###########
filme["ano"] = 1973
print(filme.get('ano'))

########### Exercício 28 ###########
lista_num = [1, 2, 2, 3, 4, 4, 5, 1]
lista_sem_duplicados = set(lista_num)
print(lista_sem_duplicados)

########### Exercício 29 ###########
set_a = {1, 2, 3, 4, 6}
set_b = {3, 4, 5, 6}
intersecao = set_a.intersection(set_b)
print(intersecao)

########### Exercício 30 ###########
altura_str = input("Digite a sua altura em metros(ex: 1.75): ")
peso_str = input("Digite seu peso em quilogramas(ex: 68.5): ")

altura_float = float(altura_str)
peso_float = float(peso_str)

imc = peso_float / (altura_float ** 2)

print(f"O calculo do IMC é: {imc:.2f}")