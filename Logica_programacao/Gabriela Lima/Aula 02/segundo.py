# Funções são blocos de código reutilizavéis. 
# O "f" no Python, usado antes das aspas de uma string (como f"texto {váriavel}"), indica que se trata de uma f-string (ou formatted string literal). Ele informa ao Python que a string contém expressões entre chaves {} que devem ser avaliados em tempo de execução e substituídas pelos seus valores reais.

def saudacao (nome):
    return f"Olá, {nome}!"
mensagem = saudacao("Gabriela")
print(mensagem)
 
def boas_vindas(nome, cargo):
    print(f"Olá, {nome}! Voce é o novo {cargo}.")

    boas_vindas("Jacó" , " Desenvolvedor")
    boas_vindas("Julia" , "estudante")
    boas_vindas("Bruno" , "professor")

# Corversões 
nome = input("Seu nome:")
idade = int(input("Sua idade:")) # Coverte texto para inteiro
print(f"{nome} tem {idade} anos. ")
