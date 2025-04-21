from todo.manager import TaskManager
import random

def test_add_task():
    tm = TaskManager()
    tm.add_task("Testar tarefa")
    assert any(task["title"] == "Testar tarefa" for task in tm.tasks)

def test_list_tasks_empty(capsys):
    tm = TaskManager()
    tm.tasks = []

    tm.list_tasks()

    captured = capsys.readouterr()
    assert "Nenhuma tarefa encontrada." in captured.out

def test_list_tasks_with_items(capsys):
    tm = TaskManager()
    tm.tasks = [
        {"title": "Estudar Python", "done": False},
        {"title": "Estudar Go", "done": True},
    ]

    tm.list_tasks()

    captured = capsys.readouterr()
    assert "1. [ ] Estudar Python" in captured.out
    assert "2. [x] Estudar Go" in captured.out

def test_complete_task(capsys):
    tm = TaskManager()
    tm.tasks = [
        {"title": "Estudar Python", "done": False},
        {"title": "Estudar Go", "done": True},
    ]

    tm.complete_task("Estudar Python")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Python' marcada como concluída." in captured.out
    assert tm.tasks[0]["done"] == True

    tm.complete_task("Estudar Go")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Go' marcada como não concluída." in captured.out
    assert tm.tasks[1]["done"] == False

    tm.complete_task("Estudar Java")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Java' não encontrada." in captured.out

def test_remove_task(capsys):
    tm = TaskManager()
    tm.tasks = [
        {"title": "Estudar Python", "done": False},
        {"title": "Estudar Go", "done": True},
    ]

    tm.remove_task("Estudar Python")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Python' removida." in captured.out
    assert len(tm.tasks) == 1

    tm.remove_task("Estudar Javascript")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Javascript' não encontrada." in captured.out

def test_add_date_task(capsys):
    tm = TaskManager()
    tm.tasks = [
        {"title": "Estudar Python", "done": False},
        {"title": "Estudar Go", "done": True},
    ]

    tm.add_date("Estudar Python", "02/05/2025")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Python' atualizada." in captured.out
    assert tm.tasks[0]["date"] == "02/05/2025"

    tm.add_date("Estudar Java", "02/05/2025")
    captured = capsys.readouterr()
    assert "Tarefa 'Estudar Java' não encontrada." in captured.out
