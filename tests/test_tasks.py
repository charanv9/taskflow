def test_create_task():
    tasks = []
    tasks.append({"title": "Sample Task", "status": "todo"})
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Sample Task"