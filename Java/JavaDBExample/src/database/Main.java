package database;
import java.util.Scanner;

import java.sql.*;
import java.util.concurrent.ExecutionException;

public class Main {
    public static void main(String[] args) throws Exception{
        Connection con = getConnection();
        Statement stmt = con.createStatement();
        String sql = "select * from actor";
        readRecords(sql,stmt);

        //write
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter First Name: ");
        String fName = sc.nextLine();
        System.out.print("Enter Last Name: ");
        String lName = sc.nextLine();
        String join = "Values ('" + fName + "', '" + lName + "')";

        sql = "INSERT INTO actor(first_name,last_name) " + join;
        System.out.println(sql);
        stmt.executeUpdate(sql);

        sql = "SELECT * FROM actor WHERE first_name = '" + fName + "' AND last_name = '" + lName + "'";
        System.out.println(sql);
        readRecords(sql,stmt);
    }

    private static Connection getConnection() throws Exception{
        try{
            String driver = "com.mysql.jdbc.Driver";
            String url = "jdbc:mysql://localhost:3306/sakila";
            String username = "root";
            String password = "2003";
            Class.forName(driver);

            Connection conn = DriverManager.getConnection(url,username,password);
            System.out.println("Connected");
            return conn;
        }catch(Exception e){
            e.printStackTrace();
        }

        return null;
    }
    private static void readRecords(String sql, Statement stmt) throws SQLException {
        ResultSet resultSet = stmt.executeQuery(sql);
        // ResultSet is initially before the first data set
        while (resultSet.next()) {

            String fname = resultSet.getString("first_name");
            String lname = resultSet.getString("last_name");
            Date date = resultSet.getDate("last_update");
            System.out.println("Name: " + fname + " " + lname + " " + date);

        }
    }
    private static void writeRecords() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter First Name: ");
        String fName = sc.nextLine();
        System.out.print("Enter Last Name: ");
        String lName = sc.nextLine();
        String join = "Values ('" + fName + "', '" + lName + "')";

        String sql = "INSERT INTO actor(first_name,last_name) " + join;
        System.out.println(sql);
        //stmt.executeUpdate(sql);
    }
    private static void latestRecords(ResultSet resultSet) throws SQLException {
        String fname = resultSet.getString("first_name");
        String lname = resultSet.getString("last_name");
        Date date = resultSet.getDate("last_update");
        System.out.println("Name: " + fname + " " + lname + " " + date);
    }

}
