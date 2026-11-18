"""
========================================================================================
VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12
DEPARTMENT OF INFORMATION TECHNOLOGY
Academic Year: 2026-27 (ODD) | Class: 25IT3A&B
Activity: Project-Based Assessment

Scenario 2: Student Project and Skill Tracking System
Course: 25ITC31 - Foundations of Data Science (Unit 5: EDA & Visualizations)
Student Name: Abhishek.R
Register No : 732925ITR002
Class       : 25IT3A (Section A)
========================================================================================
Automated Visualization Generator
Generates high-resolution publication-quality PNG charts for GitHub submission.
========================================================================================
"""

import os
import sqlite3
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Configure publication-grade styling
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 1.0

def get_db_path():
    candidate_paths = [
        os.path.join(os.path.dirname(__file__), "..", "database", "tracking_system.db"),
        os.path.join(os.path.dirname(__file__), "tracking_system.db"),
        "d:/project 1/database/tracking_system.db",
        "D:\\project 1\\database\\tracking_system.db"
    ]
    for p in candidate_paths:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("tracking_system.db not found.")

def create_visualizations():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    vis_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visualizations")
    os.makedirs(vis_dir, exist_ok=True)

    print("=" * 75)
    print("  VCET IT :: 25ITC31 DATA SCIENCE VISUALIZATION ENGINE")
    print("  Generating required submission charts into:", vis_dir)
    print("=" * 75)

    # -------------------------------------------------------------------------
    # CHART 1: Project Completion Rates (Donut & Progress Bar Chart)
    # -------------------------------------------------------------------------
    print("[*] Generating Chart 1: Project Completion Rates...")
    cursor.execute("SELECT status, COUNT(*) FROM projects GROUP BY status;")
    status_data = cursor.fetchall()
    statuses = [s[0] for s in status_data]
    status_counts = [s[1] for s in status_data]

    cursor.execute("""
    SELECT p.project_title, 
           COUNT(m.milestone_id) AS total_m,
           SUM(CASE WHEN m.status = 'Completed' THEN 1 ELSE 0 END) AS comp_m
    FROM projects p
    LEFT JOIN milestones m ON p.project_id = m.project_id
    GROUP BY p.project_id
    ORDER BY comp_m DESC, p.project_id ASC;
    """)
    proj_progress_data = cursor.fetchall()
    short_titles = [f"P{i+1}: " + (r[0][:16] + "..." if len(r[0]) > 16 else r[0]) for i, r in enumerate(proj_progress_data)]
    progress_pcts = [(r[2] / r[1] * 100.0) if r[1] > 0 else 0.0 for r in proj_progress_data]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Donut Chart
    colors = ['#10b981', '#3b82f6', '#f59e0b', '#ef4444']
    explode = (0.05, 0.0, 0.0, 0.0)
    wedges, texts, autotexts = ax1.pie(
        status_counts, 
        labels=statuses, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors[:len(statuses)],
        explode=explode[:len(statuses)],
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2),
        pctdistance=0.75
    )
    for at in autotexts:
        at.set_color('white')
        at.set_weight('bold')
    ax1.set_title("Overall Project Status Breakdown\n(N=12 Mini-Projects)", fontsize=13, weight='bold', pad=15)

    # Horizontal Bar Chart
    bar_colors = ['#10b981' if p == 100 else '#3b82f6' if p >= 50 else '#94a3b8' for p in progress_pcts]
    y_pos = range(len(short_titles))
    bars = ax2.barh(y_pos, progress_pcts, color=bar_colors, height=0.65, edgecolor='#475569', linewidth=0.5)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(short_titles, fontsize=9)
    ax2.set_xlabel("Milestone Completion Rate (%)", fontsize=11, weight='bold')
    ax2.set_xlim(0, 110)
    ax2.set_title("Individual Project Milestone Progress", fontsize=13, weight='bold', pad=15)
    ax2.grid(axis='x', linestyle='--', alpha=0.5)
    ax2.axvline(100, color='#10b981', linestyle=':', label='100% Target')

    for bar, val in zip(bars, progress_pcts):
        ax2.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height()/2, f"{val:.0f}%", 
                 va='center', fontsize=8, weight='bold', color='#1e293b')

    plt.suptitle("VCET IT - Project Completion Rates & Lifecycle Status\nAuthor: Abhishek.R (732925ITR002)", 
                 fontsize=14, weight='bold', y=1.02)
    plt.tight_layout()
    chart1_path = os.path.join(vis_dir, "1_project_completion_rates.png")
    plt.savefig(chart1_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"    -> Saved: {chart1_path}")

    # -------------------------------------------------------------------------
    # CHART 2: Popular Technology Choices (Frequency Ranking)
    # -------------------------------------------------------------------------
    print("[*] Generating Chart 2: Popular Technology Choices...")
    cursor.execute("SELECT technologies_used FROM projects;")
    tech_rows = cursor.fetchall()
    tech_counter = Counter()
    for row in tech_rows:
        for t in row[0].split(','):
            cleaned = t.strip()
            if cleaned:
                tech_counter[cleaned] += 1

    top_techs = tech_counter.most_common(10)
    names = [t[0] for t in top_techs][::-1]
    counts = [t[1] for t in top_techs][::-1]

    fig, ax = plt.subplots(figsize=(12, 6.5))
    tech_palette = ['#0284c7' if c >= 4 else '#38bdf8' if c >= 2 else '#94a3b8' for c in counts]
    bars = ax.barh(names, counts, color=tech_palette, height=0.6, edgecolor='#0f172a', linewidth=0.6)

    ax.set_title("Most Popular Technology Choices in Student Mini-Projects\nVelalar College of Engineering and Technology | Class: 25IT3A&B", 
                 fontsize=13, weight='bold', pad=15)
    ax.set_xlabel("Number of Projects Utilizing Technology", fontsize=11, weight='bold')
    ax.set_xlim(0, max(counts) + 1.5)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    for bar, c in zip(bars, counts):
        ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2, f"{c} projects", 
                va='center', fontsize=9, weight='bold', color='#0f172a')

    # Subtitle annotation
    plt.figtext(0.5, -0.02, "Top Technologies: Python (Lead Language), Java (Enterprise OOP), React.js (Frontend), SQLite/Pandas", 
                ha="center", fontsize=10, style='italic', color='#475569')

    plt.tight_layout()
    chart2_path = os.path.join(vis_dir, "2_popular_technology_choices.png")
    plt.savefig(chart2_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"    -> Saved: {chart2_path}")

    # -------------------------------------------------------------------------
    # CHART 3: Student Skill Distribution by Category and Proficiency Level
    # -------------------------------------------------------------------------
    print("[*] Generating Chart 3: Student Skill Distribution...")
    cursor.execute("""
    SELECT sk.skill_category, ss.proficiency_level, COUNT(*) 
    FROM student_skills ss
    JOIN skills sk ON ss.skill_id = sk.skill_id
    GROUP BY sk.skill_category, ss.proficiency_level
    ORDER BY sk.skill_category;
    """)
    skill_dist = cursor.fetchall()

    categories = sorted(list(set(r[0] for r in skill_dist)))
    levels = ['Beginner', 'Intermediate', 'Advanced']
    level_colors = {'Beginner': '#cbd5e1', 'Intermediate': '#38bdf8', 'Advanced': '#0284c7'}

    cat_level_map = defaultdict(lambda: defaultdict(int))
    for cat, lvl, cnt in skill_dist:
        cat_level_map[cat][lvl] = cnt

    fig, ax = plt.subplots(figsize=(13, 6.5))
    bar_width = 0.25
    x = list(range(len(categories)))

    for i, lvl in enumerate(levels):
        vals = [cat_level_map[cat][lvl] for cat in categories]
        offsets = [pos + (i - 1) * bar_width for pos in x]
        bars = ax.bar(offsets, vals, width=bar_width, label=lvl, color=level_colors[lvl], edgecolor='#334155', linewidth=0.5)
        for b, v in zip(bars, vals):
            if v > 0:
                ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.1, str(v), 
                        ha='center', fontsize=9, weight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10, weight='bold')
    ax.set_ylabel("Student Competency Count", fontsize=11, weight='bold')
    ax.set_title("Student Technical Skill Distribution across Core Engineering Domains\nGrouped by Proficiency Level (Beginner vs. Intermediate vs. Advanced)", 
                 fontsize=13, weight='bold', pad=15)
    ax.legend(title="Proficiency Level", frameon=True, facecolor='#f8fafc')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_ylim(0, max([cat_level_map[c][l] for c in categories for l in levels]) + 2)

    plt.tight_layout()
    chart3_path = os.path.join(vis_dir, "3_student_skill_distribution.png")
    plt.savefig(chart3_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"    -> Saved: {chart3_path}")

    # -------------------------------------------------------------------------
    # CHART 4: Domain-Wise Evaluation Marks Performance
    # -------------------------------------------------------------------------
    print("[*] Generating Chart 4: Domain-Wise Marks Performance...")
    cursor.execute("""
    SELECT p.domain, e.obtained_marks
    FROM evaluations e
    JOIN projects p ON e.project_id = p.project_id
    ORDER BY p.domain;
    """)
    domain_evals = cursor.fetchall()
    domain_marks = defaultdict(list)
    for dom, m in domain_evals:
        domain_marks[dom].append(m)

    sorted_domains = sorted(domain_marks.keys(), key=lambda d: sum(domain_marks[d])/len(domain_marks[d]), reverse=True)
    avg_marks = [sum(domain_marks[d])/len(domain_marks[d]) for d in sorted_domains]

    fig, ax = plt.subplots(figsize=(12, 6))
    bar_colors = ['#10b981' if a >= 18.5 else '#06b6d4' if a >= 18.0 else '#f59e0b' for a in avg_marks]
    bars = ax.bar(sorted_domains, avg_marks, color=bar_colors, width=0.5, edgecolor='#0f172a', linewidth=0.6)

    ax.axhline(18.0, color='#ef4444', linestyle='--', linewidth=1.5, label='Benchmark Target (18.0 / 20.0)')
    ax.set_title("Domain-Wise Component Evaluation Performance (Mean Score)\nEvaluated by HoD & Subject Faculty Panels", 
                 fontsize=13, weight='bold', pad=15)
    ax.set_ylabel("Mean Obtained Mark (Max 20.0)", fontsize=11, weight='bold')
    ax.set_ylim(14.0, 20.5)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(loc='lower right')

    for bar, avg in zip(bars, avg_marks):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15, f"{avg:.2f}", 
                ha='center', fontsize=9, weight='bold', color='#0f172a')

    plt.xticks(rotation=20, ha='right', fontsize=9, weight='bold')
    plt.tight_layout()
    chart4_path = os.path.join(vis_dir, "4_domain_wise_marks_performance.png")
    plt.savefig(chart4_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"    -> Saved: {chart4_path}")

    conn.close()
    print("\n[+] All 4 visualizations generated and saved successfully!")

if __name__ == "__main__":
    create_visualizations()
