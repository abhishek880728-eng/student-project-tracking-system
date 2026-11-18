package com.vcet.tracking.dao;

import com.vcet.tracking.model.Evaluation;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Data Access Object for Evaluations and Aggregated Metrics.
 */
public class EvaluationDAO {

    public List<Evaluation> getEvaluationsByProjectId(int projectId) {
        List<Evaluation> evaluations = new ArrayList<>();
        String sql = "SELECT eval_id, project_id, component_name, max_marks, obtained_marks, " +
                     "evaluator_name, evaluation_date, comments FROM evaluations " +
                     "WHERE project_id = ? ORDER BY eval_id ASC";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, projectId);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    evaluations.add(new Evaluation(
                        rs.getInt("eval_id"),
                        rs.getInt("project_id"),
                        rs.getString("component_name"),
                        rs.getDouble("max_marks"),
                        rs.getDouble("obtained_marks"),
                        rs.getString("evaluator_name"),
                        rs.getString("evaluation_date"),
                        rs.getString("comments")
                    ));
                }
            }
        } catch (SQLException e) {
            System.err.println("Error fetching evaluations: " + e.getMessage());
        }
        return evaluations;
    }

    public boolean addEvaluation(Evaluation eval) {
        String sql = "INSERT INTO evaluations (project_id, component_name, max_marks, obtained_marks, evaluator_name, evaluation_date, comments) " +
                     "VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, eval.getProjectId());
            pstmt.setString(2, eval.getComponentName());
            pstmt.setDouble(3, eval.getMaxMarks());
            pstmt.setDouble(4, eval.getObtainedMarks());
            pstmt.setString(5, eval.getEvaluatorName());
            pstmt.setString(6, eval.getEvaluationDate() != null ? eval.getEvaluationDate() : java.time.LocalDate.now().toString());
            pstmt.setString(7, eval.getComments());
            return pstmt.executeUpdate() > 0;
        } catch (SQLException e) {
            System.err.println("Error adding evaluation: " + e.getMessage());
            return false;
        }
    }

    public Map<String, Object> getOverallSummary() {
        Map<String, Object> summary = new HashMap<>();
        String projSql = "SELECT " +
                         "COUNT(*) AS total_projects, " +
                         "SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed_projects, " +
                         "SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress_projects, " +
                         "SUM(CASE WHEN status = 'Under Review' THEN 1 ELSE 0 END) AS under_review_projects, " +
                         "SUM(CASE WHEN status = 'Proposed' THEN 1 ELSE 0 END) AS proposed_projects " +
                         "FROM projects";

        String avgSql = "SELECT AVG(obtained_marks) AS avg_mark FROM evaluations";

        try (Connection conn = DatabaseConnection.getConnection()) {
            try (PreparedStatement pstmt = conn.prepareStatement(projSql);
                 ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    summary.put("total_projects", rs.getInt("total_projects"));
                    summary.put("completed_projects", rs.getInt("completed_projects"));
                    summary.put("in_progress_projects", rs.getInt("in_progress_projects"));
                    summary.put("under_review_projects", rs.getInt("under_review_projects"));
                    summary.put("proposed_projects", rs.getInt("proposed_projects"));
                }
            }

            try (PreparedStatement pstmt = conn.prepareStatement(avgSql);
                 ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    summary.put("avg_mark", rs.getDouble("avg_mark"));
                }
            }
        } catch (SQLException e) {
            System.err.println("Error fetching summary stats: " + e.getMessage());
        }
        return summary;
    }
}
