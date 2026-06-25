# Variáveis: Declaração, Atribuição e Regras de Nomenclatura

# String - texto
# Int - inteiro
# Float - ponto flutuante
# Boolean - true/false

nome = "Andrea"
idade = 25
altura = 1.60
estudante = True

print(f"O nome é: {nome}")
print(f"A idade é: {idade}")
print(f"A altura é {altura}")
print(f"É estudante? {estudante}")


# Tipo de dado
# Linguagem dinamicamente tipada - não precisa declarar o tipo das variáveis ao crialas, pois ele descobre automaticamente pelo valor atribuido

x = 10 
x1 = 10
y = "10"

# Podemos somar tipos numericos, mas nao podemos somar numero com string. 

type(x) # Retorna o tipo da variável.

# Escopo de variáveis: Globais e Locais

#Variável Global
saudacao = "Olá, Mundo!"
nome =  "Aluno DSA"

def minha_funcao_dsa():
    #Variável local
    nome= "Andrea"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global dentro da função: {saudacao}")
minha_funcao_dsa()

print(f"\nFora da funcao: {saudacao}")
print(f"\nFora da funcao: {nome}")

# Definir variáveis bem claras, e deixar claro com códigos o que são variáveis globais e locais

# Tipos de dados primitivos 

#Integer(Inteiro)
inteiro = 100 
print(f"Valor: {inteiro}, Tipo: {type(inteiro)}")

# String(texto)
nome = "Andrea"
print(f"O nome é: {nome}, Tipo: {type(nome)}")

############################################################################
# Operadores aritmeticos
a = 10
b = 9

soma = a + b 
subtracao = a - b
multiplicacao = a * b
divisao = a / b 
divisao_inteira =  a // b
mod = a % b
potencia = a ** b

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {mod}")
print(f"{a} ** {b} = {potencia}")


# 8 + 's' # Não pode, não soma tipos diferentes
'8' + 's' # Pode! Não é soma, é concatenação. 

##########################################################################
# Operadores de comparação
x = 5
y = 10

# Maior que
x > y 

#Menor que
x < y 

#Igual a 
x == y

#Diferente de
x != y

#Menor ou igual a 
x <= y

############################################################################
## Operadores lógicos
tem_dinheiro = True
tem_tempo = False

# Operador AND(e): Ambos precisam ser verdadeiros
print(f"O Cliente pode viajar? {tem_dinheiro and tem_tempo}")

#Operador OR(ou): Pelo menos um precisa ser verdadeiro.
print(f"O cliente pode viajar? {tem_dinheiro or tem_tempo}")

#Operador NOT(não): Inverte o valor booleano 
print(f"O cliente pode viajar? {tem_dinheiro and not tem_tempo}")

############################################################################
# Manipulação de Strings

#Define uma variável do tipo string.
frase = " Aprender Python é divertido! "

#Concatenação
nome = "Andrea"
saudacao = "Olá, " + nome + "!"
print(saudacao)

#Tamanho da String
print(f"Tamanho da frase: {len(frase)}")

#Maiusculo e Minusculo
print(f"Maiusculas: {frase.upper()}")
print(f"Minusculas: {frase.lower()}")

# Remover espaços em branco do inicio e do fim
frase_sem_espaco = frase.strip()
print(f"Frase sem espaço: '{frase_sem_espaco}'")

#Substituir texto - replace = substituir 
#   .replace(palavra antiga, palavra nova)
print(f"Substituindo 'divertido' por legal': {frase_sem_espaco.replace('divertido', 'legal')}")

############ IMPORTANTE PRA FUNÇÃO DE GERAR DV #############
# Fatiamente (Slicing) - Acessando partes de uma string
# O indice em Python começa em 0
print(frase_sem_espaco)
print(f"O primeiro caractere é: {frase_sem_espaco[0]}")
print(f"A Palavra Python: {frase_sem_espaco[9:15]}")

############################################################
## Estrutura de dados


# Listas
#Criando uma lista

frutas = ["Maçã", "Banana", "Uva", "Pera"]
print(f"As frutas são: {frutas}")

type(frutas)

# Acessando um item pelo índice
print(f"A primeira fruta é: {frutas[0]}")
print(f"A última fruta é: {frutas[-1]}")

#Adicionar ao final de lista
frutas.append("Laranja")
print(f"Lista com acréscimo:  {frutas}")

#Remove um item da lista
frutas.remove("Uva")
print(f"Frutas sem a Uva: {frutas}")

# Modificando itens
frutas[1] = "Kiwi"
print(f"Frutas com a subsituição da Banana: {frutas}")

#Verificando tamanho da lista
print(f"A lista tem {len(frutas)} frutas")

#Deleta a lista.
del frutas



#### TUPLAS ####
#São coleçoes ordenadas e imutáveis de itens. Uma vez criadas, nao pode ser alterada.

# Criando uma tupla
coordenadas = (10.2,20.5)
print(f"Tupla de coordenadas: {coordenadas}")

type(coordenadas)

# Tuplas são úteis para dados que não devem ser alterados, como meses do ano, coordrenadas, etc
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(f"O primeiro dia da semana é: {dias_da_semana[0]}")

#### DICIONARIOS ####
#São coleções de pares chave: valor. São mutáveis.

aluno = {
    "nome": "Andrea",
    "idade": 25,
    "curso": "Data Engineer",
    "aluno_ativo": True
    }

print(f"Dicionário do aluno: {aluno}")
type(aluno)

# Acessando um valor pela sua chave-valor
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get("curso")}")  ## .get() é uma forma segura de acessar chaves

# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print(f"Dicionário do aluno atualizado: {aluno}")

#Modificando chaves
aluno['idade'] = 27
print(f"Idade atualizada: {aluno}")

#### CONJUNTOS( SETS ) ####
# São coleções nao ordenadas de itens únicos e mutáveis. São úteis para remover duplicatas e realizar operações matemáticas de conjuntos(união, interseção)

# Criando um conjunto(numeros repetidos sao removidos)
numeros = {1,2,3,4,2,3,5}
print(f"Conjunto de números sem duplicatas: {numeros}")

# Adicionando um item
numeros.add(6)
print(f"Após adicionar o valor 6: \n{numeros}")

#Removendo um item
numeros.remove(2)
print(f"Após remover o valor 2: \n{numeros}")

#Operações de conjunto

conjunto_a = {1,2,3,4,5}
conjunto_b = {4,7,3,9,10}

# Uniao (todos os elementos de ambos os conjuntos)
uniao =  conjunto_a.union(conjunto_b)
print(f"Conjuntos unidos: {uniao}")

# Interseção (elementos que estão em ambos os conuuntos)
intersection = conjunto_a.intersection(conjunto_b)
print(f"Interseção de conjuntos: {intersection}")

#### CONVERSÃO ENTRE TIPOS DE DADOS (TYPE CASTING) ####

#Convertendo de string para inteiro
numero_em_texto = "123"
numer_inteiro = int(numero_em_texto)
print(f"Transformando uma String '{numero_em_texto}' para Integer: {numer_inteiro}, Tipo: {type(numer_inteiro)}")

#Convertendo de string para float
numero_decimal_texto = "63.22"
numero_float = float(numero_decimal_texto)
print(f"Numero decimal em texto: '{numero_decimal_texto}', tranformado em float: {numero_float}. Tipo: {type(numero_float)}")

#Convertendo número inteiro para string  ############ (IMPORTANTE PARA O GERADOR DE DV) ###############
cnpj = 12345678000195
cnpj_string = str(cnpj)
print(f"Transformando CNPJ {cnpj}, em texto para tratar DV '{cnpj_string}'. Tipo: {type(cnpj_string)}")


#Convertendo entre estruturas
lista_com_duplicatas = [1,2,3,4,5,2,4]
lista_unica = set(lista_com_duplicatas)   # set remove as duplicatas
lista_sem_duplicatas = list(lista_unica)

print(f"Lista com dupicatas: {lista_com_duplicatas}")
print(f"Lista única e tratada: {lista_unica}")
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")

#### Entrada e Saída Padrão ####

#Saída mais comum = output

nome = "Juliana"
idade = 30
cidade = "Salvador"

#Usand f-string (mais moderna e recomendada) // formatação de saída
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}")

#Formatando números
preco = 49.22233
print(f"O preço do produto é R$ {preco:.2f}") # Formata para 2 casas decimais   :.2f

#Entrada mais comum = input 
# Sempre retorna string

nome_usuario = input("Qual é o seu nome?")

#Pedir a idade e tranformar em int
idade_usuario_str = input("Digite a sua idade.")
idade_usuario_int = int(idade_usuario_str)

from datetime import date

# Pega o ano corrente na data definida no sistema da máquina
ano_atual = date.today().year

#Processando dados
ano_nascimento = ano_atual - idade_usuario_int

#Exibindo resultado
print(f"\n Olá, {nome_usuario}!!. Bem vindo(a)!")
print(f"Você tem {idade_usuario_int} anos e nasceu em {ano_nascimento}")

