from Useful_functions import message, program_restart
from datetime import date


class Statistics:
    def __init__(self, module_code_list, module_name_list, module_list):
        self.module_code_list = module_code_list
        self.module_name_list = module_name_list
        self.module_list = module_list

    def generate_statistics(self):
        message("Average Attendance Data")
        attendance_avg_data = self.statistics_avg()

        most_attended_module_index = self.highest_attendance(attendance_avg_data)
        self.statistics_print(attendance_avg_data, self.attendance_stars(attendance_avg_data))

        print(
            "\nThe best attended module is {} with a {:.2f}% attendance rate."
            .format(self.module_name_list[most_attended_module_index], attendance_avg_data[most_attended_module_index]))

        low_list = self.low_attendance(attendance_avg_data)
        self.statistics_file_store(attendance_avg_data, most_attended_module_index, low_list)
        program_restart()

    # returns a list full of calculated averages for every module
    def statistics_avg(self):
        attendance_data = []
        for modules in self.module_list:
            if sum(modules.present_list) > 0 or sum(modules.absent_list) > 0:
                attendance_data.append(
                    (sum(modules.present_list) / (sum(modules.present_list) + sum(modules.absent_list))) * 100)
            else:
                attendance_data.append(0)
        return attendance_data

    def attendance_stars(self, average_list):
        attendance_stars = []
        for i in average_list:
            attendance_stars.append(int(i / 10) * '*')
        return attendance_stars

    # prints the average statistics data
    def statistics_print(self, average_list, attendance_stars):
        for i, module in enumerate(self.module_name_list):
            print(f"{module:27}{self.module_code_list[i]:^10}{average_list[i]:^8.2f}{attendance_stars[i]:>13}")

    # method that takes in list and returns the highest in the list
    def highest_attendance(self, average_list):
        for i, average in enumerate(average_list):
            if max(average_list) == average:
                return i

    # method takes in average list and returns a list of attendances bellow 40
    def low_attendance(self, average_list):
        low_attendance_list = []
        for average in average_list:
            if average < 40:
                low_attendance_list.append(average_list.index(average))
        self.low_attendance_print(low_attendance_list)
        return low_attendance_list

    # prints low attendance list
    def low_attendance_print(self, low_attendance_list):
        if len(low_attendance_list) == 1:
            print("There is 1 module with attendance under 40%:")
        else:
            print("There are {} modules with attendance under 40%:".format(len(low_attendance_list)))
        for low_a in low_attendance_list:
            print("  {}\n".format(self.module_name_list[low_a]))

    # creates a file and stores the created statistics data
    def statistics_file_store(self, average_list, most_attended_module_index, low_attendance_list):
        today = date.today()
        day = today.strftime("%d_%m_%Y")
        file = open("Attendance_Stats_{}.txt".format(day), "w")
        for index in range(len(average_list)):
            file.write(str(self.module_name_list[index]) + " - " + str("{:.2f}").format(average_list[index]) + "\n")
        file.write(str("\nThe best attended module is {} with a {:.2f}% attendance rate.\n"
                       .format(self.module_name_list[most_attended_module_index],
                               average_list[most_attended_module_index])))
        if len(low_attendance_list) == 0:
            file.write(str("\nThere are no modules with attendance bellow 40%"))
        else:
            file.write(str("\nThe modules with attendance under 40% are: "))
            for low_a in low_attendance_list:
                file.write(str("\n  {}".format(self.module_name_list[low_a])))
        file.close()
        print("\nThe above data is also stored at Attendance_Stats_{}".format(day))

