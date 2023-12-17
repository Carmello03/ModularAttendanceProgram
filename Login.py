from Useful_functions import message


class Login:
    def __init__(self, username_list, password_list):
        self.username_list = username_list
        self.password_list = password_list

    def login(self):
        message("login")
        print("Please enter your login details below")
        username = input("Username: ")
        username_auth = self.check_valid_username(username)
        if username_auth == "Exit":
            return "Exit"
        password = input("Password: ")
        password_auth = self.check_valid_password(username, password)
        if password_auth == "Exit":
            return "Exit"

    # method to check if length of username is less or equal to 0
    def check_valid_username(self, username) -> str:
        while len(username) <= 0:
            print("Username must be at least 1 character long")
            username = input("Username: ")
        if not self.username_authenticator(username):
            return "Exit"
        return username

    # method to check if username is in list of usernames
    def username_authenticator(self, username):
        if username in self.username_list:
            return True
        else:
            print("The User {} you are looking for does not exist".format(username))

    # method to check if length of password is less or equal to 0
    def check_valid_password(self, username, password) -> str:
        while len(password) <= 0:
            print("Password must be at least 1 character long")
            password = input("Password: ")
        if not self.authenticator_password(username, password):
            return "Exit"
        return password

    # method to heck if password is the right password for username used
    def authenticator_password(self, username, password):
        if password == self.password_list[self.username_list.index(username)]:
            print("\nWelcome {} to the Attendance Record System".format(username))
            return True
        else:
            print("The password you have entered for the user {} is wrong".format(username))



