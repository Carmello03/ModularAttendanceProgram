# Tadhg Carmody - R00237030
# Modular Programing Project - Modular Attendance Program

from Lecturer import Lecturer
from Semester2.Projects.Login import Login
from Useful_functions import error_message, file_check


def main():
    # Read login and module data from files
    username_list, password_list = read_file("login_data.txt")
    module_code_list, modules_list = read_file("Modules.txt")

    # Login and verify credentials
    lecture_login = Login(username_list, password_list)
    if lecture_login.login() == "Exit":
        error_message()
    else:
        # Enter lecturer menu
        while True:
            record_options = Lecturer(module_code_list, modules_list)
            record_options.create_modules()
            if record_options.record_system_options() == "Exit":
                error_message()
                break


# Read data from file and split into two lists
def read_file(file_name) -> (list, list):
    first_list = []
    second_list = []
    with file_check(file_name) as modules_connection:
        for line in modules_connection:
            line = line.rstrip()
            line_data = line.split(',')
            first_list.append(line_data[0])
            second_list.append(line_data[1])
    return first_list, second_list


if __name__ == "__main__":
    main()
