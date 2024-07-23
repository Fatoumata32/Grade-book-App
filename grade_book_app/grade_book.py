from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student, course):
        student.register_for_course(course)

    def calculate_GPA(self):
        # TO DO: implement GPA calculation for all students
        pass

    def calculate_ranking(self):
        # TO DO: implement ranking calculation
        pass

    def search_by_grade(self, grade_range):
        # TO DO: implement search by grade
        pass

    def generate_transcript(self, student):
        # TO DO: implement transcript generation
        pass
