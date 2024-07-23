def main():
    grade_book = GradeBook()

    while True:
        print("Choose an action:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            grade_book.add_student(student)
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            grade_book.add_course(course)
        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            student = next((s for s in grade_book.student_list if s.email == student_email), None)
            course = next((c for c in grade_book.course_list if c.name == course_name), None)
            if student and course:
                grade_book.register_student_for_course(student, course)
            else:
                print("Student or course not found")
        elif choice == "4":
            grade_book.calculate_ranking()
        elif choice == "5":
            grade_range = input("Enter grade range: ")
            grade_book.search_by_grade(grade_range)
        elif choice == "6":
            student_email = input("Enter student email: ")
            student = next((s for s in grade_book.student_list if s.email == student_email), None)
            if student:
                grade_book.generate_transcript(student)
            else:
                print("Student not found")
        elif choice == "7":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
