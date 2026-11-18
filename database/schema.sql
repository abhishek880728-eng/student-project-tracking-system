-- ============================================================================
-- Velalar College of Engineering and Technology, Erode - 12
-- Department of Information Technology
-- Academic Year: 2026-27 (ODD) | Class: 25IT3A&B
-- Activity: Project-Based Assessment
-- Student Name: Abhishek.R | Register No: 732925ITR002 | Class: 25IT3A (Sec A)
-- Scenario 2: Student Project and Skill Tracking System
-- ============================================================================
-- Database Schema Definition (SQLite & MySQL Compatible DDL)
-- Meets 3NF/BCNF Normalization Standards
-- ============================================================================

-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department VARCHAR(50) NOT NULL DEFAULT 'Information Technology',
    class_name VARCHAR(20) NOT NULL DEFAULT '25IT3A',
    section VARCHAR(5) NOT NULL DEFAULT 'A',
    batch_year VARCHAR(15) NOT NULL DEFAULT '2025-2029'
);

-- 2. Technical Skills Master Table
CREATE TABLE IF NOT EXISTS skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name VARCHAR(50) NOT NULL UNIQUE,
    skill_category VARCHAR(50) NOT NULL CHECK (skill_category IN ('Programming Language', 'Database', 'Framework / Web', 'AI / ML', 'DevOps / Tools', 'Mobile App'))
);

-- 3. Student Skills Mapping Table (Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS student_skills (
    student_id VARCHAR(20) NOT NULL,
    skill_id INTEGER NOT NULL,
    proficiency_level VARCHAR(20) NOT NULL CHECK (proficiency_level IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    PRIMARY KEY (student_id, skill_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);

-- 4. Student Projects Table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id VARCHAR(20) NOT NULL,
    project_title VARCHAR(200) NOT NULL,
    domain VARCHAR(100) NOT NULL CHECK (domain IN ('Artificial Intelligence', 'Web Development', 'Internet of Things', 'Cloud Computing', 'Cybersecurity', 'Data Science', 'Mobile Applications')),
    description TEXT NOT NULL,
    technologies_used VARCHAR(250) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'In Progress' CHECK (status IN ('Proposed', 'In Progress', 'Under Review', 'Completed')),
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- 5. Project Milestones Table
CREATE TABLE IF NOT EXISTS milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    milestone_name VARCHAR(100) NOT NULL,
    due_date DATE NOT NULL,
    submission_date DATE,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK (status IN ('Pending', 'In Progress', 'Completed', 'Delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- 6. Project Component Evaluation Marks Table
CREATE TABLE IF NOT EXISTS evaluations (
    eval_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    component_name VARCHAR(100) NOT NULL CHECK (component_name IN ('Review 1 - Problem & Design', 'Review 2 - Implementation', 'Code Quality & Git', 'Testing & Verification', 'Final Presentation & Viva')),
    max_marks REAL NOT NULL DEFAULT 20.0,
    obtained_marks REAL NOT NULL CHECK (obtained_marks >= 0 AND obtained_marks <= max_marks),
    evaluator_name VARCHAR(100) NOT NULL,
    evaluation_date DATE NOT NULL DEFAULT CURRENT_DATE,
    comments TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Indexes for Query Optimization
CREATE INDEX IF NOT EXISTS idx_student_email ON students(email);
CREATE INDEX IF NOT EXISTS idx_project_student ON projects(student_id);
CREATE INDEX IF NOT EXISTS idx_project_domain ON projects(domain);
CREATE INDEX IF NOT EXISTS idx_project_status ON projects(status);
CREATE INDEX IF NOT EXISTS idx_milestone_project ON milestones(project_id);
CREATE INDEX IF NOT EXISTS idx_eval_project ON evaluations(project_id);
