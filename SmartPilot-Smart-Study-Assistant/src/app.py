"""
StudyPilot - Main Application Controller
Flask REST API and web controller for StudyPilot.
"""

from flask import Flask, jsonify, request
from task_manager import TaskManager
from analytics import AnalyticsEngine

app = Flask(__name__)
tm = TaskManager()

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "StudyPilot Smart Study & Task Planner",
        "status": "Running",
        "endpoints": ["/tasks", "/tasks/add", "/analytics"]
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tm.get_all_tasks()})

@app.route("/tasks/add", methods=["POST"])
def add_task():
    data = request.get_json() or {}
    title = data.get("title", "Untitled Task")
    category = data.get("category", "General")
    priority = data.get("priority", "Medium")
    hours = data.get("estimated_hours", 1.0)
    
    task = tm.add_task(title, category, priority, hours)
    return jsonify({"message": "Task created successfully", "task": task}), 201

@app.route("/analytics", methods=["GET"])
def get_analytics():
    engine = AnalyticsEngine(tm.get_all_tasks())
    return jsonify(engine.calculate_summary())

if __name__ == "__main__":
    print("Starting StudyPilot Smart Study & Task Planner...")
    app.run(host="0.0.0.0", port=5000, debug=True)
