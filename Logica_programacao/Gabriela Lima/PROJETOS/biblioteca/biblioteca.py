import tkinter as tk
from tkinter import messagebox


def validar_emprestimo():
    try:
        nome = entry_nome.get().strip()
        categoria_livro = categoria_var.get()
        tipo_usuario = usuario_var.get()
        dias = int(entry_dias.get())

        # Estrutura de repetição para validar campos
        campos = [nome, categoria_livro, tipo_usuario]

        for campo in campos:
            if campo == "":
                messagebox.showerror(
                    "Erro",
                    "Preencha todos os campos!"
                )
                return

        # Restrição de categoria
        if categoria_livro.lower() == "raros" and tipo_usuario == "Comunidade Geral":
            resultado = (
                f"Empréstimo NEGADO!\n\n"
                f"Livros da categoria 'Raros' só podem ser "
                f"emprestados para Alunos."
            )

        else:
            taxa = 0

            # Limites por perfil
            if tipo_usuario == "Aluno":
                limite = 14
            else:
                limite = 7

            # Verifica dias adicionais
            if dias > limite:
                dias_extras = dias - limite
                taxa = dias_extras * 5

                resultado = (
                    f"Empréstimo APROVADO!\n\n"
                    f"Usuário: {nome}\n"
                    f"Perfil: {tipo_usuario}\n"
                    f"Dias solicitados: {dias}\n"
                    f"Dias excedentes: {dias_extras}\n"
                    f"Taxa de segurança: R$ {taxa:.2f}"
                )
            else:
                resultado = (
                    f"Empréstimo APROVADO!\n\n"
                    f"Usuário: {nome}\n"
                    f"Perfil: {tipo_usuario}\n"
                    f"Dias solicitados: {dias}\n"
                    f"Taxa: Isento"
                )

        lbl_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um número válido para os dias."
        )


# Janela principal
janela = tk.Tk()
janela.title("Biblioteca Digital")
janela.geometry("500x450")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Sistema de Empréstimo - Biblioteca Digital",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

# Nome
tk.Label(janela, text="Nome do Usuário:").pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

# Tipo de usuário
tk.Label(janela, text="Tipo de Usuário:").pack()

usuario_var = tk.StringVar()

tk.Radiobutton(
    janela,
    text="Aluno",
    variable=usuario_var,
    value="Aluno"
).pack()

tk.Radiobutton(
    janela,
    text="Comunidade Geral",
    variable=usuario_var,
    value="Comunidade Geral"
).pack()

# Categoria do livro
tk.Label(janela, text="Categoria do Livro:").pack(pady=5)

categoria_var = tk.StringVar()
categoria_var.set("Comum")

opcoes = ["Comum", "Raros"]

menu = tk.OptionMenu(
    janela,
    categoria_var,
    *opcoes
)
menu.pack()

# Dias
tk.Label(janela, text="Quantidade de Dias:").pack(pady=5)

entry_dias = tk.Entry(janela)
entry_dias.pack()

# Botão
btn = tk.Button(
    janela,
    text="Validar Empréstimo",
    command=validar_emprestimo,
    bg="green",
    fg="white",
    font=("Arial", 10, "bold")
)
btn.pack(pady=15)

# Resultado
lbl_resultado = tk.Label(
    janela,
    text="",
    justify="left",
    font=("Arial", 10)
)
lbl_resultado.pack(pady=10)

janela.mainloop()