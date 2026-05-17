from datetime import datetime
import json
from rich.console import Console
from rich.table import Table
import argparse



class Display:

    @staticmethod
    def rich_display(tasks_list):

        console = Console()

        with open("tasks.json", "r") as f:
            tasks = json.load(f)

        table = Table(title="Tasks")

        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Description")
        table.add_column("Status", style="yellow")
        table.add_column("Created At")
        table.add_column("Updated At")

        for task in tasks_list:
            table.add_row(
                str(task["id"]),
                task["name"],
                task["description"],
                task["status"],
                str(task["createdAt"]),
                str(task["updatedAt"])
            )

        console.print(table)
    @staticmethod
    def core_display(tasks_list):
        with open("tasks.json", "r") as f:
            Tasks = json.load(f)

        print("=" * 90)
        print(f"{'ID':<5} {'Name':<15} {'Description':<25} {'Status':<10} {'Created At':<20} {'Updated At':<20}")
        print("=" * 90)

        for task in Tasks:

            print(
            f"{task['id']:<5} {str(task.get('name') or ''):<15} {str(task.get('Description') or ''):<25} "
            f"{str(task.get('Status') or ''):<10} {task['createdAt']:<20} "
            f"{task['updatedAt'] if 'updatedAt' in task else "None"}"
            )
        print("=" * 90)

parser = argparse.ArgumentParser(description="Task Manager CLI")

subparsers = parser.add_subparsers(dest="command")

# -------- ADD --------
add_parser = subparsers.add_parser("add")
add_parser.add_argument("-n", "--name", required=True)
add_parser.add_argument("-d", "--description")
add_parser.add_argument("-s", "--status",choices=["todo", "in-progress", "done"],default="todo" ,help="Status of the task")

# -------- UPDATE --------
update_parser = subparsers.add_parser("update")
update_parser.add_argument("-i", "--id", type=int, required=True)
update_parser.add_argument("-n", "--name")
update_parser.add_argument("-d", "--description" )
update_parser.add_argument("-s", "--status",choices=["todo", "in-progress", "done"], help="Status of the task")

# -------- DELETE --------
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("-i", "--id", type=int, required=True)
# -------- SHOW ---------
show_parser = subparsers.add_parser("show")
show_parser.add_argument("-c", "--classic", action="store_true")
show_parser.add_argument("-s", "--status",choices=["todo", "in-progress", "done"], help="Filter tasks by status")

args = parser.parse_args()

# -------- COMMAND HANDLER --------
try:
    with open("tasks.json", "r") as f:
        Tasks = json.load(f)
except FileNotFoundError:
    Tasks = []

if args.command == "add":
  
    task = {
        "id": len(Tasks) + 1,
        "name": args.name,
        "description": args.description,
        "status": args.status,
        "createdAt": datetime.utcnow().strftime("%Y-%m-%d %H:%M"),
        "updatedAt": None
    }

    Tasks.append(task)
    with open("tasks.json", "w") as f:
        json.dump(Tasks, f, indent=4)

    print("Task added successfully")

elif args.command == "update":
    found = False

    for task in Tasks:
        if task["id"] == args.id:
            task["name"] = args.name if args.name else task["name"]
            task["description"] = args.description if args.description else task["description"]
            task["status"] = args.status if args.status else task["status"]
            task["updatedAt"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
            found = True
            break

    if found:
        with open("tasks.json", "w") as f:
            json.dump(Tasks, f, indent=4)
        print("Task updated successfully")
    else:
        print("Task not found")

elif args.command == "delete":
    found = False
    for task in Tasks:
        if task["id"] == args.id:
            Tasks.remove(task)
            found = True
            break
    if found:
        with open("tasks.json", "w") as f:
            json.dump(Tasks, f, indent=4)
        print("Task has been Deleted")
    else:
        print("Task not found")

if args.command == "show":

    filtered_tasks = Tasks
    if args.status:
        filtered_tasks = [task for task in Tasks if task["status"] == args.status]
        Display.rich_display(filtered_tasks)

    else:
        Display.rich_display(Tasks)


