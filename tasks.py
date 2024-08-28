#!/usr/bin/python3

import uuid
import json
from os import error, path
import datetime
import sys



# Load the tasks from the file if it exists, otherwise create the file
if path.exists('tasks.json'):
  with open('tasks.json', 'r') as f:
    tasks = json.load(f)
else:
  with open('tasks.json', 'w') as f:
    # Initialize the tasks dictionary
    tasks = {}
    # Save the empty dictionary to the file
    json.dump(tasks, f)

context_window = {}

def create_task(title):
  """
  Creates a new task with the given title, and saves it to the 'tasks.json' file.
  
  The task is assigned a unique id, which is used as the key in the 'tasks.json' file.
  The task is created with the statuses 'not completed' and 'not started'.
  
  Args:
    title (str): The title of the task.
  
  Returns:
    None
  """
  # Create the task as a dictionary with the given title, and the current time as the created and updated time
  task = {
    "title": title,
    "createdAt": str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
    "updatedAt": str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
    "status": "not completed"
  }
  # Add the task to the dictionary of tasks
  tasks[str(uuid.uuid1())] = task
  # Save the tasks to the file
  with open('tasks.json', 'w') as f:
    json.dump(tasks, f)
  print('task created successfully')

def list_tasks(**kwargs):
  """
  Lists all tasks in the 'tasks.json' file.

  Args:
    **kwargs: The following keyword arguments are accepted:
      readAll (bool): If True, all tasks will be printed. If False, only two tasks will be printed.
      status (str): The status of the tasks to be printed. If not provided, all tasks will be printed.
      load_task (bool): If True, the tasks will not be printed, but instead stored in the context_window dictionary.
  
  Returns:
    None
  """
  # If readAll is True, get the total number of tasks. If False, get the minimum of 2 and the number of tasks.
  num_tasks = len(tasks) if kwargs.get('readAll') else min(2, len(tasks))
  # Iterate over the tasks and print them
  for i, key in enumerate(tasks, start=num_tasks):
    task = tasks[key]
    # If the status is not provided, or the status matches the task's status, print the task
    if not kwargs.get('status') or task['status'] == kwargs.get('status'):
      # If load_task is not True, print the task
      if not kwargs.get('load_task'):
        print(f'id: {i}\ntitle: {task["title"]}\nstatus: {task["status"]}\ncreated at: {task["createdAt"]}\nupdated at: {task["updatedAt"]}\n')
      # If load_task is True, store the task in the context_window dictionary
      context_window[i] = key
      # If we've reached the end of the list and readAll is False, break
      if i < 1 and not kwargs.get('readAll'):
        break
  


def update_task(id, new_title):
  """
  Updates a task with a new title.

  Args:
    id (int): The id of the task to be updated.
    new_title (str): The new title of the task.

  Returns:
    None
  """
  # If the context_window is empty, load the tasks from the file
  if not context_window:
    list_tasks(readAll=True, load_task=True)
  # Get the taskid from the context_window
  taskid = context_window[id]
  # Update the task in the tasks dictionary
  tasks[taskid]["title"] = new_title
  tasks[taskid]["updatedAt"] = str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  # Save the tasks to the file
  with open('tasks.json', 'w') as f:
    json.dump(tasks, f)
  print('task updated successfully')


def delete_task(id):
  """
  Deletes a task.

  Args:
    id (int): The id of the task to be deleted.

  Returns:
    None
  """
  # If the context_window is empty, load the tasks from the file
  if not context_window:
    list_tasks(readAll=True, load_task=True)
  # Get the taskid from the context_window
  taskid = context_window[id]
  # Remove the task from the tasks dictionary
  tasks.pop(taskid)
  # Save the tasks to the file
  with open('tasks.json', 'w') as f:
    json.dump(tasks, f)
  print('task deleted successfully')


def update_status(id, status):
  """
  Updates a task with a new status.

  Args:
    id (int): The id of the task to be updated.
    status (str): The new status of the task.

  Returns:
    None
  """
  # If the context_window is empty, load the tasks from the file
  if not context_window:
    list_tasks(readAll=True, load_task=True)
  # Get the taskid from the context_window
  taskid = context_window[id]
  # Update the task in the tasks dictionary
  tasks[taskid]["status"] = status
  tasks[taskid]["updatedAt"] = str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  # Save the tasks to the file
  with open('tasks.json', 'w') as f:
    json.dump(tasks, f)
  print('task updated successfully')


def help():
  print('''tasks.py create <title>\n
tasks.py list\n
tasks.py list all\n
tasks.py list completed\n
tasks.py list in_progress\n
tasks.py update <id> <title>\n
tasks.py delete <id>\n
tasks.py update_in_progress <id>\n
tasks.py update_completed <id>\n
tasks.py completed <id>\n
tasks.py in_progress <id>\n''')
  

args = sys.argv[1:]
try:
  if args[0] == 'create':
    create_task(args[1])
  elif args[0] == 'list':
    if len(args) == 1:
      list_tasks()
    elif args[0] == 'list' and args[1] == 'all':
      list_tasks(readAll=True)
    elif args[0] == 'list' and args[1] == 'completed':
      list_tasks(status='completed')
    elif args[0] == 'list' and args[1] == 'in_progress':
      list_tasks(status='in_progress')
    else:
      raise error
  elif args[0] == 'update':
    update_task(int(args[1]), args[2])
  elif args[0] == 'delete':
    delete_task(int(args[1]))
  elif args[0] == 'completed':
    update_status(int(args[1]), 'completed')
  elif args[0] == 'in_progress':
    update_status(int(args[1]), 'in_progress')
  elif args[0] == '--help' or args[0] == '-h':
    help()
  else:
    print('run tasks.py --help / -h for help')
    
except:
  print('run tasks.py --help for help')