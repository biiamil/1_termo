# Revisão de conteúdo:
# print = "Função de saída de dados para o console"
# input = "Função de entrada de dados do usuário via teclado "

# if = "Estrutura de decisão para executar código condicionalmente"
# elif = "Combinação de else + if para verificar múltiplas condições"
# else = "Parte opcional de um if que executa código quando a condição do if é falsa"

# for = "Laço de repetição para iterar sobre uma sequencia de elementos"
# while = "Laço de repetição para executar código enquanto uma condição for verdadeira"

# Operadores matemáticos: + - * / // % **
# OPeradores de comparação: == != >, <, >=, <=
# variavel = "Exemplo de variavel para armazenar dados"
# print(variavel)

# Exemplo 1: com print e input
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}! Bem-vindo a aula de Python para Desenvolvimento de Sistemas")

# Exemplo 2: com if, elif, else 
# nota = float(input("Digite a nota do aluno: "))
# if nota >= 7: 
#     print("Aluno Aprovado!")
# elif nota >= 5: 
#     print("Aluno em recuperação.")
# else: 
#     print("Aluno Reprovado.")

# Exemplo 3: com for
# materiais = ["metal","plastico","vidro"]
# for material in materiais:
#     print(f"Processando material: {material}.")
#     print(f"Material {material} processado com sucesso!")
# print("Fim do processamento de materiais.")

# 2. O Laço While (Repetições Inderteminadas)
# Use o while quando voce não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergencia). 
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)
# Repete enquanto a temperatura estiver segura
# import time 
# temperatura = 25
# while temperatura <40:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura +=3 # Simulado o aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite.Desligando motor...")

# Lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]
# for temp in leituras:
#     while temp > 100:
#         print(f"CRITICO: {temp}°c detectado! Acionado parada de emergencia.")
#         break  # O loop para aqui e NAO le os proximos valores (85 e 80)
#     print (f"Temperatura está em {temp}°c. Operação normal.")
# print("Sistema desligado. Agardando manutenção")

# # Produçãode peças com controle de material usando continue
# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando paradescarte...")
#         continue # Pula o restante do código abaixo e vai paraa proxima peça
# # Este código só roda se a peça for de metal 
#  print(f"processando peça de {peca}. Furando e polindo...")
# print("Fim do lote de produção")

# Execicio 1 
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5)

# for sensor in range(1,11):
#     if sensor == 5: 
#         print(f"Sensor n°{sensor} com falha")
#     print(f"Sensor {sensor} sem falha")
#     continue
# print("FIM!")

# Exercício 2 
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor.
# Use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela.)

# semaforo = ["verde", "amarelo", "vermelho"]
# for cor in semaforo: 
#     if cor == "amarelo"
#     print(f"AVISO: Luz amarela {cor} está com defeito")
#     continue # Pula a cor amela 
# print (f"Semaforo na cor {cor}. Parando por 3 segundos...")
# time.sleep(3)
# # Simula a pausa para cada cor 
# print("Fim do ciclo do semaforo")

# Exercício 3 - Soma de Cargas de Energia (for)


# consumo = 0
# for maq in range(1,6):
#     maquina = float(input(f"Digite o valor que deseja da {maq} n°"))
#     totalconsumo += consumo # Acumula o cosumo total
# print(f"O consumo total da fabrica é de {totalconsumo} kwh")

# Exercício 4 - Identificar de Peças Defeituasas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]. O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais. 
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

# pecas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for medidas in pecas:
#     if medidas >= 50.0:
#         print (f"Peça com medida {medidas}mm: Aprovada")
#     else:
#         print(f"peça com medida {medidas}mm: Rejeitado")

# Exercício 5 - Uma balança industrial esta pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações. 
# Crie um programa que peça ao usuario o peso de cada saco (via input dentro do loop) e, para cada um, informe se ele está "Dentro do limite"
# (entre 48kg e 52kg) ou "Fora do limite". No final, exiba quantos sacos estão dentro do limite.
# 
for sacos in range (1,7):
     peso = float(input(f"Digite o valor dos {sacos}"))
if 48 <= peso <= 52:
    print(f"Saco {sacos} com peso {peso}kg: Dentro do limite")
    sacos_d1 += 1 # Contra os sacos dentro do limite
else: 
    print(f"Saco {sacos} com peso {peso}kg: Fora do Limite")
print(f"Quantidade de sacos dentro do limite: {sacos_d1}")