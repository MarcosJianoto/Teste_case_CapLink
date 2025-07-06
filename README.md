# 📝 Projeto: Automação de Processos e Geração de Relatórios

Este projeto simula uma automação que consome dados da API JSONPlaceholder, processa informações, gera um relatório em Excel e permite o envio por e-mail. Ideal para testes técnicos ou aprendizado sobre automação, APIs e manipulação de dados em Python.

<<<<<<< HEAD
---

## 🚀 Funcionalidades

- 🔗 Consome endpoints da API JSONPlaceholder (`/users` e `/posts`)
- 📊 Agrupa os posts por usuário
- ✍️ Calcula a média de caracteres dos posts de cada usuário
- 📁 Gera e salva um arquivo `.xlsx` com os dados
- 📧 Envia o relatório por e-mail (via SMTP Gmail)
- 🗑️ Permite deletar o arquivo gerado após o uso

---

## 📂 Estrutura do Projeto

```
=======


🚀 Funcionalidades
🔗 Consome endpoints da API JSONPlaceholder (/users e /posts)
📊 Agrupa os posts por usuário
✍️ Calcula a média de caracteres dos posts de cada usuário
📁 Gera e salva um arquivo .xlsx com os dados
📧 Envia o relatório por e-mail (via SMTP Gmail)
🗑️ Permite deletar o arquivo gerado após o uso



📂 Estrutura do Projeto
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
CapLink/
├── api.py                      # Consumo da API
├── main.py                     # Execução principal
├── processor.py                # Lógica de agrupamento e cálculo
├── report.py                   # Geração e remoção do relatório
├── send_email/
│   ├── send_email.py           # Envio de e-mail
│   └── variables_necessary_model.py  # Variáveis de ambiente (modelo)
└── README.md
```

<<<<<<< HEAD
---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

```bash
=======


⚙️ Como rodar o projeto

Clone o repositório
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
git clone https://github.com/seu-usuario/CapLink.git
cd CapLink
```

<<<<<<< HEAD
### 2. (Opcional) Crie um ambiente virtual

```bash
=======


🧱 Crie um ambiente virtual (opcional)
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
python -m venv .venv
# Ativar:
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

<<<<<<< HEAD
### 3. Instale as dependências

```bash
=======


📦 Instale as dependências
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
pip install -r requirements.txt
```

<<<<<<< HEAD
### 4. Configure seu e-mail

Faça uma cópia do arquivo:

```bash
=======


✉️ Configure seu e-mail
Faça uma cópia do arquivo variables_necessary_model.py:
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
cp send_email/variables_necessary_model.py send_email/variables_necessary.py
```

<<<<<<< HEAD
Edite os dados:

- E-mail remetente e destinatário
- Senha de aplicativo do Gmail
- Pasta onde os arquivos serão salvos

---

## ▶️ Execute o projeto

```bash
=======


✏️ Edite as informações com seus dados:
E-mail remetente e destinatário
Senha de aplicativo do Gmail
Pasta onde os arquivos serão salvos



▶️ Execute o projeto
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
python main.py
```

<<<<<<< HEAD
---

## 📧 Sobre o envio de e-mails

O envio é feito com `smtplib` via `SMTP_SSL` do Gmail.

> ⚠️ É necessário gerar uma senha de aplicativo no Gmail.

Se o e-mail não for enviado, será exibida uma mensagem de erro.

---

## 📌 Exemplo de saída

```
=======


📧 Sobre o envio de e-mails
O envio é feito com smtplib via SMTP_SSL do Gmail.
Atenção: é necessário gerar uma senha de aplicativo no Gmail.
Caso o e-mail não seja enviado, será exibida uma mensagem de erro.



📌 Exemplo de saída
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
Relatório salvo como: ./suapasta/report_05072025_154020.xlsx
Gostaria de enviar o relatório via e-mail? [ Y/N ] Y
E-mail enviado com sucesso!
Gostaria de apagar o arquivo? [ Y/N ] Y
arquivo: ./suapasta/report_05072025_154020.xlsx removido
```

<<<<<<< HEAD
---

## 📝 Observações

- O programa utiliza dados públicos de [JSONPlaceholder](https://jsonplaceholder.typicode.com).
- Você poderá optar por enviar o relatório por e-mail e também excluí-lo após o uso.

---

## 🧰 Tecnologias Utilizadas

- Python 3.11+
- requests
- pandas
- pathlib
- smtplib / email.message
- mimetypes
- JSONPlaceholder (API fake)

---

## ✅ Boas Práticas aplicadas

- Separação de responsabilidades por arquivos
- Organização em módulos reutilizáveis
- Uso de `pathlib` para manipulação de arquivos/pastas
- `try/except` para tratamento de exceções
- Arquivo `.gitignore` para proteger credenciais
=======


📝 Observações
O programa irá gerar um relatório com base em dados públicos de JSONPlaceholder.
Após gerar o relatório, você poderá optar por enviá-lo por e-mail.
Também poderá decidir se deseja excluir o arquivo salvo.



🧰 Tecnologias Utilizadas
Python 3.11+
Requests
Pandas
Pathlib
smtplib / email.message
mimetypes
JSONPlaceholder (API fake)



✅ Boas Práticas aplicadas
Separação de responsabilidades por arquivos
Organização em módulos reutilizáveis
Uso de Pathlib para manipulação de arquivos/pastas
try/except para tratamento de exceções
Arquivo .gitignore para proteger credenciais
>>>>>>> 40bea4f908dca7092ee6a44a5aa4ee3b21531797
