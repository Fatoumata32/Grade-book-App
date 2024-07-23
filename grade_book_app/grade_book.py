import json
import os
from .student import Student
from .course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.file_name = "grade_book_data.json"

    def add_student(self, student):
        self.student_list.append(student)
        self.save_data()

    def add_course(self, course):
        self.course_list.append(course)
        self.save_data()

    def register_student_for_course(self, student, course, grade):
        student.register_for_course(course, grade)
        self.save_data()

    def save_data(self):
        data = {
            "students": [s.to_dict() for s in self.student_list],
            "courses": [c.to_dict() for c in self.course_list]
        }
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.student_list = [Student.from_dict(d) for d in data["students"]]
                self.course_list = [Course.from_dict(d) for d in data["courses"]]

    def calculate_ranking(self):
        for student in self.student_list:
            student.calculate_GPA()
        self.student_list.sort(key=lambda student: student.GPA, reverse=True)
        return self.student_list

    def search_by_grade(self, grade_range):
        grade_min, grade_max = map(float, grade_range.split('-'))
        result = [student for student in self.student_list if any(grade_min <= grade <= grade_max for _, grade in student.courses_registered)]
        return result

    def generate_transcript(self, student):
        transcript = f"Transcript for {student.names} ({student.email}):\n"
        for course, grade in student.courses_registered:
            transcript += f"  {course.name}: {grade}\n"
        transcript += f"GPA: {student.GPA:.2f}\n"
        print(transcript)
