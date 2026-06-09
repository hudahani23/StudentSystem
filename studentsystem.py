import json

students = []

def calculate_gpa(grades):
# Calculate GPA based on average grade
# Converts numerical average into a 4.0 scale system
    if not grades:
        return 0

    avg = sum(grades) / len(grades)
#conditions for the GPA,this is based off my university, you could change
    if avg >= 90:
        return 4.0
    elif avg >= 80:
        return 3.0
    elif avg >= 70:
        return 2.0
    elif avg >= 60:
        return 1.0
    else:
        return 0.0

#use dictionaries to store student info
def add_student():
    sid = input("Enter ID: ")
    name = input("Enter First Name: ")

    students.append({
        "id": sid,
        "name": name,
        "grades": []
        #create student record without any grade until the add_grade function is used
    })

    print("Student added!")


def add_grade():
# Add grade to an existing student
# Searches student by ID then appends grade
    sid = input("Enter student ID: ")

    for s in students:
        if s["id"] == sid:
            grade = float(input("Enter grade: "))
            s["grades"].append(grade)
            print("Grade added!")
            return

    print("Student not found!")


def show_students():
    if not students:
        print("No students found.")
        return

    for s in students:
        gpa = calculate_gpa(s["grades"])

        print("\nID:", s["id"])
        print("Name:", s["name"])
        print("Grades:", s["grades"])
        print("GPA:", gpa)


def search_student():
    sid = input("Enter student ID: ")

    for s in students:
        if s["id"] == sid:
            print("\nFOUND:")
            print("Name:", s["name"])
            print("Grades:", s["grades"])
            return

    print("Not found!")


def delete_student():
    sid = input("Enter student ID: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Deleted!")
            return

    print("Not found!")

def sort_by_gpa():
# Sort students by GPA in descending order
    if not students:
        print("No students found.")
        return

    sorted_students = sorted(
        students,
        key=lambda s: calculate_gpa(s["grades"]),
        reverse=True
    )

    print("\n===== SORTED BY GPA =====")

    rank = 1
    for s in sorted_students:
        print(f"\nRank {rank}")
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("GPA:", calculate_gpa(s["grades"]))
        rank += 1


def save_data():
    # Save all student data to a JSON file
    # Allows data persistence between program runs
    with open("students.json", "w") as f:
        json.dump(students, f)

    print("Data saved!")


def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []

def menu():
    load_data()

    while True:
        print("\n===== STUDENT SYSTEM =====")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Show Students")
        print("4. Search Student")
        print("5. Delete Student")
        print("6. Sort by GPA")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            show_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            sort_by_gpa()
        elif choice == "7":
            save_data()
        elif choice == "8":
            save_data()
            break
        else:
            print("Invalid choice!")


menu()
