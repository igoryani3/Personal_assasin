from flask import Blueprint, request, jsonify
from database import db
from models import Course

courses_bp = Blueprint("courses", __name__)


@courses_bp.route("/api/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses])


@courses_bp.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify(course.to_dict())


@courses_bp.route("/api/courses", methods=["POST"])
def create_course():
    data = request.get_json()
    course = Course(
        name=data.get("name", ""),
        description=data.get("description", ""),
        teacher_name=data.get("teacher_name", ""),
        teacher_contact=data.get("teacher_contact", ""),
        status=data.get("status", "active"),
        semester=data.get("semester"),
        control_type=data.get("control_type"),
        block_date=data.get("block_date"),
    )
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201


@courses_bp.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    course.name = data.get("name", course.name)
    course.description = data.get("description", course.description)
    course.teacher_name = data.get("teacher_name", course.teacher_name)
    course.teacher_contact = data.get("teacher_contact", course.teacher_contact)
    course.status = data.get("status", course.status)
    if "semester" in data:
        course.semester = data["semester"]
    if "control_type" in data:
        course.control_type = data["control_type"]
    if "block_date" in data:
        course.block_date = data["block_date"]
    db.session.commit()
    return jsonify(course.to_dict())


@courses_bp.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"ok": True})
