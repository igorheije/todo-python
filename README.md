# 📝 Todo CLI

Um pequeno projeto em Python para gerenciar tarefas diretamente pelo terminal. Permite adicionar, listar, marcar como concluída, remover e atualizar tarefas com data.

---

## 🚀 Funcionalidades

- ✅ Adicionar uma nova tarefa
- 📋 Listar todas as tarefas
- ✔️ Marcar tarefa como concluída ou não concluída
- ❌ Remover tarefa
- 🗓️ Adicionar ou atualizar data de uma tarefa

---

## 🛠️ Estrutura do Projeto

todo_python/
├── src/
│ ├── todo/
│ │ ├── **init**.py
│ │ ├── main.py  
│ │ ├── manager.py  
│ │ └── storage.py
│
├── tests/
│ ├── test_manager.py
│ └── test_storage.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── pyproject.toml

---

## 💻 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/igor-heije/todo-python.git
cd todo-python
```

### 2. Execulte os comandos

# Adicionar uma tarefa

python run.py add "Estudar Python"

# Listar tarefas

python run.py list

# Marcar como concluída/não concluída

python run.py done "Estudar Python"

# Remover tarefa

python run.py remove "Estudar Python"

# Adicionar data

python run.py add_date "Estudar Go" "2025-04-25"

### 3. Execulte os teste

PYTHONPATH=src pytest
