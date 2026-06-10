# # 1. O Problema da Idade
# # idade = input("Digite sua idade: ")
# # if idade >= 18:
# # print("Você é maior de idade.")

# # Corrigido:
idade = input("Digite a sua idade: \n")
if idade <= 18:
    print("Você é menor de idade.")
elif idade >= 18: 
    print("Você é maior de idade.")
else:
    print("Já vivido")

# 2. A Escrita Fiel
#  nome = "Mariana"
# print("Seja bem-vinda, nome!")

# # corrigido
nome = "Mariana"
print(f"Seja Bem-vindo, {nome}")

#  Melhorado
nome = input(" Digite seu nome: \n")
nome = input(f"Seja Bem-vindo, {nome}")

# 3. Falta de Espaço
# numero = 10
# if numero > 5:
#   print("O número é maior que cinco.")
# else: 
#  print("O número é menor ou igual a cinco.")

# Corrigido:
numero = 10 
if numero > 5:
    print("O número é maior que cinco")
else:
    print("O número é menor ou igual a cinco.")

 # Melhorado:
print("")
numero = 10 
if numero > 5:
    print("O número é maior que cinco")
elif numero < 5: 
    print("O número é menor que cinco.")
else:
    print("O número é igual a cinco.")




# # 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# Corrigido:
usuario = "aluno123"
if usuario == "aluno123":
   print("Login realizado com sucesso.")

# Melhorado:
usuario = "aluno123"
if usuario == "aluno123":
   print("Login realizado com sucesso.")
elif usuario == "aluno123@":
   print("Login não identificado")
else:
   print("Acesso não autorizado")
   

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

Corrigido:
clima = input("Como está o clima hoje? \n")
if clima : "ensolarado"
print("Não precisa levar guarda-chuva")
else clima : "chuvoso"
print("Leve um guarda-chuva!")


 Melhorado:
print("Atribuição e Comparação")
 clima = "ensolarado"
if clima == "ensolarado": 
   print("Não precisa levar guarda-Chuva") 
elif clima: "chuvoso"
   print("Leve um guarda-chuva!")
else:
   print("Por via das dúvidas, leve o guarda-chuva!")

#  # 6. Misturando Alhos com Bugalhos
#  pontos = 50
# #print("Parabéns! Você fez " + pontos + " pontos.")

#  Corrigido:
#  print("Misturando ")









# # 7. O sistema deve dar "Excelente" para notas 9 ou 10.
# # Corrigido:
nota = 9.5
nota = float(input("Digite a sua nota: \n"))
if nota >= 9: 
   print("Excelente!")
elif nota >= 7:    
   print("Aprovado")
else nota <=7:
   print("Reprovado")



# # 8 O Contador de 1 a 5
# # Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# # Corrigido:
for i in range(1,6):
 print(f"Mostre os números {i}")

# # # Melhorado:
print("Contador de listagem")
for numeros in range(1,6):
 print(f"Liste {numeros} ")

# # 9. O Loop Eterno
# # Corrigido:
tentativas = 1
while tentativas <= 3:
  print("Tentando conectar...")  
  tentativas
tentativas +=3
print("Conexão encerrada.")

# # Melhoria:




# # 10. A Senha Teimosa
# # Corrigido:
O programa deve pedir a senha até que o usuário digite "python123"
senha = "python123"
while senha == "python123":
senha = int(input("Digite a senha secreta: "))
print("Acesso concedido!")

# # Melhoria: 
print("A senha secreta")
senha = int(input("Digite a senha secreta: \n "))
while senha == "python123":
 print("Acesso concedido!")