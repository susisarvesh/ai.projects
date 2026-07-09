from data import tasks
def display_tasks():

    for task in tasks:
        if task["completed"]:
            print (f"{task['id']}.{task['title']} ✅")
        else:
            print (f"{task['id']}.{task['title']} ❌")
