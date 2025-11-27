students: list[dict[str, list[int]]] = []

while True:
    try:
        print('--- Student Grade Analyzer ---\n1. Add a new student\n2. Add grades for a student\n3. Generata a full report\n4. Find the top student\n5. Exit program')
        option = int(input('Enter your choice: '))
        print()
    except ValueError:
        print('Invalid input. Please enter a number.\n')
        continue

    if option == 1:
        student_name = input('Enter student name: ')
        if any(student['name'] == student_name for student in students):
            print(f'Student {student_name} already exists.\n')
        else:
            students.append({'name': student_name, 'grades': []})

    elif option == 2:
        student_name = input('Enter student name: ')
        student_founded = False
        for student in students:
            if student['name'] == student_name:
                student_founded = True
                while True:
                    grade = input('Enter a grade (or \'done\' to finish): ')
                    if grade == 'done':
                        break
                    try:
                        grade = int(grade)
                    except ValueError:
                        print('Invalid input. Please enter a number.')
                        continue
                    if 0 > grade or grade > 100:
                        print('Invalid input. Please enter a number between 0 and 100.')
                        continue
                    student['grades'].append(grade)
                break
        if not student_founded:
            print(f'Student {student_name} has not beed added.')

    elif option == 3:
        average_grades = []
        print('--- Student Report ---')
        for student in students:
            try:
                average_grade = sum(student['grades']) / len(student['grades'])
                print(f'{student["name"]}\'s average grade is {average_grade:.1f}.')
                average_grades.append(average_grade)
            except ZeroDivisionError:
                print(f'{student["name"]}\'s average grade is N/A.')

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
        if len(students) == 0:
            print('No students were added.')
        else:
            student_with_highest_average_grade = max(students,
                                                     key=lambda student: sum(student['grades']) / len(
                                                         student['grades']) if
                                                     student['grades'] else float('-inf'))
            if len(student_with_highest_average_grade['grades']) == 0:
                print('No grades were added.')
            else:
                print(
                    f'The student with the highest average grade is {student_with_highest_average_grade["name"]} with average grade of {sum(student_with_highest_average_grade["grades"]) / len(student_with_highest_average_grade["grades"]):.1f}')

    if option == 5:
        break

    print()
