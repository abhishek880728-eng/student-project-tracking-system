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

---

## 6. UML 2.0 Component Diagram

The UML Component Diagram models the modular runtime organization and wiring of the **Student Project and Skill Tracking System**, conforming to IEEE/ISO component-based software engineering standards.

![UML 2.0 Component Diagram](diagrams/component_diagram.png)

### 6.1 Component & Interface Specification Table

| Element Type | Notation & Symbol | Identifier | Role & Function in System |
|:---|:---|:---|:---|
| **Subsystem Container** | `<<component>>` Large Rectangle | `Student Project Tracking System` | Encapsulates internal business logic and hides implementation details from external actors. |
| **Central Core Component** | `<<component>>` Center Box | `ProjectTrackingEngine` | Coordinates project proposals, milestone validation, evaluation computations, and data queries. |
| **Auxiliary Component** | `<<component>>` Top-Right Box | `Student & Faculty Module` | Manages student profiles, technical skills taxonomy, faculty mentor allocations, and user roles. |
| **Auxiliary Component** | `<<component>>` Bottom-Left Box | `SkillGapAnalyzer` | Detects deficiencies between student proficiency levels and required project tech stacks. |
| **Auxiliary Component** | `<<component>>` Bottom-Right Box | `MilestoneScheduler` | Provisions 5 default academic milestones and computes completion percentages. |
| **Boundary Port** | Small Square `[ ]` on Border | `Port (Left & Right)` | Explicit interaction point mediating communication between external interfaces and internal logic. |
| **Provided Interface** | Lollipop / Ball `—(O)` | `Student Profile`, `Project Details`, `Evaluation Rubrics` | Services, APIs, and data models supplied by the system for clients, students, and faculty. |
| **Required Interface** | Socket / Arc `—(C)` | `Account / DBMS Auth`, `Project ID / Audit Record` | Services demanded by the system from external subsystems (e.g., SQLite engine, PDF export engine). |
| **Assembly Connector** | Ball-and-Socket `—(O—(C—` | `Faculty Guide`, `Milestones`, `Defect/Gap details`, `User Role` | Runtime binding linking a provided interface of one component directly to the required interface of another. |

### 6.2 Component Wiring & Data Flow (Mermaid Equivalent)

```mermaid
graph LR
    subgraph System_Container ["<<component>> Student Project Tracking System"]
        subgraph Ports_In ["Inbound Boundary Ports"]
            P1["Port: Student Profile"]
            P2["Port: Project Proposal"]
            P3["Port: Evaluation Rubrics"]
        end

        Core["<<component>>\nProjectTrackingEngine"]
        Staff["<<component>>\nStudent & Faculty Module"]
        Defect["<<component>>\nSkillGapAnalyzer"]
        MapMod["<<component>>\nMilestoneScheduler"]

        subgraph Ports_Out ["Outbound Boundary Ports"]
            P4["Port: DBMS Persistence"]
            P5["Port: Audit & PDF Export"]
        end

        P1 --> Core
        P2 --> Core
        P3 --> Defect
        Core <--> Staff
        Core <--> MapMod
        Core <--> Defect
        Staff --> P4
        Core --> P5
    end

    Ext_Student(["Provided: Student Profile API"]) --- P1
    Ext_Project(["Provided: Project Proposal API"]) --- P2
    Ext_Eval(["Provided: Evaluation Marks API"]) --- P3

    P4 --- Ext_DB(["Required: SQLite / MySQL Storage"])
    P5 --- Ext_Report(["Required: PDF Audit Report Engine"])
```

---

## 7. UML 2.0 Activity Diagram

The UML Activity Diagram defines the parallel control flow and business process logic governing **Project Registration & Evaluation Workflow**, utilizing concurrent fork-join synchronization, conditional branch guards, and activity final termination.

![UML 2.0 Activity Diagram](diagrams/activity_diagram.png)

### 7.1 Workflow State & Decision Logic Breakdown

1. **Initial Node (`●`):** The workflow initiates when a student submits a new mini-project proposal.
2. **Action State (`Receive Project Proposal`):** The system parses student credentials, project title, domain classification, abstract, and declared tech stack.
3. **Synchronization Fork Bar (Thick Horizontal Bar):** The execution thread branches concurrently into two independent parallel processing pipelines:
   - **Branch 1: Technical Stack & Competency Verification:**
     - **Action (`Verify Tech Stack & Skills`):** Queries student's recorded competencies against the declared technologies.
     - **Decision Diamond (`Condition Check`):**
       - `[skill gap found]`: Routes to **`Flag Remedial Mentoring`**, alerting the faculty mentor and scheduling tutorial milestones.
       - `[skills verified]`: Routes to **`Approve Technical Feasibility`**, confirming direct competency alignment.
     - **Merge Diamond:** Merges the conditional pathways back into a unified technical approval status.
   - **Branch 2: Academic Governance & Milestone Setup:**
     - **Action (`Auto-Provision 5 Academic Milestones`):** Generates standard academic deliverables (SRS, UML Design, Implementation, Analytics, Final Viva) with due dates.
     - **Action (`Assign Faculty Review Committee`):** Maps departmental evaluators and assigns assessment rubrics.
4. **Synchronization Join Bar (Thick Horizontal Bar):** Waits for both the technical competency analysis and the administrative milestone scheduling to complete successfully.
5. **Activity Final Node (`◉` Bullseye):** Commits the project record into `database/tracking_system.db`, marks initial status as `In Progress`, and issues confirmation to the student.

### 7.2 Activity Flow Modeling (Mermaid Equivalent)

```mermaid
flowchart TD
    Start(("●")) --> Recv["Receive Project Proposal"]
    Recv --> ForkBar["═══════════════════════════════════\n[Synchronization Fork Bar]\n═══════════════════════════════════"]

    %% Left Parallel Branch: Technical Analysis & Gap Check
    ForkBar --> Verify["Verify Tech Stack & Skills"]
    Verify --> Decision{"Skill Assessment"}
    Decision -->|"[skill gap found]"| Remedial["Flag Remedial Mentoring"]
    Decision -->|"[skills verified]"| Feasible["Approve Technical Feasibility"]
    Remedial --> MergeNode{" "}
    Feasible --> MergeNode{" "}

    %% Right Parallel Branch: Administrative Governance & Milestones
    ForkBar --> Milestones["Auto-Provision 5 Academic Milestones"]
    Milestones --> AssignFac["Assign Faculty Review Committee"]

    %% Synchronization Join
    MergeNode --> JoinBar["═══════════════════════════════════\n[Synchronization Join Bar]\n═══════════════════════════════════"]
    AssignFac --> JoinBar

    JoinBar --> EndNode((("◉")))
```

