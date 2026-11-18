# SYSTEM DESIGN & ARCHITECTURE DOCUMENT
## Student Project and Skill Tracking System

---

**Institution:** Velalar College of Engineering and Technology (Autonomous), Erode - 638012  
**Department:** Department of Information Technology  
**Academic Year:** 2026 - 27 (ODD Semester) | **Class:** 25IT3A&B  
**Author / Student Name:** Abhishek.R  
**Register Number:** 732925ITR002  
**Class & Section:** 25IT3A (Section A)  
**Course Code & Title:** 25ITT33 - Software Engineering  

---

## 1. System Architecture Design

The system implements a decoupled, 3-tier enterprise architecture ensuring separation of concerns, high maintainability, and data security:

```mermaid
graph TD
    subgraph Presentation_Layer ["Presentation & Interaction Layer"]
        CLI["Java Console CLI Interface (Main.java)"]
        PY_NOTEBOOK["Jupyter Notebook (data_analysis.ipynb)"]
    end

    subgraph Business_Logic_Layer ["Business Logic & Service Layer"]
        TRACK_SVC["TrackingService.java"]
        REP_GEN["ReportGenerator.java"]
        PY_ANALYTICS["Python Data Science Pipeline (data_retrieval_and_analysis.py)"]
        PY_VIS["Visualization Engine (generate_visualizations.py)"]
    end

    subgraph Data_Access_Layer ["Data Access & Persistence Layer (DAO)"]
        DB_CONN["DatabaseConnection.java (JDBC Singleton)"]
        STU_DAO["StudentDAO.java"]
        PROJ_DAO["ProjectDAO.java"]
        EVAL_DAO["EvaluationDAO.java"]
        PY_SQLITE["Python sqlite3 Connector"]
    end

    subgraph Storage_Layer ["Relational Storage Layer"]
        DB[("SQLite / MySQL Database (tracking_system.db)")]
        CSV_STORE[("Clean CSV Datasets")]
        CHART_STORE[("High-Resolution PNG Visualizations")]
    end

    CLI --> TRACK_SVC
    CLI --> REP_GEN
    TRACK_SVC --> STU_DAO
    TRACK_SVC --> PROJ_DAO
    TRACK_SVC --> EVAL_DAO

    STU_DAO --> DB_CONN
    PROJ_DAO --> DB_CONN
    EVAL_DAO --> DB_CONN
    DB_CONN --> DB

    PY_NOTEBOOK --> PY_SQLITE
    PY_ANALYTICS --> PY_SQLITE
    PY_VIS --> PY_SQLITE
    PY_SQLITE --> DB

    PY_ANALYTICS --> CSV_STORE
    PY_VIS --> CHART_STORE
```

### Architectural Tier Breakdown
1. **Presentation Layer:**
   - Provides user interactions through a structured menu with ANSI formatting.
   - Accepts user commands, validates immediate formats, and delegates processing to service classes.
2. **Business Logic Layer:**
   - Enforces academic validation rules, automated milestone generation, skill gap detection, and progress metric computation.
   - The Python component performs data wrangling, descriptive statistics, and chart generation.
3. **Data Access Layer (DAO Pattern):**
   - Encapsulates all SQL statement executions, connection lifecycle management, and Object-Relational mapping (`ResultSet` to Java POJOs).
4. **Relational Storage Layer:**
   - Enforces relational constraints (PK, FK, CHECK constraints, Unique indexes).

---

## 2. Use Case Modeling

### 2.1 Use Case Diagram

```mermaid
flowchart LR
    Student(["Student"])
    Faculty(["Faculty Reviewer"])
    HoD(["Head of Department / Coordinator"])
    Admin(["System Administrator"])

    subgraph Tracking_System ["Student Project and Skill Tracking System"]
        UC1(["UC-01: Register Student Profile & Skills"])
        UC2(["UC-02: Submit Project Proposal"])
        UC3(["UC-03: View Project Dossier & Milestones"])
        UC4(["UC-04: Update Milestone Submission Status"])
        UC5(["UC-05: Record Component Evaluation Marks"])
        UC6(["UC-06: Perform Skill Gap Analysis"])
        UC7(["UC-07: Generate Department Progress Dashboard"])
        UC8(["UC-08: Execute Python EDA & Visualizations"])
        UC9(["UC-09: Maintain Master Skill Taxonomy"])
    end

    Student --> UC1
    Student --> UC2
    Student --> UC3

    Faculty --> UC4
    Faculty --> UC5
    Faculty --> UC6

    HoD --> UC3
    HoD --> UC6
    HoD --> UC7
    HoD --> UC8

    Admin --> UC9
```

### 2.2 Detailed Use Case Specifications

#### Use Case UC-02: Submit Project Proposal
* **Primary Actor:** Student
* **Pre-conditions:** Student must be registered in the system with a valid Register Number.
* **Main Success Scenario:**
  1. Student selects "Register New Student Project" from the menu.
  2. System prompts for Register Number, Title, Domain, Abstract, and Technologies Used.
  3. System verifies student existence in the database.
  4. System validates that the selected domain is an approved engineering domain.
  5. System records project record with initial status `In Progress`.
  6. System automatically provisions 5 standard academic milestones with scheduled deadlines.
  7. System displays success confirmation and assigned Project ID.
* **Post-conditions:** Project and 5 milestones are committed in the database.

#### Use Case UC-05: Record Component Evaluation Marks
* **Primary Actor:** Faculty Reviewer / HoD
* **Pre-conditions:** Project must exist in the database.
* **Main Success Scenario:**
  1. Faculty inputs Project ID.
  2. System displays current project details and milestone progress.
  3. Faculty selects component (Review 1, Review 2, Code Quality, Testing, Viva).
  4. Faculty inputs obtained marks, faculty name, and remarks.
  5. System validates: $0 \le \text{Obtained Marks} \le \text{Max Marks}$.
  6. System stores evaluation record and updates aggregate project performance.
* **Post-conditions:** Evaluation marks are logged and available for report generation.

---

## 3. Class Diagram (Object-Oriented Modeling)

The class diagram demonstrates clean adherence to **25ITT32 (Java Programming)** principles: encapsulation with private fields, typed collections, separation of concerns using the DAO design pattern, and cohesive service orchestration.

```mermaid
classDiagram
    class Student {
        -String studentId
        -String name
        -String email
        -String department
        -String className
        -String section
        -String batchYear
        -List~Skill~ skills
        +getStudentId() String
        +getName() String
        +getEmail() String
        +getSkills() List~Skill~
        +addSkill(Skill) void
        +toString() String
    }

    class Skill {
        -int skillId
        -String skillName
        -String category
        -String proficiency
        +getSkillId() int
        +getSkillName() String
        +getCategory() String
        +getProficiency() String
        +toString() String
    }

    class Project {
        -int projectId
        -String studentId
        -String studentName
        -String projectTitle
        -String domain
        -String description
        -String technologiesUsed
        -String status
        -String createdAt
        -List~Milestone~ milestones
        -List~Evaluation~ evaluations
        +calculateTotalMarks() double
        +getCompletionPercentage() double
        +addMilestone(Milestone) void
        +addEvaluation(Evaluation) void
    }

    class Milestone {
        -int milestoneId
        -int projectId
        -String milestoneName
        -String dueDate
        -String submissionDate
        -String status
        +getMilestoneId() int
        +getStatus() String
        +setStatus(String) void
    }

    class Evaluation {
        -int evalId
        -int projectId
        -String componentName
        -double maxMarks
        -double obtainedMarks
        -String evaluatorName
        -String evaluationDate
        -String comments
        +getObtainedMarks() double
        +getMaxMarks() double
    }

    class DatabaseConnection {
        -String databaseUrl$
        +getConnection()$ Connection
        +closeConnection()$ void
    }

    class StudentDAO {
        +getAllStudents() List~Student~
        +getStudentById(String) Student
        +addStudent(Student) boolean
        +getSkillsForStudent(String) List~Skill~
        +addSkillToStudent(String, int, String) boolean
    }

    class ProjectDAO {
        +getAllProjects() List~Project~
        +getProjectsByDomain(String) List~Project~
        +getProjectsByStatus(String) List~Project~
        +getProjectById(int) Project
        +addProject(Project) int
        +updateMilestoneStatus(int, String, String) boolean
    }

    class EvaluationDAO {
        +getEvaluationsByProjectId(int) List~Evaluation~
        +addEvaluation(Evaluation) boolean
        +getOverallSummary() Map~String, Object~
    }

    class TrackingService {
        -StudentDAO studentDAO
        -ProjectDAO projectDAO
        -EvaluationDAO evaluationDAO
        +registerStudent(...) boolean
        +registerProjectWithDefaultMilestones(...) int
        +updateMilestone(...) boolean
        +recordEvaluation(...) boolean
        +analyzeSkillGaps(int) List~String~
    }

    class ReportGenerator {
        +printStudentsTable(List~Student~)$ void
        +printProjectsTable(List~Project~)$ void
        +printProjectFullReport(Project, List~String~)$ void
        +printDepartmentSummary(Map)$ void
    }

    Student "1" *-- "0..*" Skill : possesses
    Project "1" *-- "0..*" Milestone : tracks
    Project "1" *-- "0..*" Evaluation : assesses
    Student "1" -- "0..*" Project : authors
    TrackingService --> StudentDAO
    TrackingService --> ProjectDAO
    TrackingService --> EvaluationDAO
    StudentDAO ..> DatabaseConnection
    ProjectDAO ..> DatabaseConnection
    EvaluationDAO ..> DatabaseConnection
```

---

## 4. Sequence Diagrams

### 4.1 Project Registration & Milestone Attachment Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Student / Faculty
    participant Main as Main (CLI)
    participant Svc as TrackingService
    participant SDAO as StudentDAO
    participant PDAO as ProjectDAO
    participant DB as SQLite Database

    User->>Main: Enter Project Details (RegNo, Title, Domain, Tech)
    Main->>Svc: registerProjectWithDefaultMilestones(...)
    Svc->>SDAO: getStudentById(regNo)
    SDAO->>DB: SELECT * FROM students WHERE student_id = ?
    DB-->>SDAO: Student Record Found
    SDAO-->>Svc: Student Object Returned
    Svc->>PDAO: addProject(Project)
    PDAO->>DB: INSERT INTO projects (...)
    DB-->>PDAO: Generated Project ID = 1
    PDAO-->>Svc: Project ID = 1
    loop 5 Standard Milestones
        Svc->>PDAO: addMilestone(Milestone)
        PDAO->>DB: INSERT INTO milestones (...)
    end
    Svc-->>Main: Success (Project ID: 1)
    Main-->>User: Display Confirmation & Scheduled Milestones
```

### 4.2 Component Evaluation & Scoring Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Fac as Faculty Evaluator
    participant Main as Main (CLI)
    participant Svc as TrackingService
    participant EDAO as EvaluationDAO
    participant PDAO as ProjectDAO
    participant DB as SQLite Database

    Fac->>Main: Select "Record Evaluation" (ProjID: 1, Review 1, 19.5/20)
    Main->>Svc: recordEvaluation(1, 'Review 1', 20.0, 19.5, 'Dr. Murugesan', 'Exemplary')
    Svc->>Svc: Validate Marks (0 <= 19.5 <= 20.0)
    Svc->>EDAO: addEvaluation(Evaluation)
    EDAO->>DB: INSERT INTO evaluations (...)
    DB-->>EDAO: 1 row affected
    EDAO-->>Svc: true
    Svc-->>Main: Success
    Main->>PDAO: getProjectById(1)
    PDAO->>DB: SELECT * FROM projects WHERE project_id = 1
    DB-->>PDAO: Project Data
    PDAO-->>Main: Project Object
    Main-->>Fac: Display Updated Dossier & Aggregate Marks (96.5%)
```

---

## 5. State Transition Model for Project Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Proposed : Proposal Submitted
    Proposed --> In_Progress : Proposal Approved & Team Assigned
    In_Progress --> Under_Review : Core Milestones Completed
    Under_Review --> In_Progress : Revision Requested by Reviewer
    Under_Review --> Completed : Final Viva Cleared & Code Accepted
    Completed --> [*] : Archived in Department Repository
```
