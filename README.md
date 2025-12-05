# 🏧 Simulador de Caixa Eletrônico (ATM) - Python

Um sistema bancário completo rodando via terminal. O projeto simula as principais operações de um ATM, com foco em segurança (login), manipulação de dados financeiros e histórico de transações.

## 🔑 Acesso ao Sistema (Credenciais)

Para testar o sistema, utilize um dos usuários cadastrados no banco de dados fictício:

| Usuário | Senha | Nível |
| :--- | :--- | :--- |
| **FELIPE** | `1234` | Cliente |
| **ADMIN** | `0000` | Administrador |

## 🛠️ Funcionalidades

- [x] **Sistema de Login:** Validação de credenciais usando Dicionários. O acesso é bloqueado se usuário ou senha estiverem incorretos.
- [x] **Operações Financeiras:**
    - Consultar Saldo (Formatado em R$).
    - Depósito (Soma ao saldo e registra no histórico)
    - Saque (Verifica disponibilidade de fundos antes de subtrair).
- [x] **Extrato Dinâmico:** Utilização de Listas (`append`) para gravar cada transação realizada e exibi-las sob demanda.
- [x] **Loop de Menu:** O sistema mantém a sessão ativa permitindo múltiplas operações até o usuário decidir sair.

## 💻 Tecnologias

* Python 3
* Estruturas de Dados: Dicionários (Auth) e Listas (Log de transações).
* Formatação de Strings (f-strings para moeda).

---
Desenvolvido por **Felipe de Campos** 🦁
