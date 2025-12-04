-- Find all grades for a specific student (Alice Johnson)
SELECT grades.grade
FROM students
         JOIN grades ON students.id = grades.student_id
WHERE students.full_name = 'Alice Johnson';

-- Calculate the average grade per student
SELECT students.full_name, AVG(grades.grade)
FROM students
         JOIN grades ON students.id = grades.student_id
GROUP BY students.id;

-- List all students born after 2004
SELECT students.full_name
FROM students
WHERE students.birth_year > 2004;

-- Create a query that lists all subjects and their average grades
SELECT grades.subject, AVG(grades.grade)
FROM grades
GROUP BY grades.subject;

-- Find the top 3 students with the highest average grades
SELECT students.full_name
FROM students
         JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 3;

-- Show all students who have scored below 80 in any subject
SELECT students.full_name
FROM students
         JOIN grades ON students.id = grades.student_id
GROUP BY students.id
HAVING MIN(grades.grade) < 80;
