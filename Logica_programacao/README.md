# 🐍 Curso: Lógica de Programação com Python

Este guia prático reúne os conceitos fundamentais para quem está começando a dar os primeiros passos na programação usando a linguagem Python e a plataforma GitHub.

---

## 🚀 1. O que é o Python e o GitHub?

*   **Python:** É uma linguagem de programação muito popular, conhecida por ser simples, fácil de ler e direta, parecida com o inglês.
*   **GitHub:** É um site onde os programadores guardam, organizam e compartilham os códigos de seus projetos na nuvem, funcionando como uma rede social de códigos.

---

## 🗣️ 2. Entrada e Saída de Dados: `print` e `input`

São os comandos que usamos para o computador conversar com o usuário.

*   **`print()` (Saída):** Exibe um texto ou resultado na tela do computador.
*   **`input()` (Entrada):** Abre uma caixa para o usuário digitar alguma informação e envia esse dado para o programa.

```python
nome = input("Digite o seu nome: ")
print("Olá, bem-vindo ao curso de programação!")
```

---

## ⚖️ 3. Tomada de Decisões: `if`, `elif` e `else`

Permitem que o programa faça escolhas baseadas em condições, igual às decisões que tomamos no dia a dia.

*   **`if` (Se):** O ponto de partida. Executa um bloco de código se a condição for verdadeira.
*   **`elif` (Senão Se):** Testa uma nova opção caso a condição anterior tenha sido falsa.
*   **`else` (Senão):** O caminho padrão. É executado se nenhuma das condições anteriores der certo.

```python
idade = 18

if idades > 18:
    print("Você é maior de idade.")
elif idade == 18:
    print("Você acabou de completar 18 anos!")
else:
    print("Você é menor de idade.")
```

---

## 🔄 4. Repetição Controlada: O Comando `for`

Usado quando precisamos que o computador repita uma mesma tarefa várias vezes seguidas de forma automática.

*   **Como funciona:** Ele percorre uma lista ou uma sequência de números definida pelo comando `range()`.

```python
# Vai repetir o comando print 5 vezes, contando do 0 até o 4
for contador in range(5):
    print("Contagem:", contador)
```

---

## 📦 5. Fábrica de Códigos: Funções

Uma **função** é um bloco de código que recebe um nome e serve para realizar uma tarefa específica. Ela evita que você precise digitar o mesmo código várias vezes.

*   **Como criar:** Usamos a palavra-chave `def` seguida do nome que queremos dar para a nossa função.

```python
# Criando a função
def saudar_usuario(nome_digitado):
    print("Seja muito bem-vindo,", nome_digitado)

# Usando (chamando) a função no programa
saudar_usuario("Carlos")
```
