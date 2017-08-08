from school_class import Class
from teacher import Teacher
from student import Student
import csv


class School:
    name = ''

    def __init__(self):
        self.classes = []

    def get_best_class(self):
        highest_average = 0
        best_class = ''
        for school_class in self.classes:
            if school_class.get_average_grade() > highest_average:
                highest_average = school_class.get_average_grade()
                best_class = school_class.name

        return 'Best class {} with average {}'.format(best_class, highest_average)

    def get_all_teachers(self):
        all_teachers = []
        for school_class in self.classes:
            for teacher in school_class.teachers:
                if teacher.get_full_name() not in all_teachers:
                    all_teachers.append(teacher.get_full_name())

        return all_teachers

    def add_class(self, school_class):
        self.classes.append(school_class)

    @classmethod
    def create_from_csv(cls, csv_path):
        splitted_data = cls.get_data_from_file(csv_path)

        # first data in csv file is school name
        school_name = splitted_data[0][0]
        School.name = school_name
        school = School()

        for row in splitted_data[1:]:

            if len(row) == 1:
                school_class = School.create_class(row, school)

            else:
                first_name, last_name = row[0], row[1]
                subject = row[2]

                if subject.isalpha():
                    School.create_teacher(first_name, last_name, row, school_class)

                else:
                    School.create_student(first_name, last_name, row, school_class)

        return school

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip().split(',') for line in csvfile]

        return splitted_rows

    @classmethod
    def create_class(cls, row, school):
        class_name = row[0]
        school_class = Class(class_name)
        school.add_class(school_class)

        return school_class

    @classmethod
    def create_teacher(cls, first_name, last_name, row, school_class):
        teacher = Teacher(first_name, last_name)

        for subject in row[2:]:
            teacher.add_subject(subject)

        school_class.add_teacher(teacher)

    @classmethod
    def create_student(cls, first_name, last_name, row, school_class):
        student = Student(first_name, last_name)
        for grade in row[2:]:
            student.add_grade(grade)

        school_class.add_student(student)

    def save_to_file(self):
        list_to_save = self.get_data_to_save()
        file_path = self.name + '.csv'

        with open(file_path, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for line in list_to_save:
                writer.writerow(line)

    def get_data_to_save(self):
        list_to_save = []
        list_to_save.append([School.name])

        for school_class in self.classes:
            list_to_save.append([school_class.name])

            for teacher in school_class.teachers:
                first_name, last_name = teacher.first_name, teacher.last_name
                row = [first_name, last_name]

                for subject in teacher.subjects:
                    row.append(subject)

                list_to_save.append(row)

            for student in school_class.students:
                first_name, last_name = student.first_name, student.last_name
                row = [first_name, last_name]

                for grade in student.grades:
                    row.append(grade)

                list_to_save.append(row)

        return list_to_save

