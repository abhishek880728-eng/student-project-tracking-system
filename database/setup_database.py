"""
Velalar College of Engineering and Technology, Erode - 12
Department of Information Technology
Activity: Project-Based Assessment | Academic Year: 2026-27 (ODD)
Student: Abhishek.R (732925ITR002) | Class: 25IT3A

Automated Database Initialization Script
Executes schema.sql and seed_data.sql into tracking_system.db
"""

import os
import sqlite3
import sys

def initialize_database():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "tracking_system.db")
    schema_path = os.path.join(current_dir, "schema.sql")
    seed_path = os.path.join(current_dir, "seed_data.sql")

    print("=" * 70)
    print("  VCET IT - Student Project & Skill Tracking System (DBMS Setup)")
    print("  Student: Abhishek.R (Reg No: 732925ITR002) | Class: 25IT3A")
    print("=" * 70)
    print(f"[*] Target Database File: {db_path}")

    # Remove stale journal file if it exists
    journal_path = db_path + "-journal"
    if os.path.exists(journal_path):
        try:
            os.remove(journal_path)
        except Exception:
            pass

    # Connect to SQLite database with 30s busy timeout
    conn = sqlite3.connect(db_path, timeout=30.0)
    cursor = conn.cursor()

    # Enable foreign keys and busy timeout
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("PRAGMA busy_timeout = 30000;")

    # Execute schema
    print(f"[*] Reading and applying schema: {schema_path}")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    print("    -> Schema tables, constraints, and indexes created successfully.")

    # Execute seed data
    print(f"[*] Reading and applying seed dataset: {seed_path}")
    with open(seed_path, "r", encoding="utf-8") as f:
        seed_sql = f.read()
    cursor.executescript(seed_sql)
    print("    -> Master data, students, skills, projects, milestones & evaluations inserted.")

    conn.commit()

    # Table Count Summary
    tables = ["students", "skills", "student_skills", "projects", "milestones", "evaluations"]
    print("\n" + "-" * 40)
    print(f"  {'Table Name':<20} | {'Record Count':<10}")
    print("-" * 40)
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table:<20} | {count:<10}")
    print("-" * 40)

    conn.close()
    print("[+] Database setup completed successfully!\n")

if __name__ == "__main__":
    initialize_database()
