import pytest
from app import TaskManager

def test_add_valid_task():
    manager = TaskManager()
    task = manager.add_task("Learn Jenkins")
    
    assert task["name"] == "Learn Jenkins"
    assert task["completed"] is False
    assert len(manager.tasks) == 1

def test_add_empty_task():
    manager = TaskManager()
    # The test passes if the app successfully blocks the bad input
    with pytest.raises(ValueError, match="Task name cannot be empty"):
        manager.add_task("   ")

def test_complete_existing_task():
    manager = TaskManager()
    manager.add_task("Build Pipeline")
    
    success = manager.complete_task(1)
    
    assert success is True
    assert manager.tasks[0]["completed"] is True

def test_get_pending_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    
    manager.complete_task(1) # Complete the first task
    
    pending = manager.get_pending_tasks()
    assert len(pending) == 1
    assert pending[0]["name"] == "Task 2"
