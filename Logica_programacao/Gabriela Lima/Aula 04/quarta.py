1. O Laço 'for' (Repetição determinada)
Use 'for' quando voce sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
Exemplo: Relatório de Produção Diária 
Imagine que voce tem uma meta de produzir 5 lotes e quer numerar cada um:
 Exemplo 1 
for lote in range(1,6):
    print(f"Processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
print("Produção do dia finalizada!")

# Exemplo 3 
for b in range (10):
    print(f"Quantidade total {b} foi...")
    print("Quantidade total verificada. [OK]")
print("Fianlizado!")

# Exemplo 3
# Imagine o seguinte cenário, iremos produzir 20 discos de vinil. 
for vinil in range (21):
    print(f"Quantidade total {vinil}, diária")
print("As produções dos discos de Vinil foram finalizadas!")

 Exemplo 4
pecas = ["Engrenagem" , "Eixo" , "Rolamento" , "Parafuso" , "Martelo" , "Prego" , "Chave de fenda" , "Alicate"]
itempecas = ["Cilindrica" , "duplo" , "conica" , "Prego" , "Orelha" "redondo" , "phillips" , "universal"]

for item in pecas: 
    print(f"Item em estoque: {item} e {itempecas}") 
   
   
Exemplo 5 
Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção voce deseja e a partir da seleção ele listar os produtos. 

print(" Menu de livros e filmes")
print("1 - Livros")
print("2 - Filmes")
opcao = int(input("Escolha entre as opções que voce mais gosta" )) 

if opcao == 1:
    livros = ["romance", "drama" , "terror" , "Fábula"]
    for liv in livros:
        print(f"Os generos são esses {liv}")
elif opcao == 2:
    filmes = ["amor" , "suspense" , "Ação" , "Comédia"]
    for fil in filmes:
        print(f"Os livros são esses {fil}")
else:
 print("Má Escolha!")

Exercício 1 
1. Contador de Produção (for)
Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº x processada com sucesso".
 No final, exiba "Ciclo de produção concluído"
for ciclo in range (1,11):
    print(f"Peça nº{ciclo} processada com sucesso")
print("Ciclo de Produção concluída")

Exercício 2
Imagine uma produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas,
5 mangas, 10 melancias e 13 abacaxis

No fim da produção gostaria de ter um total das produções

print("Feirópolis")
print("Bananas")
for banana in range (1,11):
    print(f"A quantidade de {banana} são")
for man in range (1, 6):
    print(f"A quantidade de {man} são")
for melan in range (1,11):
    print(f"A qunatidade de {melan} são")
for abba in range (1,14):
    print(f"A quantidade de {abba} são")

total = banana + man + melan + abba


# Exercício 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print("Tabuada")
tab = int(input("Digite qual tabuada "))
for numero in range (1,11):
    resultado = tab * numero 
    print(f"{tab} X {numero} = {resultado}")
    