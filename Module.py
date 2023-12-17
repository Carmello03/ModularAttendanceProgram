from Useful_functions import program_restart


class Module:
    def __init__(self, student_name_list, present_list, absent_list):
        self.student_name_list = student_name_list
        self.present_list = present_list
        self.absent_list = absent_list

    # for loop which loops through all students and gathers attendance data
    def students(self, module):
        print("There are {} in this module".format(len(self.student_name_list)))
        for i, student in enumerate(self.student_name_list):
            print("Student #{} - {}".format(i + 1, student))
            attendance_status = self.attendance_status()
            self.attendance_auth(attendance_status, i)
        self.student_attendance_updater(module)
        print("{}.txt was updated with the latest attendance records.".format(module))
        program_restart()

    # method to check if attendance input was set to 1 or 2 and validation while loop
    def attendance_status(self):
        attendance_status = input("[1] Present \n[2] Absent \n>")
        while attendance_status not in ["1", "2"] or not attendance_status.isnumeric():
            print("Wrong input received please enter either 1 or 2")
            attendance_status = input("[1] Present \n[2] Absent \n>")
        return attendance_status

    # method to set change values of absent/present lists
    def attendance_auth(self, attendance, position):
        if attendance == '1':
            self.present_list[position] += 1
        else:
            self.absent_list[position] += 1

    # method to write to file with updated attendance
    def student_attendance_updater(self, module):
        with open("{}.txt".format(module), 'w') as file:
            for i, item in enumerate(self.student_name_list):
                file.write("{},{},{}\n".format(item, self.present_list[i], self.absent_list[i]))
        pass
