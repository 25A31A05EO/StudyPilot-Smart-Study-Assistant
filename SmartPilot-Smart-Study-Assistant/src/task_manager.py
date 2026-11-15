"""
StudyPilot - Task Manager Module
Handles task creation, storage, and retrieval.
"""

import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_tasks(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, category="General", priority="Medium", estimated_hours=1.0):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "category": category,
            "priority": priority,
            "estimated_hours": float(estimated_hours),
            "status": "Pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_all_tasks(self):
        return self.tasks

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                self.save_tasks()
                return True
        return False
