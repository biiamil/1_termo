# 🖥️ Curso: Sistemas Operacionais (S.O.) na Prática

Este material serve como guia de conteúdo para as aulas de operação, gerenciamento e segurança em sistemas operacionais Windows e Linux.

---

## 🛡️ 1. Segurança Cibernética no Sistema Operacional

A segurança cibernética estuda como proteger o sistema, os arquivos e as informações contra acessos não autorizados ou ataques de vírus.

*   **Princípio dos Privilégios Mínimos:** Cada usuário deve ter acesso apenas ao que é estritamente necessário para trabalhar. Isso evita que um vírus infecte todo o computador.
*   **Controle de Acessos:** Uso de ferramentas como autenticação forte (senhas robustas, biometria) e atualizações automáticas de segurança (*patches*).

---

## 🗂️ 2. Gerenciando Variáveis, Pastas e Usuários no Windows

O Windows permite organizar quem usa o computador e onde as informações ficam guardadas de forma visual ou técnica.

*   **Usuários e Grupos:** Separação entre contas de *Administrador* (pode alterar tudo) e *Usuário Padrão* (não pode instalar programas que afetem o sistema).
*   **Pastas e Permissões:** Controle de quem pode Ler, Escrever ou Modificar um arquivo específico.
*   **Variáveis de Ambiente:** Valores guardados na memória do sistema que os programas usam para se localizar (como a variável `PATH`, que aponta onde estão os executáveis do computador).

---

## 🐧 3. Distribuições Linux

O Linux não é um sistema único, mas sim um "núcleo" (kernel). Diferentes empresas e comunidades criam versões completas baseadas nele, chamadas de **Distribuições (ou Distros)**.

*   **Ubuntu / Mint:** Focados em facilidade de uso, ideais para iniciantes e computadores de uso diário.
*   **Debian / CentOS:** Extremamente estáveis, muito utilizados para rodar servidores de internet de grandes empresas.
*   **Kali Linux:** Uma distribuição voltada especificamente para profissionais de segurança realizarem testes de invasão e correção de falhas.

---

## 💡 4. Indicação de Sistemas Operacionais

Não existe um sistema melhor para tudo. Cada um atende a uma necessidade específica:

*   **Windows:** Indicado para o mercado corporativo tradicional, ferramentas de escritório (Pacote Office) e o público de jogos (Games).
*   **Linux:** Indicado para servidores de internet, desenvolvimento de software e computadores antigos que precisam de um sistema mais leve.
*   **macOS:** Indicado para profissionais de design, edição de vídeo, áudio e desenvolvimento de aplicativos para iPhone.

---

## ⌨️ 5. Operação de Sistemas Operacionais via CLI (Linha de Comando)

A **CLI (Command Line Interface)** é a interface de texto onde você controla o computador digitando ordens, sem usar o mouse. É a ferramenta favorita dos administradores pela rapidez e poder de automação.

### 🐧 Comandos Essenciais no Linux (Terminal)
*   `ls`: Lista os arquivos e pastas do diretório atual.
*   `cd`: Entra ou navega entre as pastas do sistema.
*   `mkdir`: Cria uma nova pasta.
*   `rm`: Remove ou apaga um arquivo.

---

## 🪟 6. Operação do Windows via CLI (Prompt de Comando / PowerShell)

O Windows possui o CMD tradicional e o PowerShell (mais avançado) para administração do sistema por texto.

### 💻 Comandos Essenciais no Windows (CMD)
*   `dir`: Mostra a lista de arquivos e pastas na tela (equivalente ao `ls`).
*   `cd`: Muda de pasta (igual ao Linux).
*   `mkdir` ou `md`: Cria uma nova pasta.
*   `del`: Apaga um ou mais arquivos.
*   `ipconfig`: Mostra as informações da sua conexão de internet (como o endereço IP do computador).
