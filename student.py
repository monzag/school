from person import Person


class Student(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def get_average_grades(self):
        return sum(int(grade) for grade in self.grades) / len(self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)
