package com.vcet.tracking.model;

/**
 * Model class representing a Project Milestone.
 */
public class Milestone {
    private int milestoneId;
    private int projectId;
    private String milestoneName;
    private String dueDate;
    private String submissionDate;
    private String status; // Pending, In Progress, Completed, Delayed

    public Milestone() {}

    public Milestone(int milestoneId, int projectId, String milestoneName, String dueDate, String submissionDate, String status) {
        this.milestoneId = milestoneId;
        this.projectId = projectId;
        this.milestoneName = milestoneName;
        this.dueDate = dueDate;
        this.submissionDate = submissionDate;
        this.status = status;
    }

    public int getMilestoneId() { return milestoneId; }
    public void setMilestoneId(int milestoneId) { this.milestoneId = milestoneId; }

    public int getProjectId() { return projectId; }
    public void setProjectId(int projectId) { this.projectId = projectId; }

    public String getMilestoneName() { return milestoneName; }
    public void setMilestoneName(String milestoneName) { this.milestoneName = milestoneName; }

    public String getDueDate() { return dueDate; }
    public void setDueDate(String dueDate) { this.dueDate = dueDate; }

    public String getSubmissionDate() { return submissionDate; }
    public void setSubmissionDate(String submissionDate) { this.submissionDate = submissionDate; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    @Override
    public String toString() {
        return String.format("[Milestone %d] %s | Due: %s | Submitted: %s | Status: %s",
                milestoneId, milestoneName, dueDate, (submissionDate != null ? submissionDate : "N/A"), status);
    }
}
