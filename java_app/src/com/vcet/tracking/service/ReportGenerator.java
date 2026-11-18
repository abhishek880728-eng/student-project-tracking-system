package com.vcet.tracking.service;

import com.vcet.tracking.model.*;

import java.util.List;
import java.util.Map;

/**
 * Generates formatted tabular reports for console visualization.
 */
public class ReportGenerator {

    public static void printHeader(String title) {
        System.out.println("\n" + "=".repeat(85));
        System.out.printf("  VCET IT :: %s\n", title.toUpperCase());
        System.out.println("=".repeat(85));
    }

    public static void printStudentsTable(List<Student> students) {
        printHeader("Student Roster & Skill Profiles");
        System.out.printf("%-15s | %-18s | %-10s | %-32s\n", "Register No", "Student Name", "Class-Sec", "Skills & Proficiency");
        System.out.println("-".repeat(85));
        for (Student s : students) {
            StringBuilder sb = new StringBuilder();
            if (s.getSkills().isEmpty()) {
                sb.append("None registered");
            } else {
                for (int i = 0; i < s.getSkills().size(); i++) {
                    Skill sk = s.getSkills().get(i);
                    sb.append(sk.getSkillName()).append(" (").append(sk.getProficiency().substring(0, 3)).append(")");
                    if (i < s.getSkills().size() - 1) sb.append(", ");
                }
            }
            System.out.printf("%-15s | %-18s | %-10s | %-32s\n",
                    s.getStudentId(), s.getName(), s.getClassName() + "-" + s.getSection(), sb.toString());
        }
        System.out.println("-".repeat(85));
        System.out.printf("Total Students Listed: %d\n", students.size());
    }

    public static void printProjectsTable(List<Project> projects) {
        printHeader("Student Projects Progress Overview");
        System.out.printf("%-4s | %-14s | %-28s | %-18s | %-12s | %-6s\n",
                "ID", "Student ID", "Project Title", "Domain", "Status", "Prog%");
        System.out.println("-".repeat(85));
        for (Project p : projects) {
            String title = p.getProjectTitle().length() > 27 ? p.getProjectTitle().substring(0, 24) + "..." : p.getProjectTitle();
            System.out.printf("%-4d | %-14s | %-28s | %-18s | %-12s | %5.1f%%\n",
                    p.getProjectId(), p.getStudentId(), title, p.getDomain(), p.getStatus(), p.getCompletionPercentage());
        }
        System.out.println("-".repeat(85));
        System.out.printf("Total Projects Listed: %d\n", projects.size());
    }

    public static void printProjectFullReport(Project project, List<String> skillGaps) {
        printHeader("Detailed Project Dossier - #" + project.getProjectId());
        System.out.printf("Project Title  : %s\n", project.getProjectTitle());
        System.out.printf("Student Author : %s (%s)\n", project.getStudentName(), project.getStudentId());
        System.out.printf("Domain Area    : %s\n", project.getDomain());
        System.out.printf("Lifecycle State: %s (Progress: %.1f%%)\n", project.getStatus(), project.getCompletionPercentage());
        System.out.printf("Tech Stack     : %s\n", project.getTechnologiesUsed());
        System.out.printf("Description    : %s\n", project.getDescription());

        System.out.println("\n[+] Project Milestones & Deadlines:");
        System.out.printf("    %-4s | %-35s | %-12s | %-12s | %-10s\n", "ID", "Milestone Name", "Due Date", "Submitted", "Status");
        System.out.println("    " + "-".repeat(78));
        for (Milestone m : project.getMilestones()) {
            System.out.printf("    %-4d | %-35s | %-12s | %-12s | %-10s\n",
                    m.getMilestoneId(), m.getMilestoneName(), m.getDueDate(),
                    (m.getSubmissionDate() != null ? m.getSubmissionDate() : "-"), m.getStatus());
        }

        System.out.println("\n[+] Evaluation Marks by Component (Max 100):");
        if (project.getEvaluations().isEmpty()) {
            System.out.println("    No component evaluations logged yet.");
        } else {
            System.out.printf("    %-32s | %-12s | %-22s | %-15s\n", "Component", "Marks", "Evaluator", "Comments");
            System.out.println("    " + "-".repeat(82));
            double totalObt = 0;
            double totalMax = 0;
            for (Evaluation ev : project.getEvaluations()) {
                System.out.printf("    %-32s | %4.1f / %-4.1f | %-22s | %-15s\n",
                        ev.getComponentName(), ev.getObtainedMarks(), ev.getMaxMarks(), ev.getEvaluatorName(), ev.getComments());
                totalObt += ev.getObtainedMarks();
                totalMax += ev.getMaxMarks();
            }
            System.out.println("    " + "-".repeat(82));
            System.out.printf("    AGGREGATE ASSESSMENT SCORE      : %.1f / %.1f (%.1f%%)\n",
                    totalObt, totalMax, (totalMax > 0 ? (totalObt * 100.0 / totalMax) : 0));
        }

        System.out.println("\n[+] Skill Gap Analysis:");
        if (skillGaps.isEmpty()) {
            System.out.println("    [OK] Student possesses registered proficiencies matching all required technologies.");
        } else {
            System.out.println("    [!] Potential Skill Gaps Detected:");
            for (String gap : skillGaps) {
                System.out.println("        - " + gap);
            }
        }
        System.out.println("=".repeat(85));
    }

    public static void printDepartmentSummary(Map<String, Object> summary) {
        printHeader("Department Executive Progress Dashboard");
        System.out.printf("Total Registered Projects   : %s\n", summary.get("total_projects"));
        System.out.printf("Completed Projects          : %s\n", summary.get("completed_projects"));
        System.out.printf("In Progress Projects        : %s\n", summary.get("in_progress_projects"));
        System.out.printf("Under Review Projects       : %s\n", summary.get("under_review_projects"));
        System.out.printf("Proposed Projects           : %s\n", summary.get("proposed_projects"));
        System.out.printf("Average Evaluation Mark     : %.2f / 20.0\n", summary.get("avg_mark"));
        System.out.println("=".repeat(85));
    }
}
