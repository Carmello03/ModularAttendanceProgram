def message(string):
    print()
    print("Module Attendance Record System - {}".format(string))
    print("-" * 15)


def error_message():
    print("Exiting Module Record System")


def program_restart():
    print("Press enter to continue")
    input()


def file_check(file):
    try:
        return open(file)
    except OSError:
        print("Could not open/read file:")
        exit()


