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