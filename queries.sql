-- Create Table
CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    branch VARCHAR(20),
    cgpa FLOAT,
    skills VARCHAR(100),
    internship INT,
    projects INT,
    placement_status VARCHAR(15),
    company VARCHAR(50),
    package FLOAT
);

-- Placement Percentage
SELECT 
(COUNT(CASE WHEN placement_status='Placed' THEN 1 END)*100.0 / COUNT(*)) 
AS placement_percentage
FROM students;

-- Branch-wise Placement
SELECT branch,
COUNT(*) AS total_students,
SUM(CASE WHEN placement_status='Placed' THEN 1 ELSE 0 END) AS placed_students
FROM students
GROUP BY branch;

-- Average Package
SELECT AVG(package) 
FROM students 
WHERE placement_status='Placed';

-- Top 5 Students
SELECT * 
FROM students
ORDER BY package DESC
LIMIT 5;

-- Skill Demand
SELECT skills, COUNT(*) 
FROM students
WHERE placement_status='Placed'
GROUP BY skills;