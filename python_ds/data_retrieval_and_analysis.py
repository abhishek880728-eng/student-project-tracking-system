"""
========================================================================================
VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12
DEPARTMENT OF INFORMATION TECHNOLOGY
Academic Year: 2026-27 (ODD) | Class: 25IT3A&B
Activity: Project-Based Assessment

Scenario 2: Student Project and Skill Tracking System
Course: 25ITC31 - Foundations of Data Science
Student Name: Abhishek.R
Register No : 732925ITR002
Class       : 25IT3A (Section A)
========================================================================================
Data Retrieval, Cleaning, Wrangling & Summary Statistics Script
Extracts data from SQLite database, cleans records, and calculates core metrics.
========================================================================================
"""

import os
import sqlite3
import csv
import math
from collections import Counter, defaultdict

def get_db_connection():
    candidate_paths = [
        os.path.join(os.path.dirname(__file__), "..", "database", "tracking_system.db"),
        os.path.join(os.path.dirname(__file__), "tracking_system.db"),
        "d:/project 1/database/tracking_system.db",
        "D:\\project 1\\database\\tracking_system.db"
    ]
    for p in candidate_paths:
        if os.path.exists(p):
            return sqlite3.connect(p)
    raise FileNotFoundError("Could not find tracking_system.db in project directories.")

def retrieve_and_preprocess_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    print("=" * 80)
    print("  VCET IT :: 25ITC31 FOUNDATIONS OF DATA SCIENCE - DATA RETRIEVAL & WRANGLING")
    print("  Student: Abhishek.R (732925ITR002) | Class: 25IT3A")
    print("=" * 80)

    # 1. Retrieve Projects with Student information
    query_projects = """
    SELECT 
        p.project_id,
        p.student_id,
        s.name AS student_name,
        s.class_name,
        s.section,
        p.project_title,
        p.domain,
        p.technologies_used,
        p.status,
        p.created_at,
        COUNT(m.milestone_id) AS total_milestones,
        SUM(CASE WHEN m.status = 'Completed' THEN 1 ELSE 0 END) AS completed_milestones
    FROM projects p
    JOIN students s ON p.student_id = s.student_id
    LEFT JOIN milestones m ON p.project_id = m.project_id
    GROUP BY p.project_id
    ORDER BY p.project_id;
    """
    cursor.execute(query_projects)
    project_rows = cursor.fetchall()
    project_cols = [desc[0] for desc in cursor.description]

    projects = []
    for row in project_rows:
        item = dict(zip(project_cols, row))
        total_m = item['total_milestones']
        comp_m = item['completed_milestones']
        item['progress_pct'] = (comp_m / total_m * 100.0) if total_m > 0 else 0.0
        projects.append(item)

    print(f"\n[+] Successfully extracted {len(projects)} student project records.")

    # 2. Retrieve Student Skills mapping
    query_skills = """
    SELECT 
        ss.student_id,
        s.name AS student_name,
        sk.skill_id,
        sk.skill_name,
        sk.skill_category,
        ss.proficiency_level
    FROM student_skills ss
    JOIN students s ON ss.student_id = s.student_id
    JOIN skills sk ON ss.skill_id = sk.skill_id
    ORDER BY sk.skill_category, sk.skill_name;
    """
    cursor.execute(query_skills)
    skill_rows = cursor.fetchall()
    skill_cols = [desc[0] for desc in cursor.description]
    skills_data = [dict(zip(skill_cols, row)) for row in skill_rows]
    print(f"[+] Successfully extracted {len(skills_data)} student skill mappings.")

    # 3. Retrieve Evaluations
    query_evaluations = """
    SELECT 
        e.eval_id,
        e.project_id,
        p.project_title,
        p.domain,
        e.component_name,
        e.max_marks,
        e.obtained_marks,
        e.evaluator_name,
        e.evaluation_date
    FROM evaluations e
    JOIN projects p ON e.project_id = p.project_id
    ORDER BY e.eval_id;
    """
    cursor.execute(query_evaluations)
    eval_rows = cursor.fetchall()
    eval_cols = [desc[0] for desc in cursor.description]
    eval_data = [dict(zip(eval_cols, row)) for row in eval_rows]
    print(f"[+] Successfully extracted {len(eval_data)} component evaluation records.")

    conn.close()

    # Save cleaned datasets to CSV for transparency
    output_dir = os.path.dirname(os.path.abspath(__file__))
    save_to_csv(os.path.join(output_dir, "clean_projects.csv"), projects, project_cols + ['progress_pct'])
    save_to_csv(os.path.join(output_dir, "clean_skills.csv"), skills_data, skill_cols)
    save_to_csv(os.path.join(output_dir, "clean_evaluations.csv"), eval_data, eval_cols)
    print(f"[+] Exported clean CSV copies to: {output_dir}")

    # Generate Statistical Descriptives
    compute_descriptive_statistics(projects, skills_data, eval_data)

    return projects, skills_data, eval_data

def save_to_csv(filepath, data, fieldnames):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def compute_descriptive_statistics(projects, skills_data, eval_data):
    print("\n" + "=" * 80)
    print("  UNIT 1 & 4: DESCRIPTIVE STATISTICS & SUMMARY METRICS")
    print("=" * 80)

    # 1. Project Lifecycle & Completion Rates
    status_counts = Counter(p['status'] for p in projects)
    total_projects = len(projects)
    print("\n[A] Project Status Distribution:")
    for status, count in status_counts.items():
        pct = (count / total_projects) * 100
        print(f"    - {status:<15}: {count:2d} projects ({pct:5.1f}%)")

    # 2. Technology Frequency Distribution (Unit 3 - Data Wrangling)
    tech_counter = Counter()
    for p in projects:
        techs = [t.strip() for t in p['technologies_used'].split(',') if t.strip()]
        for t in techs:
            tech_counter[t] += 1

    print("\n[B] Top Technology Choices Across Mini-Projects:")
    for tech, count in tech_counter.most_common(8):
        print(f"    - {tech:<20}: {count} occurrences")

    # 3. Domain Distribution
    domain_counts = Counter(p['domain'] for p in projects)
    print("\n[C] Project Distribution by Engineering Domain:")
    for domain, count in domain_counts.items():
        print(f"    - {domain:<25}: {count:2d} projects")

    # 4. Evaluation Marks Statistics (Central Tendency & Variability - Unit 1)
    marks = [e['obtained_marks'] for e in eval_data]
    if marks:
        n = len(marks)
        mean_mark = sum(marks) / n
        sorted_marks = sorted(marks)
        median_mark = (sorted_marks[n//2] if n % 2 != 0 else (sorted_marks[n//2 - 1] + sorted_marks[n//2]) / 2)
        variance = sum((x - mean_mark) ** 2 for x in marks) / n
        std_dev = math.sqrt(variance)

        print("\n[D] Assessment Marks Analysis (Max 20.0 per component):")
        print(f"    - Sample Size (N)       : {n} evaluations")
        print(f"    - Mean Obtained Mark    : {mean_mark:.2f}")
        print(f"    - Median Obtained Mark  : {median_mark:.2f}")
        print(f"    - Standard Deviation    : {std_dev:.2f}")
        print(f"    - Min Mark              : {min(marks):.1f}")
        print(f"    - Max Mark              : {max(marks):.1f}")

    print("=" * 80 + "\n")

if __name__ == "__main__":
    retrieve_and_preprocess_data()
