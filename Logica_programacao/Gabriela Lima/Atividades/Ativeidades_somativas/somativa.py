# Atividade somativa 

# Foco: print, input, operações matemáticas e f-strings
# 1.Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# def saudar_operador():
#     nome_operador = nome_operador_entry.get()
#     turno_operador = turno_operador_entry.get()

#     if nome_operador == "" :
#         messagebox.showwarning("Bem-Vindo", "Digite o seu nome: ") 
#     else:
#         messagebox.showinfo("Saudação", f"Olá {nome_operador}! ao seu turno {turno_operador}. Seja bem-vindo.")
#         messagebox.showinfo(f"Operador (a) {nome_operador} registrado (a) no Turno {turno_operador}. Boa jornada!")
# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações do Usuário")
# janela_bemvindo.geometry("600x700")

# lbl_nome_operador = tk.Label(janela_bemvindo, text= "Digite seu nome abaixo:")
# lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

# nome_operador_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
# nome_operador_entry.grid(row=0, column=1, pady=10, padx=10)

# lbl_turno_operador = tk.Label(janela_bemvindo, text= "Digite seu turno abaixo:")
# lbl_turno_operador.grid(row=1, column=0, pady=10, padx=10)

# turno_operador_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
# turno_operador_entry.grid(row=1, column=1, pady=10, padx=10)

# btn_enviar = tk.Button(janela_bemvindo, text="Enviar", command=saudar_operador)
# btn_enviar.grid(row=2, column=1, pady=10, padx=10)

# janela_bemvindo.mainloop()


# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def producao_pecas():
#     producao_pecas = int(producao_pecas_entry.get())
    
#     if producao_pecas == "" :
#         messagebox.showwarning("Digite a aprodução de peças produzidas em 1 hora:") 
#     else:
#         total_producao = producao_pecas * 8
#         messagebox.showinfo("Produçaõ em 8 horas", f"{total_producao}")

# janela_principal = tk.Tk()
# janela_principal.title("Produção de Peças")
# janela_principal.geometry("600x700")

# lbl_nome_operador = tk.Label(janela_principal, text= "Digite a quantidade de peças produzidas")
# lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

# producao_pecas_entry = tk.Entry(janela_principal, font=("Arial", 12))
# producao_pecas_entry.grid(row=0, column=1, pady=10, padx=10)

# btn_enviar = tk.Button(janela_principal, text="Enviar", command=producao_pecas)
# btn_enviar.grid(row=2, column=1, pady=10, padx=10)

# janela_principal.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.


# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def media_notas():
#     primeira_nota = primeira_nota_entry.get()
#     segunda_nota= segunda_nota_entry.get()
#     terceira_nota = terceira_nota_entry.get()

#     if primeira_nota == (1,11):
#         messagebox.showwarning("Digite a primeira nota:") 
#     else:
#         segunda_nota == (1,11)
#         messagebox.showwarning("Digite a segunda nota:") 
#         terceira_nota == (1,11)
#     messagebox.showwarning("Digite a terceira nota:") 

#     total_notas= (primeira_nota + segunda_nota + terceira_nota / 3)

#     messagebox.showinfo("", f"Média de qualidade: {media_notas:.2f}")
#     messagebox.showinfo(f"")
# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Nota de inspeção de peças")
# janela_bemvindo.geometry("600x700")

# lbl_media_nota = tk.Label(janela_bemvindo, text= "Digite a primeira nota abaixo:")
# lbl_media_nota.grid(row=0, column=0, pady=10, padx=10)

# primeiraa_nota_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
# primeira_nota_entry.grid(row=0, column=1, pady=10, padx=10)

# lbl_turno_operador = tk.Label(janela_bemvindo, text= "Digite a segunda nota abaixo:")
# lbl_turno_operador.grid(row=1, column=0, pady=10, padx=10)

# segunda_nota_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
# segunda_nota_entry.grid(row=2, column=1, pady=10, padx=10)

# lbl_inspecao_nota = tk.Label(janela_bemvindo, text= "Digite a terceira nota abaixo:")
# lbl_inspecao_nota.grid(row=3, column=0, pady=10, padx=10)

# treceira_nota_entry = tk.Entry(janela_bemvindo, font=("Arial", 12))
# terceira_nota_entry.grid(row=4, column=0, pady=10, padx=10)

# btn_enviar = tk.Button(janela_bemvindo, text="Enviar", command=media_notas)
# btn_enviar.grid(row=4, column=1, pady=11, padx=10)

# janela_bemvindo.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

import tkinter as tk
from tkinter import messagebox

def temp_motor():
    if < 40:
     
   
janela_principal = tk.Tk()
janela_principal.title("")
janela_principal.geometry("600x700")

lbl_nome_operador = tk.Label(janela_principal, text= "")
lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)

producao_pecas_entry = tk.Entry(janela_principal, font=("Arial", 12))
producao_pecas_entry.grid(row=0, column=1, pady=10, padx=10)

btn_enviar = tk.Button(janela_principal, text="Enviar", command=)
btn_enviar.grid(row=2, column=1, pady=10, padx=10)

janela_principal.mainloop()
