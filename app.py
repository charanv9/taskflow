tasks = []

def create_task(title):
    tasks.append({"title": title, "status": "todo"})
    return tasks

def list_tasks():
    return tasks

def update_task(index, new_title):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title
        return True
    return False

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False

create_task("Complete ISP Task 1")
update_task(0, "Complete ISP Task 1 Successfully")
delete_task(0)
print(list_tasks())