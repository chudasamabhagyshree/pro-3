students = []

while True:
    print("\n--- Student Data Organizer ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        subjects = input("Enter Subjects: ")

        student = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Grade": grade,
            "DOB": dob,
            "Subjects": subjects
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        for student in students:
            if student["ID"] == student_id:
                student["Name"] = input("Enter New Name: ")
                student["Age"] = input("Enter New Age: ")
                print("Student updated successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Subjects Offered:")
        print("1. Mathematics")
        print("2. Science")
        print("3. English")
        print("4. Computer")

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")