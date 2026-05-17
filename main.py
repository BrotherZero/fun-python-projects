from datetime import datetime
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.text import Text
import time
import argparse


# Display 
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
    def popeye_display():
        console = Console()

        intro =r"""
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⢀⣠⣤⣴⣦⣤⣄⡈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿               
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣟⣛⣻⣧⣬⣭⣉⣙⡛⠿⢿⣿⣿⣿⡿⣫⢂⣽⣷⣽⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣰⣿⣿⣿⣿⣿⠟⢻⣿⣟⣾⣯⣽⣷⣾⣭⣽⣟⠛⣛⣛⣛⡿⣶⣄⠉⢿⣿⣧⠳⣿⣿⣿⣿⣮⢿⣿⣿⣿⣿-------------------------------------
        ⣿⣿⣿⣿⣿⣿⣿⡿⠟⢠⣿⣿⣿⡿⠋⠀⣀⣬⣯⣿⣿⣿⣿⣿⣿⣿⢣⣶⣮⣦⡸⣭⣿⣻⣿⡆⠈⣿⣿⣗⡵⢫⣿⠿⢃⣾⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⡿⠋⣤⣶⣾⣿⡿⠋⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⣿⣿⣿⣷⡘⣿⣿⡿⠀⣰⡿⡫⣪⣾⣷⣶⣾⣿⣿⣿⣿⣿⣿  
        ⣿⣿⣿⣿⡟⠀⣼⣿⣿⣿⠋⠀⢠⣾⣿⡿⢛⣛⡛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣧⠈⣥⣴⣾⣫⢾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   
        ⣿⣿⣿⣿⣇⠀⣿⣿⣿⠃⠀⣴⣿⣿⣯⣿⣿⣿⣿⣿⣷⣤⣝⠻⢿⣿⣿⣿⣿⣇⠀⢻⣧⢉⣭⣥⣥⣄⢤⣤⣄⡉⠻⢿⣿⣿⣿⣿⣿⣿     Github  -->  BrotherZero
        ⣿⣿⣿⣿⣿⣆⠘⢿⣿⡀⢰⣿⣿⢷⣝⣿⣿⣿⣿⣿⣿⣿⡿⠿⠶⣭⣙⣫⣿⣿⣶⣟⣵⣿⣿⣿⣿⣿⡇⢿⣿⣿⣆⠈⢻⣿⣿⣿⣿⣿    Telegram --> t.me/BrotherZero  
        ⣿⣿⣿⣿⣿⣿⣷⣤⣈⠉⢸⣿⣿⣷⣯⣿⣿⣿⣿⣿⣿⣷⣾⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿      
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣛⣻⢿⡿⢿⣿⡿⠿⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣹⣿⣿⣿⣿⡇⠀⣽⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣍⣛⣛⣓⣟⣛⣡⡙⠿⣿⣿⣿⣿⠿⣟⣥⣾⣿⣿⣿⣿⣿⠃⢠⣿⣿⣿⣿⣿              💬💬💬
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⣘⣛⣿⣿⣿⣿⣿⣇⠉⠉⠉⠉⠉⠉⠉⠁⠀⣾⣶⣿⣿⣶⣿⣿⣿⣿⣿⡟⣿⡿⠃⢀⣾⣿⣿⣿⣿⣿-------------------------------------
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⡛⢿⣿⣿⣿⣿⣆⣤⣤⣤⣄⣤⣤⣀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠋⣀⣴⣿⣿⣿⣿⣿⣿⣿  
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⠹⢿⣿⣷⣿⡟⢿⣿⣿⣮⣻⣿⣿⣿⡿⣿⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠉⠛⣉⣤⡀⠙⢿⣿⣟⡿⣿⣿⠿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ " Ya gots a face I likes to touch "
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡉⠉⠛⠛⠿⠿⠛⠛⠉⠁⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿            
        """
        

        def slow_print(text, delay=0.001):
            for char in text:
                console.print(char, end="")
                time.sleep(delay)

        title = Text("Welcome", style="bold magenta")
        subtitle = Text("bzero 🚀", style="bold cyan")
        panel = Panel(
        Align.center(intro),
        title=title,
        subtitle=subtitle,
        border_style="bright_magenta",
        padding=(1,4)
        )

        slow_print(intro)
    

    @staticmethod
    def start_display():
        console = Console()
        title = Text("Welcome", style="bold magenta")
        subtitle = Text("bzero 🚀", style="bold cyan")

        HELP_TEXT = """
            ## Task-Tracker CLI help ##

            Run the app:
            python3 main.py <command> [options]

            General help:
            python3 main.py --help
            python3 main.py add --help
            python3 main.py update --help
            python3 main.py show --help

            Commands:
            add     Add a new task
                    python3 main.py add -n "Buy groceries" -d "Milk and bread" -s todo

            show    Show all tasks, or filter by status
                    python3 main.py show
                    python3 main.py show -s todo
                    python3 main.py show -s in-progress
                    python3 main.py show -s done

            update  Update a task by ID
                    python3 main.py update -i 1 -n "Buy groceries and cook dinner"
                    python3 main.py update -i 1 -s done

            delete  Delete a task by ID
                    python3 main.py delete -i 1
            
            popeye  "Blow me down!"

            Statuses:
            todo, in-progress, done

            Data file:
            main.py stores tasks in tasks.json in the directory where you run the command.
            """

        panel = Panel(
                Align.center(HELP_TEXT),
                title=title,
                subtitle=subtitle,
                border_style="bright_magenta",
                padding=(1,4)
                )

        
        console.print(panel)

#  -------- CLI Interface --------
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
# -------- popeye---------
popeye_parser = subparsers.add_parser("popeye")

args = parser.parse_args()

# -------- COMMAND HANDLER --------
try:
    with open("tasks.json", "r") as f:
        Tasks = json.load(f)
except FileNotFoundError:
    Tasks = []

# ADD 
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

# UPDATE
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

# DELETE 
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

# SHOW
if args.command == "show":

    filtered_tasks = Tasks
    if args.status:
        filtered_tasks = [task for task in Tasks if task["status"] == args.status]
        Display.rich_display(filtered_tasks)

    else:
        Display.rich_display(Tasks)
        
if  args.command == "popeye":
    Display.popeye_display()

if args.command is None :
    Display.start_display()
    

