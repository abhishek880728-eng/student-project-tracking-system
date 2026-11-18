package com.vcet.tracking.model;

/**
 * Model class representing a Technical Skill and Student's Proficiency.
 */
public class Skill {
    private int skillId;
    private String skillName;
    private String category;
    private String proficiency; // Beginner, Intermediate, Advanced, Expert

    public Skill() {}

    public Skill(int skillId, String skillName, String category) {
        this.skillId = skillId;
        this.skillName = skillName;
        this.category = category;
    }

    public Skill(int skillId, String skillName, String category, String proficiency) {
        this.skillId = skillId;
        this.skillName = skillName;
        this.category = category;
        this.proficiency = proficiency;
    }

    public int getSkillId() { return skillId; }
    public void setSkillId(int skillId) { this.skillId = skillId; }

    public String getSkillName() { return skillName; }
    public void setSkillName(String skillName) { this.skillName = skillName; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getProficiency() { return proficiency; }
    public void setProficiency(String proficiency) { this.proficiency = proficiency; }

    @Override
    public String toString() {
        if (proficiency != null && !proficiency.isEmpty()) {
            return String.format("%s (%s - %s)", skillName, category, proficiency);
        }
        return String.format("%s (%s)", skillName, category);
    }
}
