# Task Tracker CLI Application

This project is a command line interface (CLI) application for managing tasks, based on the requirements defined at [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Command Functionality

The application provides the following commands:

* `tasks.py create <title>`: Create a new task with the given title
* `tasks.py list`: List all incomplete tasks
* `tasks.py list all`: List all tasks
* `tasks.py list completed`: List all completed tasks
* `tasks.py list in_progress`: List all tasks in progress
* `tasks.py update <id> <title>`: Update the title of the task with the given id
* `tasks.py delete <id>`: Delete the task with the given id
* `tasks.py update_in_progress <id>`: Update the task with the given id to be in progress
* `tasks.py update_completed <id>`: Update the task with the given id to be completed
* `tasks.py --help`: to print available commands