# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
## Student Project and Skill Tracking System

---

**Institution:** Velalar College of Engineering and Technology (Autonomous), Erode - 638012  
**Department:** Department of Information Technology  
**Academic Year:** 2026 - 27 (ODD Semester)  
**Class:** 25IT3A & 25IT3B | **Semester:** III  
**Activity:** Project-Based Assessment  
**Assigned Problem:** Scenario 2 — Student Project and Skill Tracking System  
**Author / Student Name:** Abhishek.R  
**Register Number:** 732925ITR002  
**Class & Section:** 25IT3A (Section A)  
**Course Code & Title:** 25ITT33 - Software Engineering  

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) establishes the complete functional and non-functional requirements for the **Student Project and Skill Tracking System**. The system replaces uncoordinated and error-prone spreadsheet-based project monitoring by providing a centralized database, a modular Java application for project lifecycle management, and a Python analytics pipeline for departmental reporting and skill gap detection.

### 1.2 Scope of the System
The system encompasses:
1. Maintaining a database of student academic profiles, technical proficiencies, and programming competencies.
2. Registering individual mini-projects with defined titles, engineering domains, abstracts, and technology stacks.
3. Structuring and monitoring academic project milestones (SRS, UML Design, Implementation, Verification, Final Viva) with deadline auditing.
4. Logging rubric-based continuous evaluation marks across five defined assessment components.
5. Performing automated skill gap analysis by comparing project technology stacks against student skill repositories.
6. Supplying datasets to a Python data science module for descriptive analytics and visual reporting.

### 1.3 Definitions, Acronyms, and Abbreviations
* **SRS:** Software Requirements Specification
* **VCET:** Velalar College of Engineering and Technology
* **DBMS:** Database Management System
* **JDBC:** Java Database Connectivity
* **CLI:** Command Line Interface
* **DAO:** Data Access Object
* **EDA:** Exploratory Data Analysis
* **3NF / BCNF:** Third Normal Form / Boyce-Codd Normal Form
* **BVA:** Boundary Value Analysis
* **EP:** Equivalence Partitioning

### 1.4 References
1. IEEE Standard 830-1998: *Recommended Practice for Software Requirements Specifications*.
2. Pressman, R. S., *Software Engineering: A Practitioner's Approach*, 9th Edition, McGraw-Hill.
3. Elmasri, R., & Navathe, S. B., *Fundamentals of Database Systems*, 7th Edition, Pearson.
4. VCET Curriculum & Syllabi: 25ITT33 (SE), 25ITT31 (DBMS), 25ITT32 (Java), 25ITC31 (FDS).

---

## 2. Overall Description

### 2.1 Product Perspective
The Student Project and Skill Tracking System is a dedicated departmental information system designed to integrate with the existing academic framework of VCET IT. It operates on a multi-tier architectural model:
- **Presentation Layer:** Menu-driven Java CLI offering clear prompts, input validation, and formatted tables.
- **Application & Logic Layer:** Java service classes executing validation rules, progress scoring, milestone tracking, and skill gap identification.
- **Persistence Layer:** Normalized SQLite/MySQL relational database enforcing foreign key constraints and transactional integrity.
- **Analytics & Reporting Layer:** Python data science pipeline extracting data via SQL and generating visualizations using Matplotlib.

### 2.2 User Classes and Characteristics
1. **Student:** Enters personal project proposals, associates utilized technologies, and views milestone deadlines.
2. **Faculty Reviewer / Evaluator:** Evaluates project progress across scheduled reviews, scores individual assessment components (max 20 marks each), and provides written remarks.
3. **Head of Department (HoD) / Academic Coordinator:** Views department-wide progress dashboards, monitors domain distributions, and inspects skill gap metrics to plan technical training.
4. **System Administrator:** Oversees database backups, user accounts, and master skill taxonomy.

### 2.3 Operating Environment
* **Operating System:** Windows 10/11, Linux (Ubuntu 20.04+), or macOS
* **Runtime Environment:** Java Development Kit (JDK 17 or higher, verified on JDK 26)
* **Database Engine:** SQLite 3.x (with zero-configuration local serverless file storage) / MySQL 8.0
* **Data Science Engine:** Python 3.10+ with `sqlite3` and `matplotlib`

### 2.4 Design and Implementation Constraints
1. Must adhere strictly to object-oriented programming principles (encapsulation, abstraction, inheritance, polymorphism).
2. Database schema must achieve at least 3NF normalization without partial or transitive dependencies.
3. Database access must strictly employ parameterized `PreparedStatement` to prevent SQL injection vulnerabilities.
4. Must operate reliably offline without mandatory external cloud dependencies.

---

## 3. Specific System Requirements

### 3.1 Functional Requirements

#### FR-01: Student Profile & Skill Management
* **FR-01.1:** The system shall maintain student records comprising Register Number (Primary Key), Full Name, Institutional Email, Department, Class Name, Section, and Batch Year.
* **FR-01.2:** The system shall maintain a master catalog of technical skills categorized into Programming Languages, Databases, Web Frameworks, AI/ML, DevOps/Tools, and Mobile App Development.
* **FR-01.3:** The system shall allow students to associate multiple skills with proficiency levels: *Beginner*, *Intermediate*, *Advanced*, or *Expert*.

#### FR-02: Project Registration & Categorization
* **FR-02.1:** The system shall permit students to register individual mini-projects with a Project Title, Engineering Domain, Abstract/Description, and comma-separated Technologies Used.
* **FR-02.2:** The system shall validate that the selected domain belongs to accredited departmental areas: *Artificial Intelligence*, *Web Development*, *Internet of Things*, *Cloud Computing*, *Cybersecurity*, *Data Science*, or *Mobile Applications*.
* **FR-02.3:** Upon registration, the project status shall default to *In Progress* or *Proposed*, and a unique numerical Project ID shall be assigned.

#### FR-03: Milestone Tracking & Scheduling
* **FR-03.1:** The system shall automatically attach five standard academic milestones upon project creation:
  1. SRS & Requirements Specification
  2. UML System Design & Database Schema
  3. Core Module Implementation
  4. Verification, Testing & GitHub Docs
  5. Final Presentation & Project Viva
* **FR-03.2:** The system shall record target due dates, actual submission dates, and lifecycle statuses (*Pending*, *In Progress*, *Completed*, *Delayed*).
* **FR-03.3:** The system shall compute an active project completion percentage dynamically:
  $$\text{Completion Rate (\%)} = \left( \frac{\text{Completed Milestones}}{\text{Total Assigned Milestones}} \right) \times 100$$

#### FR-04: Rubric-Based Component Evaluation
* **FR-04.1:** The system shall record evaluation scores for five distinct assessment components:
  1. Review 1 - Problem & Design (Max: 20 marks)
  2. Review 2 - Implementation (Max: 20 marks)
  3. Code Quality & Git (Max: 20 marks)
  4. Testing & Verification (Max: 20 marks)
  5. Final Presentation & Viva (Max: 20 marks)
* **FR-04.2:** The system shall validate that obtained marks satisfy $0 \le \text{Obtained Marks} \le \text{Max Marks}$.
* **FR-04.3:** The system shall record evaluator name, evaluation date, and textual faculty feedback.

#### FR-05: Skill Gap Identification & Analytics
* **FR-05.1:** The system shall compare the declared technology stack of a project against the student's registered competencies.
* **FR-05.2:** Any required technology lacking an associated proficiency record shall be flagged as an identified skill gap.

#### FR-06: Python Data Retrieval & Wrangling
* **FR-06.1:** The Python pipeline shall connect to the relational database using standard database adapters.
* **FR-06.2:** The pipeline shall query joined datasets and compute descriptive statistics (mean, median, variance, standard deviation).
* **FR-06.3:** The pipeline shall export clean, preprocessed CSV datasets for departmental audits.

#### FR-07: Data Visualization Engine
* **FR-07.1:** The system shall generate publication-quality visual charts depicting:
  1. Overall project completion rates and lifecycle status distributions (Donut & Progress charts).
  2. Frequency rankings of popular student technology stacks (Horizontal Bar chart).
  3. Technical skill counts grouped by category and proficiency level (Grouped Bar chart).
  4. Domain-wise mean evaluation marks with department quality target baselines.

---

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
* **Response Time:** CLI queries and database operations shall execute in under 200 milliseconds.
* **Data Retrieval:** Python analysis scripts shall retrieve and process up to 10,000 project records in under 2 seconds.

### 4.2 Security Requirements
* **Data Integrity:** All foreign key constraints (`ON DELETE CASCADE`) and table-level `CHECK` constraints are strictly enforced.
* **SQL Injection Prevention:** All SQL statements in Java and Python must use parameterized bindings (`?`).

### 4.3 Reliability and Availability
* **Availability:** As a standalone embedded system, it operates with 99.9% uptime with zero external server dependency.
* **Fault Tolerance:** Robust exception handling traps invalid inputs (e.g., non-numeric IDs, invalid dates) without application termination.

### 4.4 Portability & Maintainability
* **Portability:** Code is cross-platform across Windows, Linux, and macOS platforms.
* **Maintainability:** Modular package architecture (`model`, `dao`, `service`, `Main`) facilitates effortless enhancements (such as migrating from SQLite to MySQL or adding a Web/GUI front-end).
