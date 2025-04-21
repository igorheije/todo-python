from todo.manager import TaskManager
import argparse

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas")
    parser.add_argument("action", choices=["add", "list", "done", "remove", "add_date"])
    parser.add_argument("title", nargs="?")
    parser.add_argument("date", nargs="?")
    args = parser.parse_args()

    tm = TaskManager()

    if args.action == "add" and args.title:
        tm.add_task(args.title)
    elif args.action == "list":
        tm.list_tasks()
    elif args.action == "done" and args.title:
        tm.complete_task(args.title)
    elif args.action == "remove" and args.title:
        tm.remove_task(args.title)
    elif args.action == "add_date" and args.title:
        tm.add_date(args.title, args.date)
    else:
        print("Comando inválido. Use --help")

if __name__ == "__main__":
    main()
