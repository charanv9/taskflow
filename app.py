"""
TaskFlow application.

This module provides functions for creating and managing tasks.
"""

tasks = []


def create_task(title):
    """Create a new task."""
    tasks.append({"title": title, "status": "todo"})
    return tasks


def list_tasks():
    """Return all tasks."""
    return tasks


def update_task(index, new_title):
    """Update the title of an existing task."""
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title
        return True
    return False


def delete_task(index):
    """Delete a task by its index."""
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False


create_task("Complete ISP Task 1")
update_task(0, "Complete ISP Task 1 Successfully")
delete_task(0)
print(list_tasks())