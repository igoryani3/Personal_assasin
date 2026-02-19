from flask import Flask, jsonify
from flask_cors import CORS
from database import init_db
from routes.courses import courses_bp
from routes.tasks import tasks_bp
from models import Task, Course

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///study_tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)
init_db(app)

app.register_blueprint(courses_bp)
app.register_blueprint(tasks_bp)


@app.route("/api/stats")
def stats():
    unclosed = Course.query.filter(Course.status != "done").count()
    return jsonify({"unclosed_tasks": unclosed})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
