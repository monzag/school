from student import Student
import view


def student_menu(student):
    print(student.get_full_name())

    user_choice = ''
    while user_choice != 0:
        view.print_student_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            show_grades(student)

        elif user_choice == 2:
            grade = view.get_user_input()
            student.add_grade(grade)


def show_grades(student):
    for grade in student.grades:
        print(grade)

