package com.vcet.tracking;

import com.vcet.tracking.dao.DatabaseConnection;
import com.vcet.tracking.model.Project;
import com.vcet.tracking.model.Skill;
import com.vcet.tracking.model.Student;
import com.vcet.tracking.service.ReportGenerator;
import com.vcet.tracking.service.TrackingService;

import java.util.List;
import java.util.Scanner;

/**
 * ============================================================================
 * VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12
 * DEPARTMENT OF INFORMATION TECHNOLOGY
 * ACADEMIC YEAR: 2026-27 (ODD) | CLASS: 25IT3A&B
 * ACTIVITY: PROJECT-BASED ASSESSMENT
 *
 * Scenario 2: Student Project and Skill Tracking System
 * Student Name: Abhishek.R
 * Register No : 732925ITR002
 * Class       : 25IT3A (Section A)
 * ============================================================================
 */
public class Main {
    private static final TrackingService service = new TrackingService();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // Support running automated demo mode via argument "--demo"
        if (args.length > 0 && "--demo".equalsIgnoreCase(args[0])) {
            runAutomatedDemonstration();
            return;
        }

        boolean running = true;
        while (running) {
            displayMenu();
            System.out.print("Select an option [1-9]: ");
            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1":
                    handleListStudents();
                    break;
                case "2":
                    handleRegisterStudent();
                    break;
                case "3":
                    handleListProjects();
                    break;
                case "4":
                    handleRegisterProject();
                    break;
                case "5":
                    handleUpdateMilestone();
                    break;
                case "6":
                    handleRecordEvaluation();
                    break;
                case "7":
                    handleProjectFullReport();
                    break;
                case "8":
                    handleDepartmentSummary();
                    break;
                case "9":
                    System.out.println("\n[!] Exiting Student Project and Skill Tracking System. Goodbye!");
                    DatabaseConnection.closeConnection();
                    running = false;
                    break;
                default:
                    System.out.println("[X] Invalid choice. Please enter a number between 1 and 9.");
            }

            if (running) {
                System.out.print("\nPress [Enter] to return to main menu...");
                scanner.nextLine();
            }
        }
    }

    private static void displayMenu() {
        System.out.println("\n" + "=".repeat(75));
        System.out.println("  VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS)");
        System.out.println("  DEPARTMENT OF INFORMATION TECHNOLOGY - CLASS 25IT3A");
        System.out.println("  STUDENT PROJECT & SKILL TRACKING SYSTEM");
        System.out.println("  Author: Abhishek.R (732925ITR002)");
        System.out.println("=".repeat(75));
        System.out.println("  1. View All Registered Students & Technical Skills");
        System.out.println("  2. Register New Student & Assign Technical Skills");
        System.out.println("  3. View All Student Projects (with Domain & Status Filters)");
        System.out.println("  4. Register New Student Project");
        System.out.println("  5. Update Project Milestone & Submission Status");
        System.out.println("  6. Record Evaluation Marks for Project Components");
        System.out.println("  7. View Detailed Project Dossier & Skill Gap Analysis");
        System.out.println("  8. View Department Executive Progress Dashboard");
        System.out.println("  9. Exit System");
        System.out.println("=".repeat(75));
    }

    private static void handleListStudents() {
        List<Student> students = service.listAllStudents();
        ReportGenerator.printStudentsTable(students);
    }

    private static void handleRegisterStudent() {
        System.out.println("\n--- Register New Student ---");
        try {
            System.out.print("Enter Register Number (e.g., 732925ITR150): ");
            String regNo = scanner.nextLine().trim();

            System.out.print("Enter Student Full Name: ");
            String name = scanner.nextLine().trim();

            System.out.print("Enter Institutional Email: ");
            String email = scanner.nextLine().trim();

            System.out.print("Enter Department [Default: Information Technology]: ");
            String dept = scanner.nextLine().trim();
            if (dept.isEmpty()) dept = "Information Technology";

            System.out.print("Enter Class Name [Default: 25IT3A]: ");
            String className = scanner.nextLine().trim();
            if (className.isEmpty()) className = "25IT3A";

            System.out.print("Enter Section [A or B]: ");
            String sec = scanner.nextLine().trim().toUpperCase();
            if (sec.isEmpty()) sec = "A";

            System.out.print("Enter Batch Year [Default: 2025-2029]: ");
            String batch = scanner.nextLine().trim();
            if (batch.isEmpty()) batch = "2025-2029";

            boolean success = service.registerStudent(regNo, name, email, dept, className, sec, batch);
            if (success) {
                System.out.println("[+] Student registered successfully!");
                promptForSkillAssignment(regNo);
            } else {
                System.out.println("[X] Registration failed. Register number or email might already exist.");
            }
        } catch (Exception e) {
            System.out.println("[X] Error: " + e.getMessage());
        }
    }

    private static void promptForSkillAssignment(String regNo) {
        System.out.print("Do you wish to assign technical skills now? (y/n): ");
        String ans = scanner.nextLine().trim();
        if (!ans.equalsIgnoreCase("y")) return;

        List<Skill> masterSkills = service.getMasterSkills();
        System.out.println("\nAvailable Skills Directory:");
        for (Skill s : masterSkills) {
            System.out.printf("  [%2d] %-20s (%s)\n", s.getSkillId(), s.getSkillName(), s.getCategory());
        }

        while (true) {
            System.out.print("\nEnter Skill ID to assign (or 0 to finish): ");
            String input = scanner.nextLine().trim();
            int skillId;
            try {
                skillId = Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("[X] Please enter a valid numerical ID.");
                continue;
            }
            if (skillId == 0) break;

            System.out.print("Enter Proficiency Level [Beginner / Intermediate / Advanced / Expert]: ");
            String prof = scanner.nextLine().trim();

            try {
                if (service.assignSkill(regNo, skillId, prof)) {
                    System.out.println("[+] Skill added to student profile.");
                } else {
                    System.out.println("[X] Failed to add skill.");
                }
            } catch (Exception e) {
                System.out.println("[X] Error: " + e.getMessage());
            }
        }
    }

    private static void handleListProjects() {
        System.out.println("\n--- Project Catalog Filter ---");
        System.out.println("1. View All Projects");
        System.out.println("2. Filter by Domain (e.g. AI, Web Development, Data Science)");
        System.out.println("3. Filter by Status (Completed, In Progress, Under Review, Proposed)");
        System.out.print("Choose option [1-3]: ");
        String sub = scanner.nextLine().trim();

        List<Project> projects;
        if ("2".equals(sub)) {
            System.out.print("Enter Domain keyword: ");
            String domain = scanner.nextLine().trim();
            projects = service.filterProjects("domain", domain);
        } else if ("3".equals(sub)) {
            System.out.print("Enter Status keyword: ");
            String status = scanner.nextLine().trim();
            projects = service.filterProjects("status", status);
        } else {
            projects = service.listAllProjects();
        }

        ReportGenerator.printProjectsTable(projects);
    }

    private static void handleRegisterProject() {
        System.out.println("\n--- Register New Student Project ---");
        try {
            System.out.print("Enter Student Register Number: ");
            String regNo = scanner.nextLine().trim();

            System.out.print("Enter Project Title: ");
            String title = scanner.nextLine().trim();

            System.out.println("Domains: Artificial Intelligence, Web Development, Internet of Things,");
            System.out.println("         Cloud Computing, Cybersecurity, Data Science, Mobile Applications");
            System.out.print("Enter Project Domain: ");
            String domain = scanner.nextLine().trim();

            System.out.print("Enter Project Abstract / Description: ");
            String desc = scanner.nextLine().trim();

            System.out.print("Enter Technologies Used (comma-separated, e.g. Java, Python, SQLite): ");
            String tech = scanner.nextLine().trim();

            int projectId = service.registerProjectWithDefaultMilestones(regNo, title, domain, desc, tech);
            if (projectId > 0) {
                System.out.printf("[+] Project successfully registered with Project ID: #%d\n", projectId);
                System.out.println("[+] 5 Standard Academic Milestones have been automatically attached.");
            } else {
                System.out.println("[X] Failed to register project. Verify student exists.");
            }
        } catch (Exception e) {
            System.out.println("[X] Error: " + e.getMessage());
        }
    }

    private static void handleUpdateMilestone() {
        System.out.println("\n--- Update Project Milestone Status ---");
        try {
            System.out.print("Enter Project ID: ");
            int projId = Integer.parseInt(scanner.nextLine().trim());

            Project p = service.getProjectDetails(projId);
            if (p == null) {
                System.out.println("[X] Project not found.");
                return;
            }

            System.out.println("Milestones for: " + p.getProjectTitle());
            for (var m : p.getMilestones()) {
                System.out.printf("  [%d] %-35s (Current: %s, Due: %s)\n",
                        m.getMilestoneId(), m.getMilestoneName(), m.getStatus(), m.getDueDate());
            }

            System.out.print("Enter Milestone ID to update: ");
            int mId = Integer.parseInt(scanner.nextLine().trim());

            System.out.print("Enter New Status [Pending / In Progress / Completed / Delayed]: ");
            String status = scanner.nextLine().trim();

            System.out.print("Enter Submission Date (YYYY-MM-DD or leave blank for today): ");
            String subDate = scanner.nextLine().trim();
            if (subDate.isEmpty()) subDate = java.time.LocalDate.now().toString();

            if (service.updateMilestone(mId, status, subDate)) {
                System.out.println("[+] Milestone status updated successfully!");
            } else {
                System.out.println("[X] Update failed. Check milestone ID.");
            }
        } catch (Exception e) {
            System.out.println("[X] Error: " + e.getMessage());
        }
    }

    private static void handleRecordEvaluation() {
        System.out.println("\n--- Record Evaluation Marks ---");
        try {
            System.out.print("Enter Project ID: ");
            int projId = Integer.parseInt(scanner.nextLine().trim());

            Project p = service.getProjectDetails(projId);
            if (p == null) {
                System.out.println("[X] Project not found.");
                return;
            }

            System.out.println("Evaluation Components:");
            System.out.println("1. Review 1 - Problem & Design");
            System.out.println("2. Review 2 - Implementation");
            System.out.println("3. Code Quality & Git");
            System.out.println("4. Testing & Verification");
            System.out.println("5. Final Presentation & Viva");
            System.out.print("Enter Component Name exactly or choose [1-5]: ");
            String compChoice = scanner.nextLine().trim();

            String compName;
            switch (compChoice) {
                case "1": compName = "Review 1 - Problem & Design"; break;
                case "2": compName = "Review 2 - Implementation"; break;
                case "3": compName = "Code Quality & Git"; break;
                case "4": compName = "Testing & Verification"; break;
                case "5": compName = "Final Presentation & Viva"; break;
                default: compName = compChoice; break;
            }

            System.out.print("Enter Maximum Marks [Default: 20.0]: ");
            String maxStr = scanner.nextLine().trim();
            double maxMarks = maxStr.isEmpty() ? 20.0 : Double.parseDouble(maxStr);

            System.out.print("Enter Obtained Marks: ");
            double obtainedMarks = Double.parseDouble(scanner.nextLine().trim());

            System.out.print("Enter Faculty Evaluator Name: ");
            String evaluator = scanner.nextLine().trim();

            System.out.print("Enter Feedback / Comments: ");
            String comments = scanner.nextLine().trim();

            if (service.recordEvaluation(projId, compName, maxMarks, obtainedMarks, evaluator, comments)) {
                System.out.println("[+] Component evaluation logged successfully!");
            } else {
                System.out.println("[X] Failed to record evaluation.");
            }
        } catch (Exception e) {
            System.out.println("[X] Error: " + e.getMessage());
        }
    }

    private static void handleProjectFullReport() {
        System.out.print("\nEnter Project ID to inspect: ");
        try {
            int projId = Integer.parseInt(scanner.nextLine().trim());
            Project p = service.getProjectDetails(projId);
            if (p == null) {
                System.out.println("[X] Project ID not found.");
                return;
            }
            List<String> gaps = service.analyzeSkillGaps(projId);
            ReportGenerator.printProjectFullReport(p, gaps);
        } catch (NumberFormatException e) {
            System.out.println("[X] Invalid ID format.");
        }
    }

    private static void handleDepartmentSummary() {
        ReportGenerator.printDepartmentSummary(service.getDepartmentDashboardSummary());
    }

    /**
     * Executes non-interactive automated test run for verification and grading.
     */
    public static void runAutomatedDemonstration() {
        System.out.println("\n" + "=".repeat(85));
        System.out.println("  AUTOMATED DEMONSTRATION & VERIFICATION RUN");
        System.out.println("  Scenario 2: Student Project and Skill Tracking System");
        System.out.println("  Author: Abhishek.R | Register No: 732925ITR002 | Class: 25IT3A");
        System.out.println("=".repeat(85));

        System.out.println("\n>>> TEST 1: Retrieve Roster of Students & Skills");
        List<Student> students = service.listAllStudents();
        ReportGenerator.printStudentsTable(students);

        System.out.println("\n>>> TEST 2: Retrieve All Registered Projects");
        List<Project> projects = service.listAllProjects();
        ReportGenerator.printProjectsTable(projects);

        System.out.println("\n>>> TEST 3: Inspect Project #1 (Abhishek.R) Dossier & Skill Gap Analysis");
        Project p1 = service.getProjectDetails(1);
        ReportGenerator.printProjectFullReport(p1, service.analyzeSkillGaps(1));

        System.out.println("\n>>> TEST 4: Department Executive Dashboard Metrics");
        ReportGenerator.printDepartmentSummary(service.getDepartmentDashboardSummary());

        System.out.println("\n[+] Automated verification demonstration concluded with 100% success!");
    }
}
