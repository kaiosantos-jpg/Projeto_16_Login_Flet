
# 🧑‍💻 Projeto: Criação de Usuário com INTERFACE + SQLite3

## 🎯 Objetivo
Criar um pequeno sistema em **Flet** que permita **cadastrar usuários** (nome, email e senha) e salvar os dados em um **banco SQLite3**.

---

## 🧩 Instruções

1. Crie um novo arquivo Python, por exemplo `app.py`.
2. Instale o **Flet** se ainda não tiver:
   ```bash
   pip install flet
   ```
3. O código deve:
   - Ter campos de entrada para **nome**, **email** e **senha**.  
   - Ter um botão **Cadastrar**.  
   - Criar o banco `usuarios.db` (caso não exista).  
   - Inserir os dados na tabela `usuarios`.  
   - Exibir uma mensagem de sucesso com `snackbar`.

---

## 💡 Dica
Use o módulo **sqlite3** para conectar e criar a tabela se não existir.

```python
import sqlite3
```

---

## 🧠 Desafio
Antes de ver a resposta, tente:
1. Criar a função `criar_tabela()` que cria a tabela `usuarios`.
2. Criar a função `cadastrar_usuario()` que insere os dados.
3. Exibir a mensagem de sucesso com `page.snackbar`.

---

## 🧾 Explicação Rápida

- **sqlite3.connect("usuarios.db")** → cria o banco (ou abre se existir).  
- **CREATE TABLE IF NOT EXISTS** → evita erro se a tabela já existir.  
- **snack_bar** → mostra mensagens amigáveis ao usuário.  

---

## 🧪 Teste
Execute o app:
```bash
python app.py
```

Cadastre um usuário e depois verifique o banco:
```bash
sqlite3 usuarios.db
SELECT * FROM usuarios;
```

---

## 🥇 Resultado Esperado
Ao cadastrar:
- O app mostra “Usuário cadastrado com sucesso! ✅”.
- O banco `usuarios.db` contém os dados inseridos.

```
id | nome   | email              | senha
------------------------------------------
1  | Ricardo | ricardo@email.com | 1234
```
