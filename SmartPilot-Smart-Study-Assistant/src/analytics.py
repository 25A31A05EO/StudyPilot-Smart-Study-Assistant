"""
StudyPilot - Analytics Engine
Computes completion metrics and productivity scores.
"""

class AnalyticsEngine:
    def __init__(self, tasks):
        self.tasks = tasks

    def calculate_summary(self):
        total = len(self.tasks)
        if total == 0:
            return {
                "total_tasks": 0,
                "completed_tasks": 0,
                "pending_tasks": 0,
                "completion_rate": 0.0
            }

        completed = sum(1 for t in self.tasks if t.get("status") == "Completed")
        pending = total - completed
        rate = round((completed / total) * 100, 2)

        return {
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending,
            "completion_rate": rate
        }
