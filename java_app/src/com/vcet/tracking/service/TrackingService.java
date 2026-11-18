package com.vcet.tracking.service;

import com.vcet.tracking.dao.EvaluationDAO;
import com.vcet.tracking.dao.ProjectDAO;
import com.vcet.tracking.dao.StudentDAO;
import com.vcet.tracking.model.*;

import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Business Logic Service for Student Project and Skill Tracking System.
 * Enforces business rules, validation, milestone generation, and skill gap identification.
 */
public class TrackingService {
    private final StudentDAO studentDAO;
    private final ProjectDAO projectDAO;
    private final EvaluationDAO evaluationDAO;

    public TrackingService() {
        this.studentDAO = new StudentDAO();
        this.projectDAO = new ProjectDAO();
        this.evaluationDAO = new EvaluationDAO();
    }

    public List<Student> listAllStudents() {
        return studentDAO.getAllStudents();
    }

    public Student getStudent(String studentId) {
        return studentDAO.getStudentById(studentId);
    }

    public boolean registerStudent(String studentId, String name, String email, String department, String className, String section, String batchYear) {
        if (studentId == null || studentId.trim().isEmpty()) {
            throw new IllegalArgumentException("Student ID cannot be empty.");
        }
        if (!email.contains("@") || !email.contains(".")) {
            throw new IllegalArgumentException("Invalid email address format.");
        }
        Student student = new Student(studentId.trim(), name.trim(), email.trim(), department.trim(), className.trim(), section.trim(), batchYear.trim());
        return studentDAO.addStudent(student);
    }

    public boolean assignSkill(String studentId, int skillId, String proficiency) {
        List<String> validProficiencies = Arrays.asList("Beginner", "Intermediate", "Advanced", "Expert");
        if (!validProficiencies.contains(proficiency)) {
            throw new IllegalArgumentException("Invalid proficiency. Choose from: " + validProficiencies);
        }
        return studentDAO.addSkillToStudent(studentId, skillId, proficiency);
    }

    public List<Skill> getMasterSkills() {
        return studentDAO.getAllMasterSkills();
    }

    public List<Project> listAllProjects() {
        return projectDAO.getAllProjects();
    }

    public List<Project> filterProjects(String filterType, String value) {
        if ("domain".equalsIgnoreCase(filterType)) {
            return projectDAO.getProjectsByDomain(value);
        } else if ("status".equalsIgnoreCase(filterType)) {
            return projectDAO.getProjectsByStatus(value);
        }
        return listAllProjects();
    }

    public Project getProjectDetails(int projectId) {
        Project project = projectDAO.getProjectById(projectId);
        if (project != null) {
            project.setEvaluations(evaluationDAO.getEvaluationsByProjectId(projectId));
        }
        return project;
    }

    public int registerProjectWithDefaultMilestones(String studentId, String title, String domain, String description, String technologies) {
        Student student = studentDAO.getStudentById(studentId);
        if (student == null) {
            throw new IllegalArgumentException("Student with ID '" + studentId + "' not found. Register student first.");
        }

        List<String> validDomains = Arrays.asList(
            "Artificial Intelligence", "Web Development", "Internet of Things", 
            "Cloud Computing", "Cybersecurity", "Data Science", "Mobile Applications"
        );
        if (!validDomains.contains(domain)) {
            throw new IllegalArgumentException("Invalid domain. Supported: " + validDomains);
        }

        Project project = new Project(0, studentId, title, domain, description, technologies, "In Progress", LocalDate.now().toString());
        int projectId = projectDAO.addProject(project);

        if (projectId > 0) {
            // Auto-create standard milestones for the project
            LocalDate now = LocalDate.now();
            projectDAO.addMilestone(new Milestone(0, projectId, "SRS & Requirements Specification", now.plusDays(14).toString(), null, "In Progress"));
            projectDAO.addMilestone(new Milestone(0, projectId, "UML System Design & Database Schema", now.plusDays(35).toString(), null, "Pending"));
            projectDAO.addMilestone(new Milestone(0, projectId, "Core Module Implementation", now.plusDays(60).toString(), null, "Pending"));
            projectDAO.addMilestone(new Milestone(0, projectId, "Verification, Testing & GitHub Docs", now.plusDays(80).toString(), null, "Pending"));
            projectDAO.addMilestone(new Milestone(0, projectId, "Final Presentation & Project Viva", now.plusDays(95).toString(), null, "Pending"));
        }
        return projectId;
    }

    public boolean updateMilestone(int milestoneId, String status, String submissionDate) {
        List<String> validStatuses = Arrays.asList("Pending", "In Progress", "Completed", "Delayed");
        if (!validStatuses.contains(status)) {
            throw new IllegalArgumentException("Invalid status. Supported: " + validStatuses);
        }
        return projectDAO.updateMilestoneStatus(milestoneId, status, submissionDate);
    }

    public boolean recordEvaluation(int projectId, String componentName, double maxMarks, double obtainedMarks, String evaluator, String comments) {
        if (obtainedMarks < 0 || obtainedMarks > maxMarks) {
            throw new IllegalArgumentException("Obtained marks (" + obtainedMarks + ") must be between 0 and " + maxMarks);
        }
        Evaluation eval = new Evaluation(0, projectId, componentName, maxMarks, obtainedMarks, evaluator, LocalDate.now().toString(), comments);
        return evaluationDAO.addEvaluation(eval);
    }

    /**
     * Identifies skill gaps between a project's required technologies and student's registered skills.
     */
    public List<String> analyzeSkillGaps(int projectId) {
        Project project = projectDAO.getProjectById(projectId);
        if (project == null) return Collections.emptyList();

        List<Skill> studentSkills = studentDAO.getSkillsForStudent(project.getStudentId());
        Set<String> knownSkills = studentSkills.stream()
                .map(s -> s.getSkillName().toLowerCase())
                .collect(Collectors.toSet());

        List<String> requiredTechs = Arrays.stream(project.getTechnologiesUsed().split(","))
                .map(String::trim)
                .collect(Collectors.toList());

        List<String> gaps = new ArrayList<>();
        for (String tech : requiredTechs) {
            boolean matched = false;
            for (String known : knownSkills) {
                if (known.contains(tech.toLowerCase()) || tech.toLowerCase().contains(known)) {
                    matched = true;
                    break;
                }
            }
            if (!matched) {
                gaps.add(tech + " (No verified student proficiency on record)");
            }
        }
        return gaps;
    }

    public Map<String, Object> getDepartmentDashboardSummary() {
        return evaluationDAO.getOverallSummary();
    }
}
