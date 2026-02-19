#!/usr/bin/env python3
"""
Import grade.csv into the Study Tracker SQLite database.
Each CSV row = one Course (discipline). No tasks are created.
Run from the backend directory:
    python3 import_csv.py ../grade.csv
"""

import csv
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app import app
from database import db
from models import Course, Task


def parse_course_status(mark: str, deadline: str) -> str:
    """Map CSV mark + deadline to course status."""
    mark = (mark or "").strip().lower()
    deadline = (deadline or "").strip()

    if mark in ("зачтено", "5", "4", "3", "2"):
        return "done"
    if mark == "неявка":
        return "active"
    if deadline:
        return "active"
    return "active"


def build_description(row: dict) -> str:
    parts = []
    kind = (row["Вид контроля"] or "").strip()
    mark = (row["Отметка"] or "").strip()
    deadline = (row["Дата блокировки"] or "").strip()

    if kind:
        parts.append(f"Вид контроля: {kind}")
    if mark:
        parts.append(f"Отметка: {mark}")
    if deadline:
        parts.append(f"Дата блокировки: {deadline}")
    return "\n".join(parts)


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "../grade.csv"
    csv_path = os.path.abspath(csv_path)

    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        sys.exit(1)

    print(f"📂 Reading {csv_path}...")

    rows = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Дисциплина"].strip():
                rows.append(row)

    print(f"   Found {len(rows)} records")

    with app.app_context():
        Task.query.delete()
        Course.query.delete()
        db.session.commit()
        print("   Cleared existing data")

        for row in rows:
            status = parse_course_status(row["Отметка"], row["Дата блокировки"])
            sem_raw = (row.get("Семестр") or "").strip()
            semester = int(sem_raw) if sem_raw.isdigit() else None
            course = Course(
                name=row["Дисциплина"].strip(),
                description=build_description(row),
                teacher_name=(row["Преподаватель"] or "").strip(),
                teacher_contact="",
                status=status,
                semester=semester,
            )
            db.session.add(course)

        db.session.commit()

        total = Course.query.count()
        done = Course.query.filter_by(status="done").count()
        active = total - done

        print(f"\n✅ Import complete!")
        print(f"   Disciplines: {total} total")
        print(f"   Done:        {done}")
        print(f"   Open:        {active}")


if __name__ == "__main__":
    main()
