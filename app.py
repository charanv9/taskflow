tasks = []

def create_task(title):
    tasks.append({"title": title, "status": "todo"})
    return tasks
def list_tasks():
    return tasks

create_task("Complete ISP Task 1")
print(list_tasks())