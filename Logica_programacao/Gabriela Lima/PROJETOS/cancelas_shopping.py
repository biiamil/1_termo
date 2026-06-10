# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

print ("Seja Bm-Vindo ao Shopping Center!")

nome_veiculo = input("Digite o nome do seu veiculo: \n")
placa_veiculo = int(input("Digite o numero da placa do seu veiculo: \n "))

print("R$12,00 por hora")

tag = input("O veiculo possui TAG? ")
if tag == "Sim":
    print=("Acesso Liberado!")
elif tag == "Não":
    print = ("Acesso Negado!")
else: 
    print("Invalido!")

horario_entrada = float(input("Que horas chegou ao estacionamento? \n"))
permanencia = input("Qual foi o tempo de permanencia no predio? \n")


horario_saida = float(input("Qual foi o horario de saida do estacionamento? \n"))

print ("Valor a ser cobrado")
print("")
valor = horario_entrada - horario_saida 

