CREATE TABLE IF NOT EXISTS students
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT, -- primary key
    full_name  TEXT,                              -- full name of the student
    birth_year INTEGER                            -- year of birth
);

CREATE TABLE IF NOT EXISTS grades
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,         -- primary key
    student_id INTEGER,                                   -- foreign key (references student.id)
    subject    TEXT,                                      -- name of the subject
    grade      INTEGER CHECK ( grade BETWEEN 1 AND 100 ), -- grade between 1 and 100

    FOREIGN KEY (student_id) REFERENCES students (id)
);

-- index on students.full_name
CREATE INDEX IF NOT EXISTS idx_students_full_name ON students (full_name);

-- index on grades.student_id
CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades (student_id);

-- index on grades.subject
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades (subject);


-- insert sample students
INSERT INTO students (full_name, birth_year)
VALUES ('Alice Johnson', 2005),
       ('Brian Smith', 2004),
       ('Carla Reyes', 2006),
       ('Daniel Kim', 2005),
       ('Eva Thompson', 2003),
       ('Felix Nguyen', 2007),
       ('Grace Patel', 2005),
       ('Henry Lopez', 2004),
       ('Isabella Martinez', 2006);

-- insert sample grades
INSERT INTO grades (student_id, subject, grade)
VALUES (1, 'Math', 88),
       (1, 'English', 92),
       (1, 'Science', 85),
       (2, 'Math', 75),
       (2, 'History', 83),
       (2, 'English', 79),
       (3, 'Science', 95),
       (3, 'Math', 91),
       (3, 'Art', 89),
       (4, 'Math', 84),
       (4, 'Science', 88),
       (4, 'Physical Education', 93),
       (5, 'English', 90),
       (5, 'History', 85),
       (5, 'Math', 88),
       (6, 'Science', 72),
       (6, 'Math', 78),
       (6, 'English', 81),
       (7, 'Art', 94),
       (7, 'Science', 87),
       (7, 'Math', 90),
       (8, 'History', 77),
       (8, 'Math', 83),
       (8, 'Science', 80),
       (9, 'English', 96),
       (9, 'Math', 89),
       (9, 'Art', 92);


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
