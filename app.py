class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        if not name.strip():
            raise ValueError("Task name cannot be empty")
        
        task = {
            "id": len(self.tasks) + 1, 
            "name": name, 
            "completed": False
        }
        self.tasks.append(task)
        return task

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["completed"]]
