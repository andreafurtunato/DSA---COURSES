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
    contador -=1   #contador = contador - 1
