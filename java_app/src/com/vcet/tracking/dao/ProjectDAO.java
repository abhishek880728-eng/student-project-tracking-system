package com.vcet.tracking.dao;

import com.vcet.tracking.model.Milestone;
import com.vcet.tracking.model.Project;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Data Access Object for Projects and Milestones.
 */
public class ProjectDAO {

    public List<Project> getAllProjects() {
        List<Project> projects = new ArrayList<>();
        String sql = "SELECT p.project_id, p.student_id, s.name AS student_name, p.project_title, " +
                     "p.domain, p.description, p.technologies_used, p.status, p.created_at " +
                     "FROM projects p " +
                     "JOIN students s ON p.student_id = s.student_id " +
                     "ORDER BY p.project_id ASC";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            while (rs.next()) {
                Project p = mapResultSetToProject(rs);
                p.setMilestones(getMilestonesByProjectId(p.getProjectId()));
                projects.add(p);
            }
        } catch (SQLException e) {
            System.err.println("Error fetching projects: " + e.getMessage());
        }
        return projects;
    }

    public List<Project> getProjectsByDomain(String domain) {
        List<Project> projects = new ArrayList<>();
        String sql = "SELECT p.project_id, p.student_id, s.name AS student_name, p.project_title, " +
                     "p.domain, p.description, p.technologies_used, p.status, p.created_at " +
                     "FROM projects p " +
                     "JOIN students s ON p.student_id = s.student_id " +
                     "WHERE p.domain LIKE ? ORDER BY p.project_id ASC";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, "%" + domain + "%");
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    Project p = mapResultSetToProject(rs);
                    p.setMilestones(getMilestonesByProjectId(p.getProjectId()));
                    projects.add(p);
                }
            }
        } catch (SQLException e) {
            System.err.println("Error filtering projects by domain: " + e.getMessage());
        }
        return projects;
    }

    public List<Project> getProjectsByStatus(String status) {
        List<Project> projects = new ArrayList<>();
        String sql = "SELECT p.project_id, p.student_id, s.name AS student_name, p.project_title, " +
                     "p.domain, p.description, p.technologies_used, p.status, p.created_at " +
                     "FROM projects p " +
                     "JOIN students s ON p.student_id = s.student_id " +
                     "WHERE p.status = ? ORDER BY p.project_id ASC";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, status);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    Project p = mapResultSetToProject(rs);
                    p.setMilestones(getMilestonesByProjectId(p.getProjectId()));
                    projects.add(p);
                }
            }
        } catch (SQLException e) {
            System.err.println("Error filtering projects by status: " + e.getMessage());
        }
        return projects;
    }

    public Project getProjectById(int projectId) {
        String sql = "SELECT p.project_id, p.student_id, s.name AS student_name, p.project_title, " +
                     "p.domain, p.description, p.technologies_used, p.status, p.created_at " +
                     "FROM projects p " +
                     "JOIN students s ON p.student_id = s.student_id " +
                     "WHERE p.project_id = ?";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, projectId);
            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    Project p = mapResultSetToProject(rs);
                    p.setMilestones(getMilestonesByProjectId(projectId));
                    return p;
                }
            }
        } catch (SQLException e) {
            System.err.println("Error fetching project by ID: " + e.getMessage());
        }
        return null;
    }

    public int addProject(Project project) {
        String sql = "INSERT INTO projects (student_id, project_title, domain, description, technologies_used, status, created_at) " +
                     "VALUES (?, ?, ?, ?, ?, ?, ?)";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            pstmt.setString(1, project.getStudentId());
            pstmt.setString(2, project.getProjectTitle());
            pstmt.setString(3, project.getDomain());
            pstmt.setString(4, project.getDescription());
            pstmt.setString(5, project.getTechnologiesUsed());
            pstmt.setString(6, project.getStatus());
            pstmt.setString(7, project.getCreatedAt() != null ? project.getCreatedAt() : java.time.LocalDate.now().toString());

            int affected = pstmt.executeUpdate();
            if (affected > 0) {
                try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {
                    if (generatedKeys.next()) {
                        return generatedKeys.getInt(1);
                    }
                }
            }
        } catch (SQLException e) {
            System.err.println("Error creating project: " + e.getMessage());
        }
        return -1;
    }

    public boolean updateProjectStatus(int projectId, String newStatus) {
        String sql = "UPDATE projects SET status = ? WHERE project_id = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, newStatus);
            pstmt.setInt(2, projectId);
            return pstmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error updating project status: " + e.getMessage());
            return false;
        }
    }

    public List<Milestone> getMilestonesByProjectId(int projectId) {
        List<Milestone> milestones = new ArrayList<>();
        String sql = "SELECT milestone_id, project_id, milestone_name, due_date, submission_date, status " +
                     "FROM milestones WHERE project_id = ? ORDER BY due_date ASC";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, projectId);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    milestones.add(new Milestone(
                        rs.getInt("milestone_id"),
                        rs.getInt("project_id"),
                        rs.getString("milestone_name"),
                        rs.getString("due_date"),
                        rs.getString("submission_date"),
                        rs.getString("status")
                    ));
                }
            }
        } catch (SQLException e) {
            System.err.println("Error fetching milestones: " + e.getMessage());
        }
        return milestones;
    }

    public boolean addMilestone(Milestone milestone) {
        String sql = "INSERT INTO milestones (project_id, milestone_name, due_date, submission_date, status) VALUES (?, ?, ?, ?, ?)";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, milestone.getProjectId());
            pstmt.setString(2, milestone.getMilestoneName());
            pstmt.setString(3, milestone.getDueDate());
            pstmt.setString(4, milestone.getSubmissionDate());
            pstmt.setString(5, milestone.getStatus());
            return pstmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error adding milestone: " + e.getMessage());
            return false;
        }
    }

    public boolean updateMilestoneStatus(int milestoneId, String status, String submissionDate) {
        String sql = "UPDATE milestones SET status = ?, submission_date = ? WHERE milestone_id = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, status);
            pstmt.setString(2, submissionDate);
            pstmt.setInt(3, milestoneId);
            return pstmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error updating milestone: " + e.getMessage());
            return false;
        }
    }

    private Project mapResultSetToProject(ResultSet rs) throws SQLException {
        Project p = new Project(
            rs.getInt("project_id"),
            rs.getString("student_id"),
            rs.getString("project_title"),
            rs.getString("domain"),
            rs.getString("description"),
            rs.getString("technologies_used"),
            rs.getString("status"),
            rs.getString("created_at")
        );
        p.setStudentName(rs.getString("student_name"));
        return p;
    }
}
