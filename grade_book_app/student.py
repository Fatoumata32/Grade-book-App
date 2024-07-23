from .course import Course

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def to_dict(self):
        return {
            "email": self.email,
            "names": self.names,
            "courses_registered": [{"course": c.to_dict(), "grade": g} for c, g in self.courses_registered],
            "GPA": self.GPA
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["email"], data["names"])
        student.courses_registered = [(Course.from_dict(c["course"]), c["grade"]) for c in data["courses_registered"]]
        student.GPA = data["GPA"]
        return student

    def register_for_course(self, course, grade):
        self.courses_registered.append((course, grade))

    def calculate_GPA(self):
        total_points = 0
        total_credits = 0
        for course, grade in self.courses_registered:
            total_points += grade * course.credits
            total_credits += course.credits
        self.GPA = total_points / total_credits if total_credits > 0 else 0.0
