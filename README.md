#  🪙 Sistema Bancário Simples

Este é um projeto de um **sistema bancário básico** desenvolvido em Python. Ele oferece funcionalidades como saques, depósitos, criação de usuários e contas, listagem de contas, e exibição de extratos, tudo acessível por meio de um menu interativo no terminal.

## 🛠️ Funcionalidades
- **Saque:** Permite realizar saques, respeitando saldo, limite de saque e número máximo de saques diários.
- **Depósito:** Realiza depósitos com validação de valores.
- **Extrato:** Exibe o histórico de movimentações financeiras e o saldo atual.
- **Criação de Usuários:** Cria novos usuários com CPF, nome, data de nascimento e endereço.
- **Criação de Contas:** Cria contas associadas a um usuário existente.
- **Listagem de Contas:** Exibe todas as contas cadastradas, incluindo número da conta, agência e titular.

## 📂 Estrutura do Código
O código é modular e organizado em funções:

- **`menu()`**: Exibe as opções do sistema.
- **`depositar()`**: Processa depósitos na conta.
- **`sacar()`**: Gerencia saques com validações de saldo e limites.
- **`exibir_extrato()`**: Exibe as movimentações e o saldo atual.
- **`criar_usuario()`**: Cadastra um novo usuário.
- **`filtrar_usuario()`**: Busca usuários pelo CPF.
- **`criar_conta()`**: Cria contas associadas a usuários.
- **`listar_contas()`**: Lista todas as contas cadastradas.
- **`main()`**: Controla o fluxo principal do programa.


## ⚙️ Pré-requisitos
- Python 3.10 ou superior.
- Um editor de código (ex: VS Code) ou terminal para execução.

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/renanboeni/Sistema-Bancario-Simples-em-Python.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Sistema-Bancario-Simples-em-Python
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

4. Siga as instruções do menu interativo.


## 📄 Exemplo de Uso
1. Crie um usuário com CPF, nome, data de nascimento e endereço.
2. Crie uma conta vinculada ao usuário.
3. Deposite um valor na conta.
4. Realize saques, respeitando os limites.
5. Visualize o extrato e as contas criadas.

## 🛡️ Regras de Negócio
- O limite diário de saques é **3**.
- O limite de saque por operação é de **R$ 500,00**.
- Depósitos e saques só podem ser realizados com valores válidos (maiores que zero).
- Cada conta deve estar associada a um CPF único.

## 🖋️ Licença
Este projeto é de código aberto e está licenciado sob os termos da [MIT License](LICENCE.txt).


## 🧑‍💻 Autor
Desenvolvido por [Renan Boeni](https://github.com/renanboeni).

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/renan-boeni-709834335/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/omgboenii/)