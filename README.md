# Task Tracker CLI

A clean command-line task tracker for managing what you need to do, what is in progress, and what is done. Tasks are saved locally in `tasks.json`.

## Features

- Add tasks with a name, description, and status.
- Update task details by ID.
- Delete tasks by ID.
- Mark tasks as `in-progress` or `done`.
- Show all tasks or filter by status.
- Use a rich table display when `rich` is installed, with a plain text fallback.

## Requirements

- Python 3.10 or newer
-  `rich` for prettier terminal output

Install the optional display dependency:

```bash
pip install rich
```

## Usage

Run commands from the project folder:

```bash
python3 main.py <command> [options]
```

Show the fancy intro and command help:

```bash
python3 main.py
```

Show full help:

```bash
python3 main.py --help
```

Show help for one command:

```bash
python3 main.py add --help
python3 main.py update --help
python3 main.py show --help
```

## Commands

### Add a task

```bash
python3 main.py add -n "Buy groceries" -d "Milk, eggs, and bread"
```

Options:

- `-n`, `--name`: task name. Required.
- `-d`, `--description`: task description. Optional.
- `-s`, `--status`: task status. Choices: `todo`, `in-progress`, `done`. Default: `todo`.

### Show tasks

```bash
python3 main.py show
```

Filter by status:

```bash
python3 main.py show -s todo
python3 main.py show -s in-progress
python3 main.py show -s done
```

### Update a task

```bash
python3 main.py update -i 1 -n "Buy groceries and cook dinner"
python3 main.py update -i 1 -s in-progress
```

Options:

- `-i`, `--id`: task ID. Required.
- `-n`, `--name`: new task name. Optional.
- `-d`, `--description`: new task description. Optional.
- `-s`, `--status`: new status. Choices: `todo`, `in-progress`, `done`.


### Delete a task

```bash
python3 main.py delete -i 1
```

## Data Format

Tasks are stored in `tasks.json`:

```json
[
    {
        "id": 1,
        "name": "Buy groceries",
        "description": "Milk, eggs, and bread",
        "status": "todo",
        "createdAt": "2026-05-17 18:55",
        "updatedAt": null
    }
]
```

## Notes

- If `tasks.json` does not exist, the app creates it automatically.
- If `rich` is not installed, the app still works and uses classic text output.
- Task IDs keep increasing from the highest existing ID, so deleting a task does not reuse old IDs.


<img width="1118" height="662" alt="image" src="https://github.com/user-attachments/assets/6f51c0f2-1651-401b-bfbc-0395878f5fa1" />

