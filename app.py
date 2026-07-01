tasks = []

def create_task(title):
    tasks.append({"title": title, "status": "todo"})
    return tasks

create_task("Complete ISP Task 1")
print(tasks)