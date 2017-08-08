def print_main_menu():
    options = ['Show all teachers', 'Get best classes', 'Choose class', 'Add class', 'Save to file']
    get_list(options)
    print_exit_option()


def get_list(options):
    print('')
    number = 1
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1
    print('')


def print_exit_option():
    print('0. Exit\n')


def get_user_input():
    number = input('\nProvide number: ')
    if number.isdigit():
        return int(number)

    return None


def get_class_name():
    return input('Choose school class: ')


def print_exit_message():
    print('\nGood bye:) ')


def print_class_menu():
    options = ['Show best student', 'Show average of class', 'Show subjects', 'Add teacher', 'Remove teacher',
               'Add student', 'Remove student', 'Show all students', 'Show teacher', 'Choose student']

    get_list(options)
    print_exit_option()


def get_new_person():
    first_name = input('Type first_name: ')
    last_name = input('Type last_name: ')

    return first_name, last_name


def get_new_class():
    return input('Type class name: ')


def print_student_menu():
    options = ['Show grades', 'Add grade']

    get_list(options)
    print_exit_option()



