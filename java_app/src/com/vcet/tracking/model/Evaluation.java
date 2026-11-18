package com.vcet.tracking.model;

/**
 * Model class representing a Project Component Evaluation.
 */
public class Evaluation {
    private int evalId;
    private int projectId;
    private String componentName;
    private double maxMarks;
    private double obtainedMarks;
    private String evaluatorName;
    private String evaluationDate;
    private String comments;

    public Evaluation() {}

    public Evaluation(int evalId, int projectId, String componentName, double maxMarks, 
                      double obtainedMarks, String evaluatorName, String evaluationDate, String comments) {
        this.evalId = evalId;
        this.projectId = projectId;
        this.componentName = componentName;
        this.maxMarks = maxMarks;
        this.obtainedMarks = obtainedMarks;
        this.evaluatorName = evaluatorName;
        this.evaluationDate = evaluationDate;
        this.comments = comments;
    }

    public int getEvalId() { return evalId; }
    public void setEvalId(int evalId) { this.evalId = evalId; }

    public int getProjectId() { return projectId; }
    public void setProjectId(int projectId) { this.projectId = projectId; }

    public String getComponentName() { return componentName; }
    public void setComponentName(String componentName) { this.componentName = componentName; }

    public double getMaxMarks() { return maxMarks; }
    public void setMaxMarks(double maxMarks) { this.maxMarks = maxMarks; }

    public double getObtainedMarks() { return obtainedMarks; }
    public void setObtainedMarks(double obtainedMarks) { this.obtainedMarks = obtainedMarks; }

    public String getEvaluatorName() { return evaluatorName; }
    public void setEvaluatorName(String evaluatorName) { this.evaluatorName = evaluatorName; }

    public String getEvaluationDate() { return evaluationDate; }
    public void setEvaluationDate(String evaluationDate) { this.evaluationDate = evaluationDate; }

    public String getComments() { return comments; }
    public void setComments(String comments) { this.comments = comments; }

    @Override
    public String toString() {
        return String.format("%s: %.1f / %.1f (Evaluator: %s) - %s",
                componentName, obtainedMarks, maxMarks, evaluatorName, comments);
    }
}
