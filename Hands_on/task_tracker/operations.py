import data as tasks
import json

with open('taskslist.json', 'r') as file:
    try:
        tasks = json.load(file)
    except json.JSONDecodeError:
        print("fuck ooff")

def complete_task(task_id):
    for task in tasks:
        if task["completed"]:
             print("Task is already completed.")
             return
  
        if task["id"] == task_id:
            task["completed"] = True
            print("Task Checked Complete ✅")
            return
        
    print("Task Not found")


def add_task(title , completed =False):
    n = len(tasks)
    if title == "" :
        print("Please enter a valid title and Completed status")
        return
    new_data = {"id":tasks[n-1]["id"]+1, "title":title,"completed":completed}
    tasks.append(new_data)

def delete_task(id):
    
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            print("Done",id)
            return
    else:
        print("Task with id not found")

def save_tasks(content):
    try:
       with open("taskslist.json","w") as f:
        json.dump(content,f)
    except FileNotFoundError:
       print("no file availaible")
def load_tasks():
    try:
        with open("taskslist.json","r") as f:
            content = json.load(f)
            return content
    except json.JSONDecodeError:
        print("no found")

    
# save_tasks(load_tasks())
