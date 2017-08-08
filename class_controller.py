from school_class import Class
from teacher import Teacher
from student import Student
import student_controller
import view


def class_menu(school_class):
    user_choice = ''
    while user_choice != 0:
        view.print_class_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            print(school_class.get_best_student())

        elif user_choice == 2:
            print(school_class.get_average_grade())

        elif user_choice == 3:
            view.get_list(school_class.get_class_subjects())

        elif user_choice == 4:
            add_teacher(school_class)

        elif user_choice == 5:
            remove_teacher(school_class)

        elif user_choice == 6:
            add_student(school_class)

        elif user_choice == 7:
            remove_student(school_class)

        elif user_choice == 8:
            show_all_students(school_class)

        elif user_choice == 9:
            show_teachers(school_class)

        elif user_choice == 10:
            choose_student(school_class)

        elif user_choice == 11:
            # choose teacher
            pass


def show_all_students(school_class):
    all_student_names = []
    school_class.sort_students()
    for student in school_class.students:
        all_student_names.append(student.get_full_name())

    view.get_list(all_student_names)


def show_teachers(school_class):
    all_teacher_names = []
    for teacher in school_class.teachers:
        all_teacher_names.append(teacher.get_full_name())

    view.get_list(all_teacher_names)


def add_teacher(school_class):
    first_name, last_name = view.get_new_person()
    teacher = Teacher(first_name, last_name)
    school_class.add_teacher(teacher)


def remove_teacher(school_class):
    show_teachers()
    user_choice = view.get_user_input()
    school_class.remove_teacher(user_choice)


def add_student(school_class):
    first_name, last_name = view.get_new_person()
    student = Student(first_name, last_name)
    school_class.add_student(student)


def remove_student(school_class):
    show_all_students(school_class)
    user_choice = view.get_user_input()
    school_class.remove_student(user_choice)


def choose_student(school_class):
    show_all_students(school_class)
    user_choice = view.get_user_input()
    if user_choice in range(len(school_class.students)):
        student = school_class.sort_students()[user_choice]
        student_controller.student_menu(student)

