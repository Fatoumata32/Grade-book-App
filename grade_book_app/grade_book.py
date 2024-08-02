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

    def register_student_for_course(self, student, course):
        student.register_for_course(course)
        self.save_data()

    def save_data(self):
        data = {
            "students": [s.to_dict() for s in self.student_list],
            "courses": [c.to_dict() for c in self.course_list]
        }
        with open(self.file_name, "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.student_list = [Student.from_dict(d) for d in data["students"]]
                self.course_list = [Course.from_dict(d) for d in data["courses"]]

    def calculate_ranking(self):
        # TO DO: implement GPA calculation
        pass

    def search_by_grade(self, grade_range):
        # TO DO: implement search by grade
        pass

    def generate_transcript(self, student):
        # TO DO: implement transcript generation
        pass
