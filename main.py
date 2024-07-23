from grade_book_app.grade_book import GradeBook
from grade_book_app.student import Student
from grade_book_app.course import Course

def main():
    grade_book = GradeBook()
    grade_book.load_data()

    while True:
        print("Choose an action:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Display student information")
        print("5. Display course information")
        print("6. Calculate ranking")
        print("7. Search by grade")
        print("8. Generate transcript")
        print("9. Quit")

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
            grade = float(input("Enter grade: "))
            student = next((s for s in grade_book.student_list if s.email == student_email), None)
            course = next((c for c in grade_book.course_list if c.name == course_name), None)
            if student and course:
                grade_book.register_student_for_course(student, course, grade)
            else:
                print("Student or course not found")
        elif choice == "4":
            student_email = input("Enter student email: ")
            student = next((s for s in grade_book.student_list if s.email == student_email), None)
            if student:
                print(f"{student.names} ({student.email})")
                for course, grade in student.courses_registered:
                    print(f"  {course.name} ({course.trimester} {course.credits} credits) - Grade: {grade}")
            else:
                print("Student not found")
        elif choice == "5":
            course_name = input("Enter course name: ")
            course = next((c for c in grade_book.course_list if c.name == course_name), None)
            if course:
                print(f"{course.name} ({course.trimester} {course.credits} credits)")
            else:
                print("Course not found")
        elif choice == "6":
            ranking = grade_book.calculate_ranking()
            for student in ranking:
                print(f"{student.names}: {student.GPA:.2f}")
        elif choice == "7":
            grade_range = input("Enter grade range (min-max): ")
            students = grade_book.search_by_grade(grade_range)
            for student in students:
                print(student.names)
        elif choice == "8":
            student_email = input("Enter student email: ")
            student = next((s for s in grade_book.student_list if s.email == student_email), None)
            if student:
                grade_book.generate_transcript(student)
            else:
                print("Student not found")
        elif choice == "9":
            break
        else:
            print("Invalid choice")

    grade_book.save_data()

if __name__ == "__main__":
    main()
