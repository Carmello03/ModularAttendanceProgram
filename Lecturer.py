from Module import Module
from Useful_functions import message, file_check
from Statistics import Statistics


class Lecturer:
    def __init__(self, module_code_list, module_name_list):
        self.module_code_list = module_code_list
        self.module_name_list = module_name_list
        self.module_list = []

    # Reads data from module files and creates Module objects.
    def create_modules(self):
        for code in self.module_code_list:
            self.read_module_data('{}.txt'.format(code))

    # Reads data from a module file and creates a Module object.
    def read_module_data(self, file_name):
        student_name_list = []
        present_list = []
        absent_list = []
        with file_check(file_name) as choices_connection:
            for line in choices_connection:
                line = line.rstrip()
                line_data = line.split(',')
                student_name_list.append(line_data[0])
                present_list.append(int(line_data[1]))
                absent_list.append(int(line_data[2]))
            self.module_list.append(Module(student_name_list, present_list, absent_list))

    # Displays options to the user and performs the selected action.
    def record_system_options(self):
        message("Options")
        options = int(input("[1] Record Attendance \n[2] Generate Statistics \n[3] Exit \n>"))
        if options == 1:
            if self.record_attendance() == "Exit":
                return "Exit"
        elif options == 2:
            statistics_data = Statistics(self.module_code_list, self.module_name_list, self.module_list)
            statistics_data.generate_statistics()
        elif options == 3:
            return "Exit"
        else:
            print("Wrong input Received!")
            return "Exit"

    # Displays module options to the user and records attendance for the selected module.
    def record_attendance(self):
        message("Module")
        module = int(input("[1] {} \n[2] {} \n[3] {} \n>".format(self.module_code_list[0], self.module_code_list[1],
                                                                 self.module_code_list[2])))
        if module == 1:
            self.module_list[0].students(self.module_code_list[0])
        elif module == 2:
            self.module_list[1].students(self.module_code_list[1])
        elif module == 3:
            self.module_list[2].students(self.module_code_list[2])
        else:
            print("Wrong Input Received!")
            return "Exit"
