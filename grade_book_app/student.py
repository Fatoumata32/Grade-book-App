class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        # TO DO: implement GPA calculation
        pass

    def register_for_course(self, course):
        self.courses_registered.append(course)
