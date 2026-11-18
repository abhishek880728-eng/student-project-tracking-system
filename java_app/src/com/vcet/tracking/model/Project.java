package com.vcet.tracking.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Model class representing a Student Mini-Project.
 */
public class Project {
    private int projectId;
    private String studentId;
    private String studentName;
    private String projectTitle;
    private String domain;
    private String description;
    private String technologiesUsed;
    private String status; // Proposed, In Progress, Under Review, Completed
    private String createdAt;
    private List<Milestone> milestones;
    private List<Evaluation> evaluations;

    public Project() {
        this.milestones = new ArrayList<>();
        this.evaluations = new ArrayList<>();
    }

    public Project(int projectId, String studentId, String projectTitle, String domain, 
                   String description, String technologiesUsed, String status, String createdAt) {
        this.projectId = projectId;
        this.studentId = studentId;
        this.projectTitle = projectTitle;
        this.domain = domain;
        this.description = description;
        this.technologiesUsed = technologiesUsed;
        this.status = status;
        this.createdAt = createdAt;
        this.milestones = new ArrayList<>();
        this.evaluations = new ArrayList<>();
    }

    // Getters and Setters
    public int getProjectId() { return projectId; }
    public void setProjectId(int projectId) { this.projectId = projectId; }

    public String getStudentId() { return studentId; }
    public void setStudentId(String studentId) { this.studentId = studentId; }

    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }

    public String getProjectTitle() { return projectTitle; }
    public void setProjectTitle(String projectTitle) { this.projectTitle = projectTitle; }

    public String getDomain() { return domain; }
    public void setDomain(String domain) { this.domain = domain; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getTechnologiesUsed() { return technologiesUsed; }
    public void setTechnologiesUsed(String technologiesUsed) { this.technologiesUsed = technologiesUsed; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public String getCreatedAt() { return createdAt; }
    public void setCreatedAt(String createdAt) { this.createdAt = createdAt; }

    public List<Milestone> getMilestones() { return milestones; }
    public void setMilestones(List<Milestone> milestones) { this.milestones = milestones; }
    public void addMilestone(Milestone milestone) { this.milestones.add(milestone); }

    public List<Evaluation> getEvaluations() { return evaluations; }
    public void setEvaluations(List<Evaluation> evaluations) { this.evaluations = evaluations; }
    public void addEvaluation(Evaluation evaluation) { this.evaluations.add(evaluation); }

    public double calculateTotalMarks() {
        return evaluations.stream().mapToDouble(Evaluation::getObtainedMarks).sum();
    }

    public double calculateMaxMarks() {
        return evaluations.stream().mapToDouble(Evaluation::getMaxMarks).sum();
    }

    public double getCompletionPercentage() {
        if (milestones.isEmpty()) return 0.0;
        long completedCount = milestones.stream().filter(m -> "Completed".equalsIgnoreCase(m.getStatus())).count();
        return (completedCount * 100.0) / milestones.size();
    }

    @Override
    public String toString() {
        return String.format("#%d: %s [%s] - Status: %s (Student: %s)", projectId, projectTitle, domain, status, studentId);
    }
}
