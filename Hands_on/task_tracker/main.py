from display import display_tasks
from operations import add_task , complete_task , delete_task ,save_tasks,load_tasks


load_tasks()
add_task("go out")
delete_task(2)
complete_task(1)

display_tasks()
