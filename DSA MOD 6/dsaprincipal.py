import modulodsa

mensagem = modulodsa.dsa_saudacao("Dea")
print(mensagem)

print(f"O vaor de PI do nosso módulo é: {modulodsa.PI}")

from modulodsa import dsa_saudacao, PI

mensagem_direta = dsa_saudacao("Aluno DSA")
print(mensagem_direta)
print(f"O valor de PI importado é: {PI}")