"""
Migration: extract 'Вид контроля' and 'Дата блокировки' from description
into the dedicated control_type and block_date columns.
"""
import re
import sys
import os

# Add backend dir to path so we can import app
sys.path.insert(0, os.path.dirname(__file__))

from app import app
from database import db
from models import Course

CONTROL_MAP = {
    "зачет": "credit",
    "зачёт": "credit",
    "экзамен": "exam",
    "дифференцированный зачет": "diff_credit",
    "дифференцированный зачёт": "diff_credit",
    "диф. зачет": "diff_credit",
    "диф. зачёт": "diff_credit",
    "курсовая": "coursework",
    "курсовая работа": "coursework",
}


def parse_control_type(description: str):
    m = re.search(r"Вид контроля:\s*(.+)", description)
    if not m:
        return None
    raw = m.group(1).strip().lower()
    return CONTROL_MAP.get(raw, raw)


def parse_block_date(description: str):
    m = re.search(r"Дата блокировки:\s*(\d{2}\.\d{2}\.\d{4})", description)
    if not m:
        return None
    d, mo, y = m.group(1).split(".")
    return f"{y}-{mo}-{d}"


def clean_description(description: str) -> str:
    """Remove the control/block lines from description."""
    lines = description.split("\n")
    cleaned = [
        l for l in lines
        if not l.startswith("Вид контроля:") and not l.startswith("Дата блокировки:")
    ]
    return "\n".join(cleaned).strip()


with app.app_context():
    courses = Course.query.all()
    updated = 0
    for c in courses:
        if not c.description:
            continue
        ct = parse_control_type(c.description)
        bd = parse_block_date(c.description)
        if ct is not None or bd is not None:
            if ct is not None and c.control_type is None:
                c.control_type = ct
            if bd is not None and c.block_date is None:
                c.block_date = bd
            # Clean up description
            c.description = clean_description(c.description)
            updated += 1
            print(f"  [{c.id}] {c.name[:40]:40s} → control={c.control_type}, block={c.block_date}")
    db.session.commit()
    print(f"\nДонe. Обновлено курсов: {updated}")
