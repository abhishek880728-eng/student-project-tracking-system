"""
========================================================================================
VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12
DEPARTMENT OF INFORMATION TECHNOLOGY
Course: 25ITT33 - Software Engineering (Unit 5: Project Management & Metrics)
Student: Abhishek.R | Register No: 732925ITR002 | Class: 25IT3A
Activity: Project-Based Assessment - Scenario 2

Lines of Code (LOC) & Software Metrics Calculator
Calculates LOC, SLOC, Blank, Comment lines, and COCOMO Software Estimation Metrics.
========================================================================================
"""

import os
import math
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

IGNORE_DIRS = {'.git', '.tools', 'bin', 'lib', '.system_generated', '__pycache__', '.idea', '.vscode'}

LANGUAGE_EXTS = {
    'Java': ['.java'],
    'Python': ['.py'],
    'SQL': ['.sql'],
    'Web / HTML / JS': ['.html', '.js', '.css'],
    'Documentation (Markdown)': ['.md'],
    'Batch Scripts': ['.bat'],
    'Data / Config (JSON, CSV)': ['.json', '.csv', '.ipynb']
}

def analyze_file(filepath, ext):
    total = 0
    blank = 0
    comment = 0
    code = 0

    is_block_comment = False

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            total = len(lines)

            for line in lines:
                s = line.strip()
                if not s:
                    blank += 1
                    continue

                if ext in ['.java', '.js', '.css']:
                    if is_block_comment:
                        comment += 1
                        if '*/' in s:
                            is_block_comment = False
                        continue
                    if s.startswith('/*'):
                        comment += 1
                        if '*/' not in s:
                            is_block_comment = True
                        continue
                    if s.startswith('//'):
                        comment += 1
                        continue

                elif ext == '.py':
                    if is_block_comment:
                        comment += 1
                        if '"""' in s or "'''" in s:
                            is_block_comment = False
                        continue
                    if s.startswith('"""') or s.startswith("'''"):
                        comment += 1
                        if s.count('"""') == 1 or s.count("'''") == 1:
                            is_block_comment = True
                        continue
                    if s.startswith('#'):
                        comment += 1
                        continue

                elif ext == '.sql':
                    if s.startswith('--'):
                        comment += 1
                        continue

                elif ext == '.html':
                    if s.startswith('<!--'):
                        comment += 1
                        continue

                elif ext == '.bat':
                    if s.lower().startswith('rem ') or s.startswith('::'):
                        comment += 1
                        continue

                code += 1

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return total, code, comment, blank

def scan_project():
    stats = {}
    for lang in LANGUAGE_EXTS:
        stats[lang] = {
            'files': 0, 'total': 0, 'code': 0, 'comment': 0, 'blank': 0, 'details': []
        }

    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            matched_lang = None
            for lang, exts in LANGUAGE_EXTS.items():
                if ext in exts:
                    matched_lang = lang
                    break

            if matched_lang:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, PROJECT_ROOT)
                tot, cod, com, blk = analyze_file(full_path, ext)

                stats[matched_lang]['files'] += 1
                stats[matched_lang]['total'] += tot
                stats[matched_lang]['code'] += cod
                stats[matched_lang]['comment'] += com
                stats[matched_lang]['blank'] += blk
                stats[matched_lang]['details'].append({
                    'file': rel_path, 'total': tot, 'code': cod, 'comment': com, 'blank': blk
                })

    return stats

def calculate_cocomo(source_kloc):
    """
    Basic COCOMO Estimation Model (Organic Mode for small team academic projects):
    Effort (E) = a * (KLOC)^b [Person-Months] (a=2.4, b=1.05)
    Development Time (D) = c * (E)^d [Months] (c=2.5, d=0.38)
    Average Staffing (SS) = E / D [Persons]
    """
    a, b = 2.4, 1.05
    c, d = 2.5, 0.38

    kloc = max(source_kloc, 0.1)
    effort = a * (kloc ** b)
    duration = c * (effort ** d)
    staff = effort / duration
    productivity = kloc / effort

    return {
        'kloc': kloc,
        'effort_pm': effort,
        'duration_months': duration,
        'avg_staff': staff,
        'productivity_kloc_pm': productivity
    }

def print_and_save_report(stats):
    lines_output = []

    def p(s=""):
        print(s)
        lines_output.append(s)

    p("=" * 85)
    p("  VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS)")
    p("  DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A")
    p("  Course: 25ITT33 - Software Engineering (Unit 5: Project Management & Metrics)")
    p("  Student: Abhishek.R | Register No: 732925ITR002")
    p("  Activity: Project-Based Assessment - Scenario 2")
    p("=" * 85)
    p(f"  Execution Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    p("=" * 85)
    p()
    p("--- SUMMARY: LINES OF CODE (LOC) BREAKDOWN BY LANGUAGE / CATEGORY ---")
    p(f"{'Category / Language':<26} | {'Files':<5} | {'Total LOC':<10} | {'SLOC (Code)':<11} | {'Comments':<9} | {'Blank':<6}")
    p("-" * 85)

    grand_files = 0
    grand_total = 0
    grand_code = 0
    grand_comment = 0
    grand_blank = 0

    core_source_code_loc = 0

    for lang, data in sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True):
        if data['files'] == 0:
            continue
        grand_files += data['files']
        grand_total += data['total']
        grand_code += data['code']
        grand_comment += data['comment']
        grand_blank += data['blank']

        if lang in ['Java', 'Python', 'SQL', 'Web / HTML / JS']:
            core_source_code_loc += data['code']

        p(f"{lang:<26} | {data['files']:^5} | {data['total']:^10} | {data['code']:^11} | {data['comment']:^9} | {data['blank']:^6}")

    p("-" * 85)
    p(f"{'GRAND TOTAL':<26} | {grand_files:^5} | {grand_total:^10} | {grand_code:^11} | {grand_comment:^9} | {grand_blank:^6}")
    p("=" * 85)
    p()

    # Unit 5 COCOMO Analysis
    kloc = grand_total / 1000.0
    source_kloc = core_source_code_loc / 1000.0
    cocomo = calculate_cocomo(source_kloc)

    p("--- UNIT 5 SOFTWARE ENGINEERING METRICS & PROJECT ESTIMATION ---")
    p(f"• Total Project Size (All Artifacts)       : {grand_total:,} Lines ({kloc:.3f} KLOC)")
    p(f"• Pure Executable Source Code (SLOC)        : {core_source_code_loc:,} Lines ({source_kloc:.3f} KLOC)")
    p(f"• Total Comments & Documentation Overhead   : {grand_comment:,} Lines ({grand_comment/grand_total*100:.1f}%)")
    p(f"• Blank / Formatting Spacing Lines          : {grand_blank:,} Lines ({grand_blank/grand_total*100:.1f}%)")
    p()
    p("• Basic COCOMO Estimation Model (Organic Mode):")
    p(f"    - Formula for Effort          : Effort = 2.4 * (KLOC)^1.05")
    p(f"    - Estimated Effort            : {cocomo['effort_pm']:.2f} Person-Months")
    p(f"    - Formula for Duration        : Time = 2.5 * (Effort)^0.38")
    p(f"    - Estimated Development Time  : {cocomo['duration_months']:.2f} Months")
    p(f"    - Recommended Staff Size      : {cocomo['avg_staff']:.2f} Person(s) (~1-2 developers)")
    p(f"    - Estimated Productivity      : {cocomo['productivity_kloc_pm']:.2f} KLOC / Person-Month")
    p("=" * 85)
    p()

    # Detailed File-by-File Breakdown
    p("--- DETAILED FILE-BY-FILE LINE COUNT AUDIT ---")
    p(f"{'File Relative Path':<48} | {'Total':<6} | {'Code':<6} | {'Comment':<7} | {'Blank':<5}")
    p("-" * 85)
    for lang, data in stats.items():
        if not data['details']:
            continue
        p(f"[{lang.upper()}]")
        for item in sorted(data['details'], key=lambda x: x['total'], reverse=True):
            p(f"  {item['file']:<46} | {item['total']:^6} | {item['code']:^6} | {item['comment']:^7} | {item['blank']:^5}")
        p()

    # Write Markdown Report to docs/LOC_METRICS_REPORT.md
    report_md_path = os.path.join(PROJECT_ROOT, "docs", "LOC_METRICS_REPORT.md")
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write("# SOFTWARE PROJECT METRICS & LINES OF CODE (LOC) AUDIT REPORT\n\n")
        f.write("**Institution:** Velalar College of Engineering and Technology (Autonomous), Erode - 12  \n")
        f.write("**Department:** Department of Information Technology | **Class:** 25IT3A (Section A)  \n")
        f.write("**Course Code & Title:** 25ITT33 - Software Engineering (**Unit 5: Project Management & Metrics**)  \n")
        f.write("**Student Name:** Abhishek.R | **Register Number:** 732925ITR002  \n")
        f.write("**Activity:** Project-Based Assessment - Scenario 2 (Student Project and Skill Tracking System)  \n\n")
        f.write("---\n\n")

        f.write("## 1. Executive Summary: Lines of Code (LOC) Breakdown\n\n")
        f.write("| Category / Technology | Files | Total LOC | Source Code (SLOC) | Comments (CLOC) | Blank Lines |\n")
        f.write("|:---|:---:|:---:|:---:|:---:|:---:|\n")
        for lang, data in sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True):
            if data['files'] > 0:
                f.write(f"| **{lang}** | {data['files']} | {data['total']:,} | {data['code']:,} | {data['comment']:,} | {data['blank']:,} |\n")
        f.write(f"| **GRAND TOTAL** | **{grand_files}** | **{grand_total:,}** | **{grand_code:,}** | **{grand_comment:,}** | **{grand_blank:,}** |\n\n")

        f.write("---\n\n")
        f.write("## 2. Software Engineering Estimation & COCOMO Analysis (Unit 5)\n\n")
        f.write(f"* **Total Project Scale:** `{grand_total:,}` total lines across `{grand_files}` files (`{kloc:.3f}` KLOC).\n")
        f.write(f"* **Core Executable Source Code:** `{core_source_code_loc:,}` lines (`{source_kloc:.3f}` KLOC) across Java, Python, SQL, and Web frontend.\n")
        f.write(f"* **Documentation Density:** `{grand_comment:,}` lines of technical commentary and structured markdown.\n")
        f.write(f"* **Basic COCOMO Effort Estimation:**\n")
        f.write(f"  $$\\text{{Effort}} = 2.4 \\times (\\text{{KLOC}})^{{1.05}} = 2.4 \\times ({source_kloc:.3f})^{{1.05}} \\approx {cocomo['effort_pm']:.2f} \\text{{ Person-Months}}$$\n")
        f.write(f"* **Development Duration Estimation:**\n")
        f.write(f"  $$\\text{{Duration}} = 2.5 \\times (\\text{{Effort}})^{{0.38}} = 2.5 \\times ({cocomo['effort_pm']:.2f})^{{0.38}} \\approx {cocomo['duration_months']:.2f} \\text{{ Months}}$$\n")
        f.write(f"* **Recommended Staff Size:** `{cocomo['avg_staff']:.2f}` developer(s) (optimally suited for a single student mini-project).\n\n")

        f.write("---\n\n")
        f.write("## 3. Detailed File-Level Line Count Matrix\n\n")
        f.write("| Relative File Path | Language | Total Lines | Code (SLOC) | Comments | Blank |\n")
        f.write("|:---|:---|:---:|:---:|:---:|:---:|\n")
        for lang, data in stats.items():
            for item in sorted(data['details'], key=lambda x: x['total'], reverse=True):
                f.write(f"| `{item['file']}` | {lang} | {item['total']} | {item['code']} | {item['comment']} | {item['blank']} |\n")

    print(f"\n[+] Generated and saved Markdown report to: {report_md_path}")

if __name__ == "__main__":
    file_stats = scan_project()
    print_and_save_report(file_stats)
