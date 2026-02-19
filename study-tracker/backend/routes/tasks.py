from flask import Blueprint, request, jsonify
from database import db
from models import Task, Course

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/api/courses/<int:course_id>/tasks", methods=["GET"])
def get_tasks(course_id):
    Course.query.get_or_404(course_id)
    tasks = Task.query.filter_by(course_id=course_id).all()
    return jsonify([t.to_dict() for t in tasks])


@tasks_bp.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(
        course_id=data["course_id"],
        name=data.get("name", ""),
        description=data.get("description", ""),
        status=data.get("status", "todo"),
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@tasks_bp.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.name = data.get("name", task.name)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify(task.to_dict())


@tasks_bp.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"ok": True})
