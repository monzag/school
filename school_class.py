from student import Student


class Class:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def get_best_student(self):
        highest_average = 0
        best_student = ''
        for student in self.students:
            if student.get_average_grades() > highest_average:
                highest_average = student.get_average_grades()
                best_student = student.get_full_name()

        return 'Best student is {} with average {}'.format(best_student, highest_average)

    def get_average_grade(self):
        sum_all_average = 0
        if len(self.students) > 0:
            for student in self.students:
                sum_all_average += student.get_average_grades()

            return sum_all_average / len(self.students)

        else:
            return sum_all_average

    def get_class_subjects(self):
        class_subjects = []
        for teacher in self.teachers:
            subjects = teacher.subjects
            class_subjects.append(subjects)

        return class_subjects

    def sort_students(self, attr='alphabetically'):
        is_sorted = False
        while not is_sorted and len(self.students) > 1:
            is_sorted = True
            for index in range(len(self.students) - 1):
                if attr == 'alphabetically':
                    if self.students[index].get_full_name() > self.students[index + 1].get_full_name():
                        self.get_alghoritm_to_sort(index)

                # sort by average
                else:
                    if self.students[index].get_average_grades() > self.students[index + 1].get_average_grades():
                        self.get_alghoritm_to_sort(index)

            return self.students

    def get_alghoritm_to_sort(self, index):
        temp = self.students[index]
        self.students[index] = self.students[index + 1]
        self.students[index + 1] = temp
        is_sorted = False

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, user_choice):
        if user_choice in range(len(self.teachers)):
            del(self.teachers[user_choice])

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, user_choice):
        if user_choice in range(len(self.students)):
            del(self.students[user_choice])


