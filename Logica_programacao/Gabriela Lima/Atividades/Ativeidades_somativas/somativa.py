Atividade somativa 

Foco: print, input, operações matemáticas e f-strings
1.Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
"Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

import tkinter as tk
from tkinter import messagebox

def saudar_operador():
    nome_operador = nome_operador_entry.get()
    turno_operador = turno_operador_entry.get()

    if nome_operador == "" :
        messagebox.showwarning("Bem-Vindo", "Digite o seu nome: ") 
    else:
        messagebox.showinfo("Saudação", f"Olá {nome_operador}! ao seu turno {turno_operador}. Seja bem-vindo.")
        messagebox.showinfo(f"Operador (a) {nome_operador} registrado (a) no Turno {turno_operador}. Boa jornada!")
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações do Usuário")
janela_bemvindo.geometry("600x700")

lbl_nome_operador = tk.Label(janela_bemvindo, text= "Digite seu nome abaixo:")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

nome_operador_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
nome_operador_entry.grid(row=0, column=1, pady=10, padx=10)

lbl_turno_operador = tk.Label(janela_bemvindo, text= "Digite seu turno abaixo:")
lbl_turno_operador.grid(row=1, column=0, pady=10, padx=10)

turno_operador_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
turno_operador_entry.grid(row=1, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_bemvindo, text="Enviar", command=saudar_operador)
btn_enviar.grid(row=2, column=1, pady=10, padx=10)

janela_bemvindo.mainloop()


2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
exiba quantas peças serão produzidas em um turno de 8 horas.

import tkinter as tk
from tkinter import messagebox

def producao_pecas():
    producao_pecas = int(producao_pecas_entry.get())
    
    if producao_pecas == "" :
        messagebox.showwarning("Digite a aprodução de peças produzidas em 1 hora:") 
    else:
        total_producao = producao_pecas * 8
        messagebox.showinfo("Produçaõ em 8 horas", f"{total_producao}")

janela_principal = tk.Tk()
janela_principal.title("Produção de Peças")
janela_principal.geometry("600x700")

lbl_nome_operador = tk.Label(janela_principal, text= "Digite a quantidade de peças produzidas")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

producao_pecas_entry = tk.Entry(janela_principal, font=("Arial", 12))
producao_pecas_entry.grid(row=0, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_principal, text="Enviar", command=producao_pecas)
btn_enviar.grid(row=2, column=1, pady=10, padx=10)

janela_principal.mainloop()

3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
≈ 14.5 PSI) e exiba com duas casas decimais.


4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
aritmética simples delas.

import tkinter as tk
from tkinter import messagebox

def media_notas():
    primeira_nota = primeira_nota_entry.get()
    segunda_nota= segunda_nota_entry.get()
    terceira_nota = terceira_nota_entry.get()

    if primeira_nota == (1,11):
        messagebox.showwarning("Digite a primeira nota:") 
    else:
        segunda_nota == (1,11)
        messagebox.showwarning("Digite a segunda nota:") 
        terceira_nota == (1,11)
    messagebox.showwarning("Digite a terceira nota:") 

    total_notas= (primeira_nota + segunda_nota + terceira_nota / 3)

    messagebox.showinfo("", f"Média de qualidade: {media_notas:.2f}")
    messagebox.showinfo(f"")
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Nota de inspeção de peças")
janela_bemvindo.geometry("600x700")

lbl_media_nota = tk.Label(janela_bemvindo, text= "Digite a primeira nota abaixo:")
lbl_media_nota.grid(row=0, column=0, pady=10, padx=10)

primeiraa_nota_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
primeira_nota_entry.grid(row=0, column=1, pady=10, padx=10)

lbl_turno_operador = tk.Label(janela_bemvindo, text= "Digite a segunda nota abaixo:")
lbl_turno_operador.grid(row=1, column=0, pady=10, padx=10)

segunda_nota_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
segunda_nota_entry.grid(row=2, column=1, pady=10, padx=10)

lbl_inspecao_nota = tk.Label(janela_bemvindo, text= "Digite a terceira nota abaixo:")
lbl_inspecao_nota.grid(row=3, column=0, pady=10, padx=10)

treceira_nota_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
terceira_nota_entry.grid(row=4, column=0, pady=10, padx=10)

btn_enviar = tk.Button(janela_bemvindo, text="Enviar", command=media_notas)
btn_enviar.grid(row=4, column=1, pady=11, padx=10)

janela_bemvindo.mainloop()

5. Termostato Inteligente: Peça a temperatura de um motor.
Abaixo de 40°C: "Baixa carga".
Entre 40°C e 70°C: "Normal".
Acima de 70°C: "ALERTA: Resfriamento Ativado!".

import tkinter as tk
from tkinter import messagebox

def temp_motor():

    temperatura_motor = int(informacao_temperatura_entry.get())

    if temperatura_motor < 40:
        messagebox.showwarning("Atenção", "Baixo carga") 
    elif temperatura_motor > 40 and temperatura_motor > 70:
        messagebox.showwarning("Boa!", "Normal") 
    else:
        messagebox.showwarning("Atenção!", "ALERTA: Resfriamento Ativado!") 


janela_principal = tk.Tk()
janela_principal.title("Temperatura do Motor")
janela_principal.geometry("600x700")

lbl_nome_operador = tk.Label(janela_principal, text= "Digite a temperatura do motor e verifiacaremos!")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

informacao_temperatura_entry = tk.Entry(janela_principal, font=("Arial", 12))
informacao_temperatura_entry.grid(row=0, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_principal, text="Enviar", command=temp_motor)
btn_enviar.grid(row=2, column=1, pady=10, padx=10)

janela_principal.mainloop()

6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

import tkinter as tk
from tkinter import messagebox

def classic_lotes ():
    
    classificador_lotes = informacao_lotes_entry.get()

    if classificador_lotes == ("A"):
        messagebox.showwarning("Digite o código", "Alimentos") 
    elif classificador_lotes == ("E"):
        messagebox.showwarning("Digite o código", "Eletrônicos") 
    else:
        messagebox.showwarning("Atenção", "Desconhecido") 
    
janela_principal = tk.Tk()
janela_principal.title("Classificação Lotes")
janela_principal.geometry("600x700")

lbl_nome_operador = tk.Label(janela_principal, text= "Digite o código e verifiacaremos!")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

informacao_lotes_entry = tk.Entry(janela_principal, font=("Arial", 12))
informacao_lotes_entry.grid(row=0, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_principal, text="Enviar", command=classic_lotes)
btn_enviar.grid(row=2, column=1, pady=10, padx=10)

janela_principal.mainloop()

7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
iniciar.

import tkinter as tk
from tkinter import messagebox, ttk

def sensor_porta ():
    seguranca_opera= porta_sensores_entry.get()
    botao_emergencia = informacao_emergencia_entry.get()

    if seguranca_opera == ("fechado"):
        messagebox.showwarning("A Máquina não pode iniciar", "fechado")
    
    elif botao_emergencia == ("desligado"):
        messagebox.showwarning("Alerta!", "O modo emergencia está ativado")
    else:
        messagebox.showwarning("Concluído!")

janela_principal = tk.Tk()
janela_principal.title("Segurança de Operação")
janela_principal.geometry("600x700")

lbl_nome_operador = tk.Label(janela_principal, text= "Sensor ativado")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

lbl_nome_operador = tk.Label(janela_principal, text= "Modo Emergencia")
lbl_nome_operador.grid(row=2, column=0, pady=10, padx=10)

porta_sensores_entry = tk.ttk.Combobox(janela_principal, values=["ABERTO", "FECHADO"])
porta_sensores_entry.grid(row=0, column=1, pady=10, padx=10)

informacao_emergencia_entry = tk.ttk.Combobox(janela_principal, values=["LIGADO", "DESLIGADO"])
informacao_emergencia_entry.grid(row=2, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_principal, text="Enviar", command=sensor_porta)
btn_enviar.grid(row=3, column=0, pady=10, padx=10)

janela_principal.mainloop()

8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
"Processo Otimizado".

import tkinter as tk
from tkinter import messagebox

def verificar():
    total = int(tudo_total.get())
    defeituosas = int(pecas_defeituosas.get())

    porcentagem = (defeituosas / total) * 100

    if porcentagem > 5:
        resultado = "Revisar Processo"
    else:
        resultado = "Processo Otimizado"

    messagebox.showinfo("Resultado", resultado)

janela = tk.Tk()
janela.title("Cálculo de Descarte")
janela.geometry("300x200")

tk.Label(janela, text="Total de peças").pack()
tudo_total = tk.Entry(janela)
tudo_total.pack()

tk.Label(janela, text="Peças defeituosas").pack()
pecas_defeituosas = tk.Entry(janela)
pecas_defeituosas.pack()

tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

janela.mainloop()

9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
diga se está dentro da tolerância, acima ou abaixo.

import tkinter as tk
from tkinter import messagebox

def vali_media ():

    pecas_medidas= float(medidas_pecas.get())

    if pecas_medidas <9.8 and pecas_medidas < 10.2:
        messagebox.showwarning("Aviso!", "A peça está dentro da tolerancia") 
    elif pecas_medidas <9.8 :
        messagebox.showwarning("Aviso!", "A peça está abaixo da tolerancia") 
    else:
        messagebox.showwarning("Aviso", "A peça está acima da tolerancia") 

janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
janela_principal.geometry("600x700")

lbl_nome_operador = tk.Label(janela_principal, text= "Digite a medida da peça")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

pecas_medidas_entry = tk.Entry(janela_principal, font=("Arial", 12))
pecas_medidas_entry.grid(row=0, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_principal, text="Enviar", command=vali_media)
btn_enviar.grid(row=2, column=1, pady=10, padx=10)

janela_principal.mainloop()

10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

import tkinter as tk
from tkinter import messagebox

def iniciar_prensa():
    contagem = ""

    for i in range(10, 0, -1):
        contagem += str(i) + "\n"

    contagem += "Prensa Ativada!"

    messagebox.showinfo("Contagem Regressiva", contagem)

janela = tk.Tk()
janela.title("Setup da Prensa")
janela.geometry("300x150")

tk.Button(
    janela,
    text="Iniciar Contagem",
    command=iniciar_prensa
).pack(pady=10)

tk.Button(
    janela,
    text="Fechar Janela",
    command=janela.destroy
).pack(pady=10)

janela.mainloop()