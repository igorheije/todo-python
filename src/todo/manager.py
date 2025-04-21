from .storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        existe = any(t["title"] == title for t in self.tasks)
        if existe:
            print("Essa tarefa já existe.")
            return

        self.tasks.append({"title": title, "done": False, "date": None})
        save_tasks(self.tasks)
        print(f"Tarefa '{title}' adicionada!")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i+1}. {status} {task['title']}")

    def complete_task(self, title):
        for task in self.tasks:
            if task["title"] == title:
                if task["done"] == True:
                    task["done"] = False
                    print(f"Tarefa '{title}' marcada como não concluída.")
                else:
                    task["done"] = True
                    print(f"Tarefa '{title}' marcada como concluída.")
                save_tasks(self.tasks)
                return
        print(f"Tarefa '{title}' não encontrada.")

    def remove_task(self, title):
        existe = any(t["title"] == title for t in self.tasks)
        if existe:
            self.tasks = [t for t in self.tasks if t["title"] != title]
            save_tasks(self.tasks)
            print(f"Tarefa '{title}' removida.")
        print(f"Tarefa '{title}' não encontrada.")
   
    def add_date(self, title, date):
        existe = any(t["title"] == title for t in self.tasks)
        if existe:
            for task in self.tasks:
                if task["title"] == title:
                    task["date"] = date
                    save_tasks(self.tasks)
                    print(f"Tarefa '{title}' atualizada.")
                    return
        print(f"Tarefa '{title}' não encontrada.")
