"""
========================================================================================
VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12
DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A
Activity: Project-Based Assessment - Scenario 2
Student: Abhishek.R (732925ITR002)

Lightweight Embedded Web Server & REST API for Student Project Tracking System
Zero third-party dependencies (Built purely on Python standard library)
========================================================================================
"""

import os
import sys
import json
import sqlite3
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

PORT = 8080

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

class TrackingRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        super().__init__(*args, directory=root_dir, **kwargs)

    def end_headers(self):
        if self.path.endswith(('.png', '.svg', '.jpg', '.jpeg', '.css', '.js', '.ico')):
            self.send_header('Cache-Control', 'public, max-age=3600')
        elif self.path.startswith('/api/'):
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/"):
            self.handle_api(path)
        else:
            super().do_GET()

    def handle_api(self, path):
        db_path = get_db_path()
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        data = None
        if path == "/api/summary":
            cursor.execute("""
            SELECT 
                COUNT(*) AS total_projects,
                SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed_projects,
                SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress_projects,
                SUM(CASE WHEN status = 'Under Review' THEN 1 ELSE 0 END) AS under_review_projects,
                SUM(CASE WHEN status = 'Proposed' THEN 1 ELSE 0 END) AS proposed_projects
            FROM projects;
            """)
            summary_row = dict(cursor.fetchone())

            cursor.execute("SELECT AVG(obtained_marks) AS avg_mark FROM evaluations;")
            avg_row = cursor.fetchone()
            summary_row["avg_mark"] = round(avg_row["avg_mark"], 2) if avg_row and avg_row["avg_mark"] else 0.0

            cursor.execute("SELECT COUNT(*) AS total_students FROM students;")
            summary_row["total_students"] = cursor.fetchone()["total_students"]
            data = summary_row

        elif path == "/api/students":
            cursor.execute("SELECT * FROM students ORDER BY student_id ASC;")
            students = [dict(r) for r in cursor.fetchall()]
            for s in students:
                cursor.execute("""
                SELECT sk.skill_name, sk.skill_category, ss.proficiency_level
                FROM student_skills ss
                JOIN skills sk ON ss.skill_id = sk.skill_id
                WHERE ss.student_id = ?
                ORDER BY sk.skill_name;
                """, (s["student_id"],))
                s["skills"] = [dict(r) for r in cursor.fetchall()]
            data = students

        elif path == "/api/projects":
            cursor.execute("""
            SELECT p.*, s.name AS student_name, s.class_name, s.section
            FROM projects p
            JOIN students s ON p.student_id = s.student_id
            ORDER BY p.project_id ASC;
            """)
            projects = [dict(r) for r in cursor.fetchall()]
            for p in projects:
                cursor.execute("SELECT * FROM milestones WHERE project_id = ? ORDER BY due_date ASC;", (p["project_id"],))
                p["milestones"] = [dict(r) for r in cursor.fetchall()]

                cursor.execute("SELECT * FROM evaluations WHERE project_id = ? ORDER BY eval_id ASC;", (p["project_id"],))
                p["evaluations"] = [dict(r) for r in cursor.fetchall()]

                total_m = len(p["milestones"])
                comp_m = sum(1 for m in p["milestones"] if m["status"] == "Completed")
                p["progress_pct"] = round((comp_m / total_m * 100.0), 1) if total_m > 0 else 0.0
            data = projects

        elif path == "/api/skills":
            cursor.execute("""
            SELECT sk.skill_category, sk.skill_name, COUNT(ss.student_id) AS student_count
            FROM skills sk
            LEFT JOIN student_skills ss ON sk.skill_id = ss.skill_id
            GROUP BY sk.skill_id
            ORDER BY sk.skill_category, student_count DESC;
            """)
            data = [dict(r) for r in cursor.fetchall()]

        conn.close()

        if data is not None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data, default=str).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        """Handle CORS pre-flight requests."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len)
        try:
            payload = json.loads(body)
        except Exception:
            self.send_response(400)
            self.end_headers()
            return

        if path == "/api/register_student":
            self.handle_register_student(payload)
        elif path == "/api/assign_skill":
            self.handle_assign_skill(payload)
        else:
            self.send_response(404)
            self.end_headers()

    def handle_register_student(self, payload):
        """Insert a new student + their skills into the database."""
        s = payload.get("student", {})
        skills = payload.get("skills", [])
        db_path = get_db_path()
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO students
                  (student_id, name, email, department, class_name, section, batch_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                s.get("student_id"),
                s.get("name"),
                s.get("email"),
                s.get("department", "Information Technology"),
                s.get("class_name", "25IT3A"),
                s.get("section", "A"),
                s.get("batch_year", "2025-2029"),
            ))
            # Assign skills
            for sk in skills:
                cursor.execute("SELECT skill_id FROM skills WHERE skill_name = ?", (sk.get("skill_name"),))
                row = cursor.fetchone()
                if row:
                    skill_id = row[0]
                else:
                    cursor.execute(
                        "INSERT INTO skills (skill_name, skill_category) VALUES (?, ?)",
                        (sk.get("skill_name"), "General")
                    )
                    skill_id = cursor.lastrowid
                cursor.execute("""
                    INSERT OR IGNORE INTO student_skills (student_id, skill_id, proficiency_level)
                    VALUES (?, ?, ?)
                """, (s.get("student_id"), skill_id, sk.get("proficiency_level", "Intermediate")))
            conn.commit()
            conn.close()
            response = {"success": True, "message": f"Student {s.get('name')} registered successfully."}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        except Exception as ex:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": str(ex)}).encode("utf-8"))

    def handle_assign_skill(self, payload):
        """Assign a skill to an existing student."""
        student_id = payload.get("student_id")
        skill_name = payload.get("skill_name")
        proficiency = payload.get("proficiency_level", "Intermediate")
        db_path = get_db_path()
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT skill_id FROM skills WHERE skill_name = ?", (skill_name,))
            row = cursor.fetchone()
            if row:
                skill_id = row[0]
            else:
                cursor.execute("INSERT INTO skills (skill_name, skill_category) VALUES (?, ?)", (skill_name, "General"))
                skill_id = cursor.lastrowid
            cursor.execute("""
                INSERT OR IGNORE INTO student_skills (student_id, skill_id, proficiency_level)
                VALUES (?, ?, ?)
            """, (student_id, skill_id, proficiency))
            conn.commit()
            conn.close()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "message": "Skill assigned."}).encode("utf-8"))
        except Exception as ex:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": str(ex)}).encode("utf-8"))

class ReusableThreadingServer(ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True

def run_server():
    server_address = ("", PORT)
    httpd = ReusableThreadingServer(server_address, TrackingRequestHandler)
    print("=" * 75)
    print("  VCET IT :: STUDENT PROJECT & SKILL TRACKING WEB PORTAL")
    print("  Student: Abhishek.R (732925ITR002) - Class: 25IT3A")
    print(f"  Server listening at: http://localhost:{PORT}")
    print("  Mode: High-Performance Multi-Threaded HTTP Server")
    print("=" * 75)
    webbrowser.open(f"http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Web server shut down gracefully.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
