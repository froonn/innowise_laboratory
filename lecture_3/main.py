"""
Student Grade Analyzer

This script allows users to manage student data and analyze their grades.
Users can add students, input grades, generate reports, and find the top student based on average grades.

Features:
1. Add a new student
2. Add grades for a student
3. Generate a full report
4. Find the top student
5. Exit the program
"""

# List to store student data, where each student is represented as a dictionary with 'name' and 'grades' keys.
students: list[dict[str, list[int]]] = []

while True:
    try:
        # Display the menu options to the user.
        print('--- Student Grade Analyzer ---\n1. Add a new student\n2. Add grades for a student\n3. Generata a full report\n4. Find the top student\n5. Exit program')
        option = int(input('Enter your choice: '))
        print()
    except ValueError:
        # Handle invalid input for menu selection.
        print('Invalid input. Please enter a number.\n')
        continue

    if option == 1:
        # Option 1: Add a new student.
        student_name = input('Enter student name: ')
        if any(student['name'] == student_name for student in students):
            # Check if the student already exists.
            print(f'Student {student_name} already exists.\n')
        else:
            # Add a new student with an empty grades list.
            students.append({'name': student_name, 'grades': []})

    elif option == 2:
        # Option 2: Add grades for an existing student.
        student_name = input('Enter student name: ')
        student_founded = False
        for student in students:
            if student['name'] == student_name:
                student_founded = True
                while True:
                    grade = input('Enter a grade (or \'done\' to finish): ')
                    if grade == 'done':
                        # Exit the grade input loop.
                        break
                    try:
                        grade = int(grade)
                    except ValueError:
                        # Handle invalid grade input.
                        print('Invalid input. Please enter a number.')
                        continue
                    if 0 > grade or grade > 100:
                        # Ensure the grade is within the valid range.
                        print('Invalid input. Please enter a number between 0 and 100.')
                        continue
                    # Add the valid grade to the student's grades list.
                    student['grades'].append(grade)
                break
        if not student_founded:
            # Handle case where the student does not exist.
            print(f'Student {student_name} has not beed added.')

    elif option == 3:
        # Option 3: Generate a full report of students and their average grades.
        average_grades = []
        print('--- Student Report ---')
        for student in students:
            try:
                # Calculate and display the average grade for each student.
                average_grade = sum(student['grades']) / len(student['grades'])
                print(f'{student["name"]}\'s average grade is {average_grade:.1f}.')
                average_grades.append(average_grade)
            except ZeroDivisionError:
                # Handle case where a student has no grades.
                print(f'{student["name"]}\'s average grade is N/A.')

        # Display summary statistics for all students.
        if len(students) == 0:
            print('No students were added.')
        elif len(average_grades) == 0:
            print('No average grades were found.')
        else:
            print('-' * 40)
            print(f'Min Average: {min(average_grades):.1f}')
            print(f'Max Average: {max(average_grades):.1f}')
            print(f'Overall Average: {sum(average_grades) / len(average_grades):.1f}')

    elif option == 4:
        # Option 4: Find the student with the highest average grade.
        if len(students) == 0:
            print('No students were added.')
        else:
            # Find the student with the highest average grade.
            student_with_highest_average_grade = max(students,
                                                     key=lambda student: sum(student['grades']) / len(
                                                         student['grades']) if
                                                     student['grades'] else float('-inf'))
            if len(student_with_highest_average_grade['grades']) == 0:
                # Handle case where no grades were added for the top student.
                print('No grades were added.')
            else:
                print(
                    f'The student with the highest average grade is {student_with_highest_average_grade["name"]} with average grade of {sum(student_with_highest_average_grade["grades"]) / len(student_with_highest_average_grade["grades"]):.1f}')

    if option == 5:
        # Option 5: Exit the program.
        break

    print()