from person import Person


class Teacher(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

