filepath = "students2.txt"
studentsDict = {}


def add_grades_for_students_who_dont_have_them(students_dict):
    for email in students_dict:
        if email in students_dict and "grade" not in students_dict[email]:
            #here is the problem...
            students_dict[email] = {"grade": students_dict[email]["punkty"] < 75 if "GOOD" else "VERY GOOD"}


with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())
        parts = line.strip().split(",")
        if len(parts) == 4:
            email, imie, nazwisko, punkty = parts
            studentsDict[email] = {
                "imie": imie,
                "nazwisko": nazwisko,
                "punkty": int(punkty),
            }
        elif len(parts) == 5:
            email, imie, nazwisko, punkty, grade = parts
            studentsDict[email] = {
                "imie": imie,
                "nazwisko": nazwisko,
                "punkty": int(punkty),
                "grade": grade
            }

add_grades_for_students_who_dont_have_them(studentsDict)

with open("students.txt", "w") as file:
    for email, student in studentsDict.items():
        print(student)
        #line = f"{email},{student['imie']},{student['nazwisko']},{student['punkty']}\n"
        file.write(line)
