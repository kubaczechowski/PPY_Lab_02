from LinkedList import MyLinkedList

filepath = "students2.txt"

students = MyLinkedList()


def save_data():
    with open('students.txt', 'w') as f:
        current = students.head
        while current:
            email = current.data[0]
            name = current.data[1]
            surname = current.data[2]
            points = current.data[3]
            grade = current.data[4]
            status = current.data[5]
            line = f"{email},{name},{surname},{points},{grade},{status}\n"
            f.write(line)
            current = current.nextE
    print("Data has been saved to file.")


with open(filepath, 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        email, name, surname, points = parts[:4]
        grade = parts[4] if len(parts) >= 5 else ''
        status = parts[5] if len(parts) >= 6 else ''
        data = [email, name, surname, int(points), grade, status]
        students.append(data)

print(students)

current = students.head
while current:
    student = current.data
    if student[5] not in ('GRADED', 'MAILED'):
        if student[3] >= 90:
            student[4] = '5.0'
        elif student[3] >= 75:
            student[4] = '4.5'
        elif student[3] >= 60:
            student[4] = '4.0'
        elif student[3] >= 50:
            student[4] = '3.5'
        elif student[3] >= 40:
            student[4] = '3.0'
        else:
            student[4] = '2.0'
        student[5] = 'GRADED'
    current = current.nextE
save_data()

print(students)


def add_student(email, name, surname, points):
    current = students.head
    while current:
        if current.data[0] == email:
            print(f"Student with email {email} already exists!")
            return
        current = current.nextE
    data = [email, name, surname, int(points), '', '']
    students.append(data)
    print(f"Student {name} {surname} with email {email} and {points} points has been added.")
    save_data()


def remove_student(email):
    students.delete((email, None))
    save_data()
    print(f"Student with email {email} has been removed.")
