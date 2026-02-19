from database import db


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default="")
    teacher_name = db.Column(db.String(200), default="")
    teacher_contact = db.Column(db.String(200), default="")
    status = db.Column(db.String(50), default="active")  # active / done / archive
    semester = db.Column(db.Integer, default=None)
    control_type = db.Column(db.String(50), default=None)  # exam / credit / diff_credit / coursework
    block_date = db.Column(db.String(20), default=None)  # ISO date string YYYY-MM-DD

    tasks = db.relationship("Task", backref="course", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.status == "done")
        progress = round((done / total * 100) if total > 0 else 0)
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "teacher_name": self.teacher_name,
            "teacher_contact": self.teacher_contact,
            "status": self.status,
            "semester": self.semester,
            "control_type": self.control_type,
            "block_date": self.block_date,
            "progress": progress,
            "tasks_total": total,
            "tasks_done": done,
        }


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default="")
    status = db.Column(db.String(50), default="todo")  # todo / in_progress / done

    def to_dict(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
        }
