filepath = "students2.txt"

students = {}


def save_data():
    with open('students.txt', 'w') as f:
        for email, student_data in students.items():
            line = f"{email},{student_data['name']},{student_data['surname']},{student_data['points']},{student_data['grade']},{student_data['status']}\n"
            f.write(line)
    print("Data has been saved to file.")


with open(filepath, 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        email, name, surname, points = parts[:4]
        grade = parts[4] if len(parts) >= 5 else ''
        status = parts[5] if len(parts) >= 6 else ''
        if email not in students:
            students[email] = {'name': name, 'surname': surname, 'points': int(points), 'grade': grade,
                               'status': status}
        else:
            students[email]['points'] += int(points)

print(students)

for student in students.values():
    if student['status'] not in ('GRADED', 'MAILED'):
        if student['points'] >= 90:
            student['grade'] = '5.0'
        elif student['points'] >= 75:
            student['grade'] = '4.5'
        elif student['points'] >= 60:
            student['grade'] = '4.0'
        elif student['points'] >= 50:
            student['grade'] = '3.5'
        elif student['points'] >= 40:
            student['grade'] = '3.0'
        else:
            student['grade'] = '2.0'
        student['status'] = 'GRADED'
    save_data()

print(students)


def add_student(email, name, surname, points):
    if email in students:
        print(f"Student with email {email} already exists!")
    else:
        students[email] = {'name': name, 'surname': surname, 'points': int(points), 'grade': '', 'status': ''}
        print(f"Student {name} {surname} with email {email} and {points} points has been added.")
        save_data()


def remove_student(email):
    if email in students:
        del students[email]
        print(f"Student with email {email} has been removed.")
        save_data()
    else:
        print(f"Student with email {email} does not exist.")
