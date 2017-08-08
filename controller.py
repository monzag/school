from school import School
from school_class import Class
import view
import class_controller


def main_menu():
    school = School.create_from_csv('school.csv')

    user_choice = None
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            view.get_list(school.get_all_teachers())

        elif user_choice == 2:
            print(school.get_best_class())

        elif user_choice == 3:
            choose_class(school)

        elif user_choice == 4:
            new_class = add_class(school)
            class_controller.class_menu(new_class)

        elif user_choice == 5:
            school.save_to_file()

    view.print_exit_message()


def choose_class(school):
    view.get_list(show_all_classes(school))
    class_name = view.get_class_name()
    for school_class in school.classes:
        if class_name.lower() == school_class.name:
            class_controller.class_menu(school_class)


def show_all_classes(school):
    class_names = []
    for school_class in school.classes:
        class_names.append(school_class.name)

    return class_names


def add_class(school):
    name = view.get_class_name()
    school_class = Class(name)
    school.add_class(school_class)

    return school_class

