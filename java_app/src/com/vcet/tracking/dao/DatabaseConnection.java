package com.vcet.tracking.dao;

import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * Database Connection Manager for SQLite.
 * Provides fresh connections compatible with try-with-resources.
 * Aligns with 25ITT31 (DBMS) and 25ITT32 (Java JDBC).
 */
public class DatabaseConnection {
    private static String databaseUrl = null;

    private DatabaseConnection() {}

    private static synchronized void initializeUrl() {
        if (databaseUrl != null) return;

        try {
            Class.forName("org.sqlite.JDBC");
        } catch (ClassNotFoundException e) {
            System.err.println("[!] SQLite JDBC Driver not found in classpath.");
        }

        // Search for tracking_system.db in candidate locations
        String[] possiblePaths = {
            "database/tracking_system.db",
            "../database/tracking_system.db",
            "../../database/tracking_system.db",
            "d:/project 1/database/tracking_system.db",
            "D:\\project 1\\database\\tracking_system.db"
        };

        String selectedPath = "database/tracking_system.db";
        for (String path : possiblePaths) {
            File f = new File(path);
            if (f.exists()) {
                selectedPath = f.getAbsolutePath();
                break;
            }
        }
        databaseUrl = "jdbc:sqlite:" + selectedPath;
    }

    public static Connection getConnection() throws SQLException {
        if (databaseUrl == null) {
            initializeUrl();
        }
        return DriverManager.getConnection(databaseUrl);
    }

    public static void closeConnection() {
        // Safe no-op for connection pool / individual connections
    }
}
