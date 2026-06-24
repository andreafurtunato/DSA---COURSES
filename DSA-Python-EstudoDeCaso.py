##### JOGO - PEDRA, PAPEL OU TESOURA #####

# Apresentação do jogo

print("########################################")
print("#      PEDRA, PAPEL E TESOURA          #")
print("########################################")

print("\nEscolha uma opção:")
print("- pedra")
print("- papel")
print("- tesoura")
print("\n----------------------------------------")

opcoes_validas = ("pedra", "papel", "tesoura")
print(f"Opções válidas: {opcoes_validas}")
print("----------------------------------------")

# Coleta dos Dados
jogador1 = input("\nJOGADOR 1 - Por favor, digite a sua escolha: ")
jogador2 = input("\nJOGADOR 2 - Por favor, digite a sua escolha: ")
print("\n----------------------------------------")
# Tratamento dos Dados
jogador1_convert = jogador1.strip().lower()
jogador2_convert = jogador2.strip().lower()

print(f"\nJogador 1 escolheu: {jogador1_convert}")
print(f"Jogador 2 escolheu: {jogador2_convert}")
print("\n----------------------------------------")

# Lógica de vencedor
if jogador1_convert == jogador2_convert: 
    print("\nResultado: EMPATE! Tentem novamente!")
# Boas práticas colocar as comparações dentro de um parênteses, dentro da condição.    
elif (
    (jogador1_convert == "pedra" and jogador2_convert == "tesoura") or
    (jogador1_convert == "tesoura" and jogador2_convert == "papel") or
    (jogador1_convert == "papel" and jogador2_convert == "pedra")
):
        print("\nResultado: Jogador 1 venceu!!")
else:
    print("\nResultado: Jogador 2 venceu!")   

print("\nFIM DE JOGO!")

    