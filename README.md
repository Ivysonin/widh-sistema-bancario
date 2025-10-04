# 📄 Documentação – WIDH Banco Digital

## 📚 Sumário

1. [Descrição do Sistema](#-descrição-do-sistema)
2. [Estrutura do Projeto](#-estrutura-do-projeto)
3. [Requisitos do Sistema](#-requisitos-do-sistema-bancário)
4. [Funcionamento do Sistema](#-funcionamento-do-sistema)
5. [Histórico de Transações](#-histórico-de-transações)
6. [Segurança](#-segurança)
7. [Como Executar](#-como-executar)
8. [Limitações e Melhorias](#-limitações-e-melhorias-possíveis)
9. [Licença](#-licença)
10. [Desenvolvedores](#-desenvolvedores)

---

## 📌 Descrição do Sistema

Este sistema simula operações bancárias básicas, permitindo:

- Criação de contas
- Depósitos e saques
- Transferências entre contas
- Consulta de saldo e extrato
- Histórico completo de transações

A aplicação funciona via terminal e todas as operações exigem autenticação por número de conta e senha.

---

## 📁 Estrutura do Projeto

```
SistemaBancario/
│
├── docs/
│ └── fluxograma.pdf # Fluxograma geral do sistema
├── services/
│ ├── banco_service.py # Lógica do banco (gerenciamento de contas)
│ └── conta_service.py # Lógica da conta bancária individual
├── templates/
│ └── menu.py # Interface do usuário (menu e interações)
├── main.py # Arquivo principal para executar o sistema

```

---

## 📋 Requisitos do Sistema Bancário

### ✅ Requisitos Funcionais (RF)

| Código | Descrição |
|--------|-----------|
| RF01 | Permitir a criação de uma conta bancária com nome do titular e senha. |
| RF02 | Gerar automaticamente um número de conta único. |
| RF03 | Permitir depósitos de valores em contas existentes. |
| RF04 | Permitir saques, desde que o saldo disponível seja suficiente. |
| RF05 | Possibilitar transferências de valores entre contas diferentes. |
| RF06 | Autenticar o usuário por número de conta e senha antes de operações sensíveis (depósito, saque, transferência e consulta). |
| RF07 | Exibir o saldo da conta após autenticação. |
| RF08 | Registrar e manter histórico de todas as transações realizadas. |
| RF09 | Permitir a visualização do histórico de transações pelo usuário. |
| RF10 | Possibilitar o encerramento da sessão (logout). |

### 🚫 Requisitos Não Funcionais (RNF)

| Código | Descrição |
|--------|-----------|
| RNF01 | Desenvolver o sistema em Python puro, sem dependências externas. |
| RNF02 | Executar o sistema exclusivamente via terminal (linha de comando). |
| RNF03 | Garantir tempo de resposta imediato, simulando atrasos com `sleep()` apenas para melhor experiência do usuário. |
| RNF04 | Armazenar os dados apenas em memória, sem uso de arquivos ou banco de dados. |
| RNF05 | Utilizar hash SHA-256 para armazenamento seguro das senhas. |
| RNF06 | Organizar o código em módulos separados por responsabilidade. |
| RNF07 | Manter o sistema simples, de fácil leitura e compreensão, com foco didático/acadêmico. |
| RNF08 | Apresentar o histórico de transações de forma detalhada e legível ao usuário final. |

---

### ✅ Funcionalidades

- Criação de contas com número único
- Autenticação com senha segura
- Depósito e saque
- Transferência entre contas
- Consulta de saldo e extrato
- Histórico completo de operações
- Menu interativo no terminal

---

## 🧩 Funcionamento do Sistema

### Módulo: `main.py`


-  **Descrição:** Ponto de entrada da aplicação, chama a função `menu()` e permite interação do usuário via terminal.
-  **Função:**  `menu()` – exibe o menu principal e processa as opções do usuário.


#### Opções do Menu

| Opção | Ação |
|-------|------|
| 1 | Criar conta: solicita nome e senha, cadastra a conta e retorna o número da conta. |
| 2 | Depositar: solicita número da conta, senha e valor, realiza depósito se autenticado. |
| 3 | Sacar: solicita número da conta, senha e valor, realiza saque se autenticado e houver saldo. |
| 4 | Transferir: solicita conta de origem, senha, conta de destino e valor, realiza transferência se autenticado e houver saldo. |
| 5 | Consultar saldo: exibe o saldo atual da conta autenticada. |
| 6 | Extrato: exibe histórico completo de transações da conta autenticada. |
| 7 | Sair: encerra a execução do menu. |

  

-  **Fluxo:**

1. Usuário escolhe uma opção.
2. A aplicação chama métodos da classe `Banco` ou `Conta`.
3. As operações são processadas com base na autenticação por número de conta e senha.

---

### Módulo: `banco_service.py`

-  **Classe:**  `Banco` – gerencia todas as contas do sistema.

-  **Atributos:**
	
	-  `self.contas`: dicionário com contas cadastradas, usando o número da conta como chave.

-  **Métodos:**
	
	-  `gerar_numero_conta() -> str`: gera número de conta único (10000-99999).
	-  `cadastrar(titular: str, senha: str) -> str`: cria nova conta e retorna o número.
	-  `autenticar(numero_conta: str, senha: str) -> Conta | None`: valida senha e retorna o objeto `Conta`.
	-  `transferir(conta_origem: str, senha: str, conta_destino: str, valor: float) -> bool`: realiza transferência se saldo e autenticação forem válidos.

---

### Módulo: `conta_service.py`

-  **Classe:**  `Conta` – representa uma conta individual.

-  **Atributos:**
	
	-  `numero`: número da conta
	-  `titular`: nome do titular
	-  `senha_hash`: senha criptografada (SHA-256)
	-  `saldo`: saldo atual
	-  `historico`: lista de dicionários com operações realizadas

-  **Métodos:**

	-  `__init__(numero, titular, senha)`: inicializa a conta com senha criptografada.
	-  `autenticar(senha: str) -> bool`: valida a senha.
	-  `registrar(tipo: str, valor: float, destino: str | None = None)`: adiciona operação ao histórico.
	-  `depositar(valor: float) -> bool`: adiciona saldo (somente positivo).
	-  `sacar(valor: float) -> bool`: subtrai saldo se houver fundos suficientes.

---

### ⌛ Histórico de Transações

Cada operação é registrada assim:

```

{
	"tipo":  "DEPÓSITO"  |  "SAQUE"  |  "TRANSFERÊNCIA ENVIO"  |  "TRANSFERÊNCIA RECEBIDA",
	"valor":  float,
	"destino":  str  |  null
	"saldo_att":  float
}

```

---

### 🔏 Segurança

- Senhas armazenadas como hash SHA-256.
- Autenticação obrigatória para qualquer operação financeira.

---

### 💡 Como Executar

```python
# Clone o repositório
https://github.com/WyldSLA/widh-sistema-bancario.git
# Acesse a pasta do projeto
cd widh-sistema-bancario
# Execute o sistema no terminal
python3 main.py

```
---

### 🚫 Limitações e Melhorias Possíveis

- Persistência: dados apenas em memória, perdendo informações ao encerrar o sistema
- Segurança: hash SHA-256 sem salt é vulnerável a ataques de dicionário
- Interface: atualmente só via terminal, poderia ter GUI ou web
- Validação: aceitar somente dados válidos (nomes e senhas não vazios, valores positivos)

---

### 🧾 Licença

Este projeto é de uso acadêmico e está licenciado sob a [MIT License](LICENSE).

---
### 👥 Desenvolvedores
- Eduardo Ribeiro
- Ivyson Thauan
- Henrique Morais
- Wyldson Marllon