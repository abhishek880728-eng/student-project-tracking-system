package com.vcet.tracking.dao;

import com.vcet.tracking.model.Skill;
import com.vcet.tracking.model.Student;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Data Access Object for Student and Skill entities.
 */
public class StudentDAO {

    public List<Student> getAllStudents() {
        List<Student> students = new ArrayList<>();
        String sql = "SELECT student_id, name, email, department, class_name, section, batch_year FROM students ORDER BY student_id ASC";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            while (rs.next()) {
                Student s = new Student(
                    rs.getString("student_id"),
                    rs.getString("name"),
                    rs.getString("email"),
                    rs.getString("department"),
                    rs.getString("class_name"),
                    rs.getString("section"),
                    rs.getString("batch_year")
                );
                s.setSkills(getSkillsForStudent(s.getStudentId()));
                students.add(s);
            }
        } catch (SQLException e) {
            System.err.println("Error fetching students: " + e.getMessage());
        }
        return students;
    }

    public Student getStudentById(String studentId) {
        String sql = "SELECT student_id, name, email, department, class_name, section, batch_year FROM students WHERE student_id = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, studentId);
            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    Student s = new Student(
                        rs.getString("student_id"),
                        rs.getString("name"),
                        rs.getString("email"),
                        rs.getString("department"),
                        rs.getString("class_name"),
                        rs.getString("section"),
                        rs.getString("batch_year")
                    );
                    s.setSkills(getSkillsForStudent(studentId));
                    return s;
                }
            }
        } catch (SQLException e) {
            System.err.println("Error fetching student by ID: " + e.getMessage());
        }
        return null;
    }

    public boolean addStudent(Student student) {
        String sql = "INSERT INTO students (student_id, name, email, department, class_name, section, batch_year) VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, student.getStudentId());
            pstmt.setString(2, student.getName());
            pstmt.setString(3, student.getEmail());
            pstmt.setString(4, student.getDepartment());
            pstmt.setString(5, student.getClassName());
            pstmt.setString(6, student.getSection());
            pstmt.setString(7, student.getBatchYear());
            return pstmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error adding student: " + e.getMessage());
            return false;
        }
    }

    public List<Skill> getSkillsForStudent(String studentId) {
        List<Skill> skills = new ArrayList<>();
        String sql = "SELECT s.skill_id, s.skill_name, s.skill_category, ss.proficiency_level " +
                     "FROM student_skills ss " +
                     "JOIN skills s ON ss.skill_id = s.skill_id " +
                     "WHERE ss.student_id = ? ORDER BY s.skill_name ASC";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, studentId);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    skills.add(new Skill(
                        rs.getInt("skill_id"),
                        rs.getString("skill_name"),
                        rs.getString("skill_category"),
                        rs.getString("proficiency_level")
                    ));
                }
            }
        } catch (SQLException e) {
            System.err.println("Error fetching student skills: " + e.getMessage());
        }
        return skills;
    }

    public boolean addSkillToStudent(String studentId, int skillId, String proficiency) {
        String sql = "INSERT OR REPLACE INTO student_skills (student_id, skill_id, proficiency_level) VALUES (?, ?, ?)";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, studentId);
            pstmt.setInt(2, skillId);
            pstmt.setString(3, proficiency);
            return pstmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error adding skill to student: " + e.getMessage());
            return false;
        }
    }

    public List<Skill> getAllMasterSkills() {
        List<Skill> skills = new ArrayList<>();
        String sql = "SELECT skill_id, skill_name, skill_category FROM skills ORDER BY skill_category, skill_name";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {
            while (rs.next()) {
                skills.add(new Skill(
                    rs.getInt("skill_id"),
                    rs.getString("skill_name"),
                    rs.getString("skill_category")
                ));
            }
        } catch (SQLException e) {
            System.err.println("Error fetching master skills: " + e.getMessage());
        }
        return skills;
    }
}
