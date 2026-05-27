# Clean Code - Aula 7 
# Para que usar?
# Como usar?
# print("Clean Code - Aula 7")
# aula = 7 
# print(f"Estamos na aula {aula} de Clean Code")


# print("Perfil de Gamer - Seja Bem-Vindo Jogador")
# nome_jogador = input("Qual é o Nick do Jogador?")
# nivel_jogador =  input("Qual o nivel do jogador?")
# print(f"O jogador {nome_jogador} esta no nivel {nivel_jogador} e pronto para a partida!")


# print("Calculadora de Mesada")
# valor_semana = float(input("Qual é seu valor que recebeu?"))
# total_mes = valor_semana * 4 
# print(f"Sua mesada no final do mes será de... {total_mes}")

# Manipulação de Arquivos e Textos 
# manipular_texto = " Python é Muito Legal!"
# print(manipular_texto.strip().upper()) # "PYTHON"
# print(manipular_texto.strip().lower()) # "python"
# print(manipular_texto.strip().startswith("A")) # "Começar com Letra Inicial

# print(manipular_texto.strip().capitalize()) # "Letras Inial"
# print(manipular_texto.strip().title ()) # "Título"
# print(manipular_texto.strip().replace ()) 
# ("", "_")  # "Preencher vazios"
# print(manipular_texto.strip().split()) # "Separar palavras"

# Exercicio 1 
# Crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba a frase 
# com  as seguintes tranformações:
# - Deixe o texto em letras minúsculas 
# frase_usuario = input("Digite uma frase:")
# print(frase_usuario.strip().lower())

# # Manipulador de Arquivos:

# # Escrevendo
# with open ("notas.txt", "w", encoding="utf-8") as texto: 
#     texto.write("Estudar Python hoje!")
#     texto.write("\nLer sobre Clean Code")
#     texto.write("\nEstamos evoluindo.")

# # Lendo 
# with open ("notas.txt", "r", encoding="utf-g") as texto: 
#     conteudo = texto.read()
#     print(conteudo)

# # Exemplo 1:
# # Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes
# #  a palavra "Python" aparece no arquivo. Exiba o resultado para o usuario.
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count ("Python")
#     contagem = conteudo.upper().count ("PYTHON")

#     print (f"A contagem de palavras {contagem} é de...")

# Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# Criar pastas
# os.mkdir("Amil")
# Criar arquivos

# Renomear pastas
# os.rename("Amil", "Minha_Pasta")

# Apagar pastas
# os.rmdir("Gabi")
os.remove("notas.txt") #Excluir arquivos

Complemento de comandos uteis
