# SOFTWARE PROJECT METRICS & LINES OF CODE (LOC) AUDIT REPORT

**Institution:** Velalar College of Engineering and Technology (Autonomous), Erode - 12  
**Department:** Department of Information Technology | **Class:** 25IT3A (Section A)  
**Course Code & Title:** 25ITT33 - Software Engineering (**Unit 5: Project Management & Metrics**)  
**Student Name:** Abhishek.R | **Register Number:** 732925ITR002  
**Activity:** Project-Based Assessment - Scenario 2 (Student Project and Skill Tracking System)  

---

## 1. Executive Summary: Lines of Code (LOC) Breakdown

| Category / Technology | Files | Total LOC | Source Code (SLOC) | Comments (CLOC) | Blank Lines |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Java** | 12 | 1,487 | 1,221 | 62 | 204 |
| **Web / HTML / JS** | 2 | 1,446 | 1,282 | 48 | 116 |
| **Documentation (Markdown)** | 6 | 1,189 | 981 | 0 | 208 |
| **Python** | 5 | 947 | 436 | 376 | 135 |
| **Data / Config (JSON, CSV)** | 4 | 338 | 338 | 0 | 0 |
| **SQL** | 2 | 254 | 190 | 41 | 23 |
| **Batch Scripts** | 5 | 105 | 89 | 0 | 16 |
| **GRAND TOTAL** | **36** | **5,766** | **4,537** | **527** | **702** |

---

## 2. Software Engineering Estimation & COCOMO Analysis (Unit 5)

* **Total Project Scale:** `5,766` total lines across `36` files (`5.766` KLOC).
* **Core Executable Source Code:** `3,129` lines (`3.129` KLOC) across Java, Python, SQL, and Web frontend.
* **Documentation Density:** `527` lines of technical commentary and structured markdown.
* **Basic COCOMO Effort Estimation:**
  $$\text{Effort} = 2.4 \times (\text{KLOC})^{1.05} = 2.4 \times (3.129)^{1.05} \approx 7.95 \text{ Person-Months}$$
* **Development Duration Estimation:**
  $$\text{Duration} = 2.5 \times (\text{Effort})^{0.38} = 2.5 \times (7.95)^{0.38} \approx 5.50 \text{ Months}$$
* **Recommended Staff Size:** `1.45` developer(s) (optimally suited for a single student mini-project).

---

## 3. Detailed File-Level Line Count Matrix

| Relative File Path | Language | Total Lines | Code (SLOC) | Comments | Blank |
|:---|:---|:---:|:---:|:---:|:---:|
| `java_app\src\com\vcet\tracking\Main.java` | Java | 381 | 309 | 17 | 55 |
| `java_app\src\com\vcet\tracking\dao\ProjectDAO.java` | Java | 221 | 196 | 3 | 22 |
| `java_app\src\com\vcet\tracking\service\TrackingService.java` | Java | 159 | 128 | 8 | 23 |
| `java_app\src\com\vcet\tracking\dao\StudentDAO.java` | Java | 143 | 129 | 3 | 11 |
| `java_app\src\com\vcet\tracking\service\ReportGenerator.java` | Java | 114 | 100 | 3 | 11 |
| `java_app\src\com\vcet\tracking\dao\EvaluationDAO.java` | Java | 99 | 86 | 3 | 10 |
| `java_app\src\com\vcet\tracking\model\Project.java` | Java | 95 | 72 | 4 | 19 |
| `java_app\src\com\vcet\tracking\model\Student.java` | Java | 65 | 47 | 5 | 13 |
| `java_app\src\com\vcet\tracking\model\Evaluation.java` | Java | 59 | 44 | 3 | 12 |
| `java_app\src\com\vcet\tracking\dao\DatabaseConnection.java` | Java | 57 | 41 | 7 | 9 |
| `java_app\src\com\vcet\tracking\model\Milestone.java` | Java | 48 | 35 | 3 | 10 |
| `java_app\src\com\vcet\tracking\model\Skill.java` | Java | 46 | 34 | 3 | 9 |
| `calculate_loc.py` | Python | 283 | 220 | 20 | 43 |
| `python_ds\generate_visualizations.py` | Python | 257 | 51 | 170 | 36 |
| `python_ds\data_retrieval_and_analysis.py` | Python | 194 | 66 | 104 | 24 |
| `web\server.py` | Python | 148 | 59 | 69 | 20 |
| `database\setup_database.py` | Python | 65 | 40 | 13 | 12 |
| `database\seed_data.sql` | SQL | 170 | 131 | 23 | 16 |
| `database\schema.sql` | SQL | 84 | 59 | 18 | 7 |
| `index.html` | Web / HTML / JS | 723 | 641 | 24 | 58 |
| `web\index.html` | Web / HTML / JS | 723 | 641 | 24 | 58 |
| `docs\SYSTEM_DESIGN.md` | Documentation (Markdown) | 360 | 308 | 0 | 52 |
| `README.md` | Documentation (Markdown) | 251 | 198 | 0 | 53 |
| `docs\DATABASE_DESIGN.md` | Documentation (Markdown) | 238 | 197 | 0 | 41 |
| `docs\SRS.md` | Documentation (Markdown) | 151 | 121 | 0 | 30 |
| `docs\TESTING_DOCUMENT.md` | Documentation (Markdown) | 112 | 90 | 0 | 22 |
| `docs\LOC_METRICS_REPORT.md` | Documentation (Markdown) | 77 | 67 | 0 | 10 |
| `push_to_github.bat` | Batch Scripts | 38 | 33 | 0 | 5 |
| `push_with_gh.bat` | Batch Scripts | 32 | 27 | 0 | 5 |
| `java_app\compile.bat` | Batch Scripts | 16 | 13 | 0 | 3 |
| `launch_website.bat` | Batch Scripts | 10 | 9 | 0 | 1 |
| `java_app\run.bat` | Batch Scripts | 9 | 7 | 0 | 2 |
| `python_ds\data_analysis.ipynb` | Data / Config (JSON, CSV) | 268 | 268 | 0 | 0 |
| `python_ds\clean_skills.csv` | Data / Config (JSON, CSV) | 31 | 31 | 0 | 0 |
| `python_ds\clean_evaluations.csv` | Data / Config (JSON, CSV) | 26 | 26 | 0 | 0 |
| `python_ds\clean_projects.csv` | Data / Config (JSON, CSV) | 13 | 13 | 0 | 0 |
