-- ============================================================================
-- Velalar College of Engineering and Technology, Erode - 12
-- Department of Information Technology | Class: 25IT3A&B
-- Seed Dataset for Student Project and Skill Tracking System
-- ============================================================================

-- Insert Master Skills
INSERT OR IGNORE INTO skills (skill_id, skill_name, skill_category) VALUES
(1, 'Java', 'Programming Language'),
(2, 'Python', 'Programming Language'),
(3, 'C++', 'Programming Language'),
(4, 'JavaScript', 'Programming Language'),
(5, 'SQL', 'Database'),
(6, 'MongoDB', 'Database'),
(7, 'React.js', 'Framework / Web'),
(8, 'Node.js', 'Framework / Web'),
(9, 'Spring Boot', 'Framework / Web'),
(10, 'TensorFlow / PyTorch', 'AI / ML'),
(11, 'Pandas / NumPy', 'AI / ML'),
(12, 'Docker', 'DevOps / Tools'),
(13, 'Git / GitHub', 'DevOps / Tools'),
(14, 'Flutter', 'Mobile App'),
(15, 'Kotlin', 'Mobile App');

-- Insert Students
INSERT OR IGNORE INTO students (student_id, name, email, department, class_name, section, batch_year) VALUES
('732925ITR002', 'Abhishek.R', 'abhishek.r@vcet.ac.in', 'Information Technology', '25IT3A', 'A', '2025-2029'),
('732925ITR032', 'Dharun Kumar.M', 'dharun.m@vcet.ac.in', 'Information Technology', '25IT3A', 'A', '2025-2029'),
('732925ITR062', 'Kavya.S', 'kavya.s@vcet.ac.in', 'Information Technology', '25IT3A', 'A', '2025-2029'),
('732925ITR092', 'Manojkumar.P', 'manojkumar.p@vcet.ac.in', 'Information Technology', '25IT3B', 'B', '2025-2029'),
('732925ITRL02', 'Naveen.K', 'naveen.k@vcet.ac.in', 'Information Technology', '25IT3B', 'B', '2025-2029'),
('732925ITR015', 'Ananya.V', 'ananya.v@vcet.ac.in', 'Information Technology', '25IT3A', 'A', '2025-2029'),
('732925ITR028', 'Bala Murugan.T', 'bala.t@vcet.ac.in', 'Information Technology', '25IT3A', 'A', '2025-2029'),
('732925ITR045', 'Gokul.N', 'gokul.n@vcet.ac.in', 'Information Technology', '25IT3A', 'A', '2025-2029'),
('732925ITR077', 'Priya.M', 'priya.m@vcet.ac.in', 'Information Technology', '25IT3B', 'B', '2025-2029'),
('732925ITR088', 'Rohit.S', 'rohit.s@vcet.ac.in', 'Information Technology', '25IT3B', 'B', '2025-2029'),
('732925ITR105', 'Sneha.R', 'sneha.r@vcet.ac.in', 'Information Technology', '25IT3B', 'B', '2025-2029'),
('732925ITR118', 'Vigneshwaran.A', 'vignesh.a@vcet.ac.in', 'Information Technology', '25IT3B', 'B', '2025-2029');

-- Insert Student Skills
INSERT OR IGNORE INTO student_skills (student_id, skill_id, proficiency_level) VALUES
('732925ITR002', 1, 'Advanced'),      -- Abhishek: Java
('732925ITR002', 2, 'Advanced'),      -- Abhishek: Python
('732925ITR002', 5, 'Intermediate'),  -- Abhishek: SQL
('732925ITR002', 11, 'Advanced'),     -- Abhishek: Pandas/NumPy
('732925ITR002', 13, 'Intermediate'), -- Abhishek: Git
('732925ITR032', 2, 'Intermediate'),  -- Dharun: Python
('732925ITR032', 7, 'Advanced'),      -- Dharun: React
('732925ITR032', 8, 'Intermediate'),  -- Dharun: Node
('732925ITR062', 1, 'Intermediate'),  -- Kavya: Java
('732925ITR062', 9, 'Intermediate'),  -- Kavya: Spring Boot
('732925ITR062', 5, 'Advanced'),      -- Kavya: SQL
('732925ITR092', 2, 'Advanced'),      -- Manoj: Python
('732925ITR092', 10, 'Advanced'),     -- Manoj: TensorFlow
('732925ITR092', 11, 'Advanced'),     -- Manoj: Pandas
('732925ITRL02', 14, 'Advanced'),     -- Naveen: Flutter
('732925ITRL02', 4, 'Intermediate'),  -- Naveen: JavaScript
('732925ITR015', 2, 'Intermediate'),  -- Ananya: Python
('732925ITR015', 10, 'Intermediate'), -- Ananya: AI/ML
('732925ITR028', 1, 'Advanced'),      -- Bala: Java
('732925ITR028', 5, 'Intermediate'),  -- Bala: SQL
('732925ITR045', 7, 'Advanced'),      -- Gokul: React
('732925ITR045', 6, 'Intermediate'),  -- Gokul: MongoDB
('732925ITR077', 2, 'Advanced'),      -- Priya: Python
('732925ITR077', 11, 'Advanced'),     -- Priya: Pandas
('732925ITR088', 12, 'Intermediate'), -- Rohit: Docker
('732925ITR088', 13, 'Advanced'),     -- Rohit: Git
('732925ITR105', 4, 'Advanced'),      -- Sneha: JS
('732925ITR105', 7, 'Intermediate'),  -- Sneha: React
('732925ITR118', 1, 'Intermediate'),  -- Vignesh: Java
('732925ITR118', 3, 'Advanced');      -- Vignesh: C++

-- Insert Projects
INSERT OR IGNORE INTO projects (project_id, student_id, project_title, domain, description, technologies_used, status, created_at) VALUES
(1, '732925ITR002', 'Student Project and Skill Tracking System', 'Data Science', 'Automated portal to monitor student mini-projects, track competencies, and perform descriptive/predictive analytics on skill gaps.', 'Java, Python, SQLite, Pandas, Matplotlib', 'Completed', '2026-08-10'),
(2, '732925ITR032', 'Campus Event Hub & Ticketing Platform', 'Web Development', 'Full-stack collaborative portal for managing inter-college symposium registrations and technical events.', 'React.js, Node.js, Express, MongoDB', 'Completed', '2026-08-12'),
(3, '732925ITR062', 'Automated Library Asset Management', 'Web Development', 'Enterprise inventory system with barcode scanning and fine calculation algorithms.', 'Java, Spring Boot, MySQL, Thymeleaf', 'In Progress', '2026-08-15'),
(4, '732925ITR092', 'Smart Crop Disease Detection using CNN', 'Artificial Intelligence', 'Deep learning computer vision model to identify leaf fungal infections in turmeric and paddy crops in Erode district.', 'Python, TensorFlow, OpenCV, Flask', 'Completed', '2026-08-18'),
(5, '732925ITRL02', 'VCET Bus Transport Tracking Mobile App', 'Mobile Applications', 'Real-time GPS bus fleet monitoring and route alerting app for rural commuting students.', 'Flutter, Dart, Firebase, Google Maps API', 'In Progress', '2026-08-20'),
(6, '732925ITR015', 'Customer Sentiment Analysis for E-Commerce', 'Data Science', 'NLP-driven aspect-based sentiment analyzer using TF-IDF and BERT embeddings on retail reviews.', 'Python, NLTK, Scikit-learn, Streamlit', 'Under Review', '2026-08-22'),
(7, '732925ITR028', 'Secure Healthcare Record Management System', 'Cybersecurity', 'Role-based access control and AES-256 encrypted electronic health records for medical clinics.', 'Java, Cryptography API, SQLite, JavaFX', 'In Progress', '2026-08-25'),
(8, '732925ITR045', 'IoT Smart Energy Metering & Power Leakage Alert', 'Internet of Things', 'ESP32 microcontroller power monitor sending live telemetry to cloud MQTT brokers.', 'C++, ESP-IDF, MQTT, Node-RED, Python', 'Completed', '2026-08-28'),
(9, '732925ITR077', 'Predictive Student Placement Analytics', 'Data Science', 'Machine learning classification pipeline predicting student placement chances based on academic CGPA and skills.', 'Python, Pandas, Seaborn, XGBoost', 'Completed', '2026-09-01'),
(10, '732925ITR088', 'Containerized Microservices CI/CD Pipeline', 'Cloud Computing', 'Automated DevOps workflow using Docker, Jenkins, and Kubernetes for scalable web workloads.', 'Docker, Kubernetes, GitHub Actions, Linux', 'Under Review', '2026-09-05'),
(11, '732925ITR105', 'Community Food Redistribution Network', 'Web Development', 'Hyperlocal platform connecting banquet halls with food banks to reduce organic wastage.', 'JavaScript, React, Node.js, PostgreSQL', 'In Progress', '2026-09-10'),
(12, '732925ITR118', 'Network Intrusion Detection System (NIDS)', 'Cybersecurity', 'Packet sniffing and anomalous network signature detection engine for departmental lab firewalls.', 'C++, Python, Scapy, Snort Rules', 'Proposed', '2026-09-15');

-- Insert Project Milestones
INSERT OR IGNORE INTO milestones (milestone_id, project_id, milestone_name, due_date, submission_date, status) VALUES
-- Milestones for Project 1 (Abhishek.R - Completed)
(1, 1, 'SRS & Requirements Specification', '2026-08-25', '2026-08-24', 'Completed'),
(2, 1, 'UML Design & Database Schema', '2026-09-15', '2026-09-14', 'Completed'),
(3, 1, 'Java Application Implementation', '2026-10-10', '2026-10-08', 'Completed'),
(4, 1, 'Python Data Analytics & Visualizations', '2026-10-30', '2026-10-28', 'Completed'),
(5, 1, 'Testing & GitHub Documentation', '2026-11-15', '2026-11-14', 'Completed'),

-- Milestones for Project 2 (Dharun - Completed)
(6, 2, 'SRS & UI Wireframes', '2026-08-28', '2026-08-27', 'Completed'),
(7, 2, 'Backend API Development', '2026-09-20', '2026-09-19', 'Completed'),
(8, 2, 'Frontend React Integration', '2026-10-15', '2026-10-14', 'Completed'),
(9, 2, 'Payment Gateway & Load Testing', '2026-11-05', '2026-11-04', 'Completed'),

-- Milestones for Project 3 (Kavya - In Progress)
(10, 3, 'SRS & Class Modeling', '2026-08-30', '2026-08-29', 'Completed'),
(11, 3, 'Database Normalization & Spring DAOs', '2026-09-25', '2026-09-24', 'Completed'),
(12, 3, 'Barcode Scanner Module', '2026-10-20', '2026-10-23', 'Completed'),
(13, 3, 'Role Based Security Integration', '2026-11-20', NULL, 'In Progress'),

-- Milestones for Project 4 (Manojkumar - Completed)
(14, 4, 'Dataset Collection & Augmentation', '2026-08-30', '2026-08-28', 'Completed'),
(15, 4, 'CNN Architecture & Training', '2026-09-25', '2026-09-23', 'Completed'),
(16, 4, 'Web Inference API', '2026-10-20', '2026-10-18', 'Completed'),
(17, 4, 'Field Validation & Report', '2026-11-10', '2026-11-09', 'Completed'),

-- Milestones for Project 5 (Naveen - In Progress)
(18, 5, 'UI Mockups & Route Mapping', '2026-09-05', '2026-09-04', 'Completed'),
(19, 5, 'Firebase Realtime DB Setup', '2026-10-01', '2026-10-02', 'Completed'),
(20, 5, 'Driver GPS Mobile Interface', '2026-10-28', NULL, 'In Progress'),
(21, 5, 'Student Live Tracking Screen', '2026-11-25', NULL, 'Pending'),

-- Milestones for Project 8 (Gokul - Completed)
(22, 8, 'Hardware Circuit Schematic', '2026-09-05', '2026-09-04', 'Completed'),
(23, 8, 'Firmware MQTT Telemetry', '2026-09-30', '2026-09-29', 'Completed'),
(24, 8, 'Node-RED Dashboard', '2026-10-25', '2026-10-24', 'Completed'),

-- Milestones for Project 9 (Priya - Completed)
(25, 9, 'Academic Data Preprocessing', '2026-09-10', '2026-09-08', 'Completed'),
(26, 9, 'Feature Engineering & Model Selection', '2026-10-05', '2026-10-04', 'Completed'),
(27, 9, 'Evaluation & Model Tuning', '2026-10-30', '2026-10-29', 'Completed');

-- Insert Evaluations (5 Components per project where evaluated)
-- Project 1 (Abhishek.R)
INSERT OR IGNORE INTO evaluations (eval_id, project_id, component_name, max_marks, obtained_marks, evaluator_name, evaluation_date, comments) VALUES
(1, 1, 'Review 1 - Problem & Design', 20.0, 19.5, 'Dr. S. Murugesan (HoD/IT)', '2026-09-18', 'Exemplary SRS, comprehensive 3NF relational schema, and clear architectural diagrams.'),
(2, 1, 'Review 2 - Implementation', 20.0, 19.0, 'Prof. P. Ramya (AP/IT)', '2026-10-12', 'Clean modular Java code with JDBC integration and robust exception handling.'),
(3, 1, 'Code Quality & Git', 20.0, 19.5, 'Prof. T. Senthil (AP/IT)', '2026-10-25', 'Well-structured repository, meaningful commit messages, and clean code formatting.'),
(4, 1, 'Testing & Verification', 20.0, 19.0, 'Prof. P. Ramya (AP/IT)', '2026-11-05', 'Detailed black-box and white-box test cases with boundary value coverage.'),
(5, 1, 'Final Presentation & Viva', 20.0, 19.5, 'Dr. S. Murugesan (HoD/IT)', '2026-11-16', 'Outstanding viva delivery; excellent data science charts and visual insights.');

-- Project 2 (Dharun Kumar.M)
INSERT OR IGNORE INTO evaluations (eval_id, project_id, component_name, max_marks, obtained_marks, evaluator_name, evaluation_date, comments) VALUES
(6, 2, 'Review 1 - Problem & Design', 20.0, 18.0, 'Dr. S. Murugesan (HoD/IT)', '2026-09-18', 'Good UI wireframes and requirement analysis.'),
(7, 2, 'Review 2 - Implementation', 20.0, 18.5, 'Prof. P. Ramya (AP/IT)', '2026-10-12', 'Smooth React UI with operational Node.js backend.'),
(8, 2, 'Code Quality & Git', 20.0, 17.5, 'Prof. T. Senthil (AP/IT)', '2026-10-25', 'Proper folder structure and modular components.'),
(9, 2, 'Testing & Verification', 20.0, 18.0, 'Prof. P. Ramya (AP/IT)', '2026-11-05', 'API endpoints verified via Postman test suites.'),
(10, 2, 'Final Presentation & Viva', 20.0, 18.5, 'Dr. S. Murugesan (HoD/IT)', '2026-11-16', 'Working live prototype demonstrated effectively.');

-- Project 4 (Manojkumar.P)
INSERT OR IGNORE INTO evaluations (eval_id, project_id, component_name, max_marks, obtained_marks, evaluator_name, evaluation_date, comments) VALUES
(11, 4, 'Review 1 - Problem & Design', 20.0, 18.5, 'Dr. S. Murugesan (HoD/IT)', '2026-09-18', 'Well-formulated agricultural problem statement.'),
(12, 4, 'Review 2 - Implementation', 20.0, 19.0, 'Prof. P. Ramya (AP/IT)', '2026-10-12', 'CNN model achieves 94.2% test accuracy on test split.'),
(13, 4, 'Code Quality & Git', 20.0, 18.0, 'Prof. T. Senthil (AP/IT)', '2026-10-25', 'Jupyter notebooks organized with clear markdown cells.'),
(14, 4, 'Testing & Verification', 20.0, 18.5, 'Prof. P. Ramya (AP/IT)', '2026-11-05', 'Confusion matrix and ROC curves well documented.'),
(15, 4, 'Final Presentation & Viva', 20.0, 19.0, 'Dr. S. Murugesan (HoD/IT)', '2026-11-16', 'Strong demonstration of domain knowledge.');

-- Project 8 (Gokul.N)
INSERT OR IGNORE INTO evaluations (eval_id, project_id, component_name, max_marks, obtained_marks, evaluator_name, evaluation_date, comments) VALUES
(16, 8, 'Review 1 - Problem & Design', 20.0, 17.0, 'Dr. S. Murugesan (HoD/IT)', '2026-09-18', 'Clean circuit design and component selection.'),
(17, 8, 'Review 2 - Implementation', 20.0, 17.5, 'Prof. P. Ramya (AP/IT)', '2026-10-12', 'ESP32 MQTT publishing telemetry reliably.'),
(18, 8, 'Code Quality & Git', 20.0, 16.5, 'Prof. T. Senthil (AP/IT)', '2026-10-25', 'Well-commented C++ code in platformio structure.'),
(19, 8, 'Testing & Verification', 20.0, 17.0, 'Prof. P. Ramya (AP/IT)', '2026-11-05', 'Tested under varied power load conditions.'),
(20, 8, 'Final Presentation & Viva', 20.0, 18.0, 'Dr. S. Murugesan (HoD/IT)', '2026-11-16', 'Working hardware prototype demonstrated.');

-- Project 9 (Priya.M)
INSERT OR IGNORE INTO evaluations (eval_id, project_id, component_name, max_marks, obtained_marks, evaluator_name, evaluation_date, comments) VALUES
(21, 9, 'Review 1 - Problem & Design', 20.0, 18.5, 'Dr. S. Murugesan (HoD/IT)', '2026-09-18', 'Solid statistical approach to student analytics.'),
(22, 9, 'Review 2 - Implementation', 20.0, 18.0, 'Prof. P. Ramya (AP/IT)', '2026-10-12', 'Model tuning with cross-validation properly done.'),
(23, 9, 'Code Quality & Git', 20.0, 18.0, 'Prof. T. Senthil (AP/IT)', '2026-10-25', 'Clean code adherence to PEP8.'),
(24, 9, 'Testing & Verification', 20.0, 17.5, 'Prof. P. Ramya (AP/IT)', '2026-11-05', 'F1-scores and precision-recall curves presented.'),
(25, 9, 'Final Presentation & Viva', 20.0, 18.5, 'Dr. S. Murugesan (HoD/IT)', '2026-11-16', 'Clear insights presented to reviewers.');
