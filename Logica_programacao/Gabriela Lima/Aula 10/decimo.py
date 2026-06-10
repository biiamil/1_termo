# Tratamento de Erros
# Try e except são usados para lidar com erros de forma controlada, evitando que o programa quebre. O código dentro do bloco try é
# executado normalmente, mas sem ocorrer um erro, o controle é passado para o bloco except, onde podemos lidar com a situação de forma
# apropriada.

try:
    numero = int(input("Digite um número: \n"))
    resultado = 10 / numero 
    print("O resultado é:", resultado) 

except ValueError:
    print("Erro: Voce deve digitar um número válido.")

except ZeroDivisionError:
    print("Erro: não é possível divifir por zero")

except KeyboardInterrupt:
    print("\n Programa Interrompido")

except TypeError: 
    print("Erro: tipo de dado inválido")

except Exception as erro:
    print("Erro inesperado:", erro)

# Exercício 1:
# Escreva um programa que solicite ao usuário calcule a média de tres números. O programa deve lidar com possívei erros, como a entrada 
# de valores não numéricos ou a divisão por zero

# print ("Somativa")
# numero1 =int(input("Digite o 1° número: \n"))
# numero2 =int(input("Digite o 2° número: \n"))
# numero3 = int(input("Digite o 3° valor"))

    

# Explicação de Def: A palavra-chave "def" é usada para definir uma função em Python. Uma função é um bloco de código reutilizável
# que realiza uma tarefa específica. 
# Return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função
# foi chamada. 
# O valor retornado pode ser usado posteriormente no código.

# def nome_da_funcao(parametro1, parametro2):
# # Corpo de função (código que será executado)
# resultado = parametro1 + parametro2






# Exemplo 1:
# def saudaçao (nome, idade):
#     nome = input("Digite seu nome: \n")
#     return f"Olá, {nome}, {idade}!"
# print(saudaçao(",14"))

# Exemplo 2:
# def calcular_media(num1, num2, num3):
#     try:
#         media =(num1 + num2 + num3) /3
#         return media 
#     except TypeError:
#         return "Erro: Todos os valores devem ser números."
#     except ZeroDivisionError:
#         return "Erro: Não é possível dividir por zero"
    
# print(f"calcular_media {calcular_media (10,20,30)}")

# Exemplo 3:
def valores():
    print("Digite tres valores:")
    a = int(input("Digite o primeiro valor: \n"))
    b = int(input("Digite o segundo valor: \n"))
    c = int(input("Digite o terceiro valor: \n"))
    return a,b,c
print(f"O maior valor é: {max (valores())}")

# Exemplo 4:
# Calcule o dobro de um número fornecido pelo usuário, tratando erros da entrada inválida.
def calcular_dobro():
    try: 
        valor_digitado = int(input("Digite o valor que deseja: )"))
        total_dobro = valor_digitado * 2 
        return total_dobro

    except ValueError:
        print("Digite um número válido")
print(f"O calculo é: {calcular_dobro()}")