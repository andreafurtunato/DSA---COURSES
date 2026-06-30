### TOMADA DE DECISÃO COM ESTRUTURAS CONDICIONAIS ###

# if / elif / else

# Define a variável
nota = 6

#Agora checamos o valor da variável e tomamos decisões.
if nota >= 7.0:
    print(f"Aprovado! Parabéns pela nota {nota}!!")
else: 
    print(f"Reprovado. Sua nota foi menor que a média.")


############################################################

idade = 70

if idade < 18:   ## primeira condição.
    print("Menor de idade")
elif idade > 18 and idade < 65:   ## segunda condição.
    print("Você é adulto.")
else:                             ## ultima condição.
    print("Idoso.")

############################################################
            ### LAÇOS DE REPETIÇÃO ###

## for 

## Listas
frutas = ['Banana', 'Laranja', 'Maçã', 'Pera']

for fruta in frutas:          ## for variavel in lista 
    print(f'- {fruta}') 

## Tuplas
cores = ('vermelho', 'branco', 'azul', 'verde')

for cor in cores:
    print(cor)

## Dicionários
formacoes_dsa = {
    "Formação Cientista de Dados": 6,
    "Formação Analista de Dados": 4,
    "Formação Engenheiro de Dados": 5
}
for chave, valor in formacoes_dsa.items():    # para cada chave e valor, dentro dicionarios, busque os itens e imprima
    print(chave,':', valor)

############################################################

#exemplo com função range
print("\nContagem até 5: ")
for numero in range(6):  #gera numero até 5 ( 0 a 5 )
    print(numero)

############################################################
## while

#Define a variavel
contador = 5

#Imprime a mensagem
print("Contagem regressiva: ")

while contador > 0:
    print(contador)
    contador -=1    #contador = contador - 1

# Quando usar While ou For?
# For é usado quando voce ja sabe sobre o que quer iterar(lista, tupla, dicionário, range etc). Ele percorre cada elemento de uma sequencia ou iterável de forma automática
# sem que voce precise gerenciar manualmente a condiução separada.

# Já o While é usado quando vc nao sabe previamente quantas vezes o loop vai rodar e a repetição depende de uma condição booleana que deve
# continuar verdadeira para q o loop prossiga. Voce precisa cuidar manualmente de alterar o estado dessa condicação para evitar loops infinitos.

# For -> ideal para quando vc ja tem uma coleção ou numero definido de repetições.
# While -> ideal quando a repetição depende de uma condição que pode mudar ao longo da execução.

############################################################

# Iteração sobre estruturas de dados com loops e condicionais.

#Tupla
numeros = (3,7,10,15,20)

#Itera pela tupla e mostra apenas os numeros pares
for n in numeros:
    if n % 2 == 0:   # se o resto da divisão de um número por 2, for igual a 0 = número é par
        print(f"{n} É PAR.")

#Lista
nomes = {"Andrea", "Bianca", "Carla"}

for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome que começa com A: {nome}")

#Dicionário
produtos = {"arroz": 25, "feijão": 12, "macarrão": 7, "carne": 45}

for item, preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais.")

############################################################
#Controle de fluxo

numeros =  [1,2,3,4,5,6,7,8,9]

#Mensagem
print("\nBuscando pelo número 5...")

#Loop com break.
for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado.")
        break
    print(f"Verificando {numero}...")


print("\nImprimindo apenas os números ímpares: ")

#Loop com continue.
for numero in range(1,11):
    if numero % 2 == 0:
        continue  ## pula e imprime somente os numeros impares
    print(numero)

############################################################
# Comprehensions (List, set, dict e generator)

# estruturas que são consideradas construtores sintáticos, ou expressões de compreensão.

# Lista comprehension -> expressão que gera listas.
# Set comprehension -> empressão que gera conjuntos
# Dict comprehenrion  -> expressão que gera dicionários.
# Generator expression -> empressão que gera iteradores.

# Criando uma lista de quadrados dos números de 0 a 9
quadrados = [x ** 2 for x in range(10)]
print(f"\nQuadrados de 0 a 9: {quadrados}")

# Criando uma lista de números pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]
print(f"Números de pares de 0 a 20: {pares}")

# Criando um dicionário com números e seus quadrados.
quadrado_dict = {x: x ** 2 for x in range(6)}
print(quadrado_dict)

# Conjuntos de quadrados (sem repetição)
quadrados_set = {x ** 2 for x in [1,2,3,3,4,4]}
print(quadrados_set)

#Generator expression
gen = (x ** 2 for x in range(6))
print(gen)

# Convertendo em tupla
quadrados_tupla = tuple(x ** 2 for x in range(6))
print(quadrados_tupla)

############################################################

#Funções
# São blocos de código que sao reutilizaveis que realizam uma tarefa específica.

def dsa_saudacao():
    # Esta função exite uma saudação simples.
    print("\nOlá, bem vindo!")

dsa_saudacao() ## Aqui chamamos a função 

#Define uma função que retorna um valor 
def dsa_soma(a,b):
    return a + b

resultado = dsa_soma (5,4)
print(f"Resultado: {resultado}")


# Parametros e Argumentos de Funções

#Argumentos posicionais
def dsa_apresentacao(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

dsa_apresentacao("Andrea", 25)

# Argumentos nomeados 
dsa_apresentacao(idade = 30, nome = "Bob")

# Parametros com valores padrão(default)
def dsa_saudacao_completa (nome, saudacao = "Olá"):
    print(f"{saudacao}, {nome}!!")

# dsa_saudacao_completa() - dá erro, pois nao foi passado argumento nome

dsa_saudacao_completa("Andrea")

############################################################

#Argumentos de tamanho variável(*args)

def dsa_soma_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(f"A soma dos numeros: {dsa_soma_numeros(1,2,3,4,5)}")

############################################################
# Expressão LAMBDA
# São pequenas funções anonimas definidas com a palavra-chave "lambda"

#Uma funçao lambda que dobra um numero
dobro = lambda x: x* 2
print(f"O dobro de 7 é: {dobro(7)}")

########################################################################################################################
## Modulo Python = é um script em python. Importamos o script e utilizamos o método.

import math
# sqrt = Raiz quadrada inteira de um inteiro não negativo n
raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é: {int(raiz_quadrada)}")

import random 
#Gera um numero inteiro de 1 a 100 (definido)  = random.randit(a: int, b: int)
num_aleatorio = random.randint(1,100)
print(f"O número aleatório entre 1 e 100: {num_aleatorio}")

#Seleciona aleartoriamente uma cidade da lista fornecida
cidade_aleatoria = random.choice(["Rio de Janeiro", "Salvador", "Curitiba", "São Paulo"])
print(f"A cidade escolhida foi: {cidade_aleatoria}")

#########################################################
## Criando e importando o próprio módulo.

