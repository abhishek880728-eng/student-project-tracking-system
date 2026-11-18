package com.vcet.tracking.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Model class representing a Student in the VCET IT department.
 * Aligns with 25ITT32 (Java Programming) OOP principles.
 */
public class Student {
    private String studentId;
    private String name;
    private String email;
    private String department;
    private String className;
    private String section;
    private String batchYear;
    private List<Skill> skills;

    public Student() {
        this.skills = new ArrayList<>();
    }

    public Student(String studentId, String name, String email, String department, String className, String section, String batchYear) {
        this.studentId = studentId;
        this.name = name;
        this.email = email;
        this.department = department;
        this.className = className;
        this.section = section;
        this.batchYear = batchYear;
        this.skills = new ArrayList<>();
    }

    // Getters and Setters
    public String getStudentId() { return studentId; }
    public void setStudentId(String studentId) { this.studentId = studentId; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }

    public String getClassName() { return className; }
    public void setClassName(String className) { this.className = className; }

    public String getSection() { return section; }
    public void setSection(String section) { this.section = section; }

    public String getBatchYear() { return batchYear; }
    public void setBatchYear(String batchYear) { this.batchYear = batchYear; }

    public List<Skill> getSkills() { return skills; }
    public void setSkills(List<Skill> skills) { this.skills = skills; }
    public void addSkill(Skill skill) { this.skills.add(skill); }

    @Override
    public String toString() {
        return String.format("[%s] %s | %s - Sec %s | %s", studentId, name, className, section, email);
    }
}
