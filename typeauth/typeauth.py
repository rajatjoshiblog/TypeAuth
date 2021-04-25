import keyboard
import sys
import pickle
import os

FILEPATH = os.path.dirname(os.path.abspath(__file__))

class UserCred:


    def __init__(self):
        try:
            db_file = open('dbstore/userdb.pickle',"rb")
            userdb_dict = pickle.load(db_file)
            db_file.close()
            self.db_dict = userdb_dict
        except:
            self.db_dict = {}


    def login_init(self):
        print("Select options:")
        print("(1) New user register")
        print("(2) Existing user - Login")
        print("(3) Exit")
        user_input = int(input("Enter your choice"))
        if user_input == 1:
            self.register_user()
        elif user_input == 2:
            self.login_main()
        else:
            sys.exit(0)

    def check_user(self, userid):
        usercheck = userid in self.db_dict.keys()
        return usercheck

    def check_pass(self, userid):
        return self.db_dict[userid]


    def login_main(self):

        # Input userid from system
        userid = input("Enter userid: ")
        # If user id exists, get userid and password for 
        # login validation
        if self.check_user(userid):
            password = input("Enter password: ")
            # Validate password from db
            hiddenpass = self.check_pass(userid)
            if password == hiddenpass:
                print("Login successful! Let's get you typing.")
            else:
                print("Incorrect Password, start again.")
                self.login_main()
        else:
            reg_true = input("User does not exists. Do you want to \
            register(Y/N): ")
            if reg_true.lower() == 'y':
                self.register_user()


    def register_user(self):
        newuserid = input("Choose a userid (only alphanumerics): ")
        if self.check_user(newuserid):
            print("userid already exist, try again")
            self.register_user()
        else:
            password = input("Choose a password: ")
            passvalidate = input("Confirm your password again: ")
            if password == passvalidate:
                print("password matched!")
                self.update_new_user(newuserid,password)
            else:
                print("Oops! Wrong password. Try again.")
                self.register_user()


    def update_new_user(self, userid: str, password: str):
        userdb_dict = self.db_dict
        userdb_dict[userid] = password
        db_file = open("dbstore/userdb.pickle","wb")
        pickle.dump(userdb_dict, db_file)
        db_file.close()

class KeyLogs:

    def __init__(self,key_logs):
        self.event_name = key_logs.name
        self.event_code = key_logs.scan_code
        self.event_time = key_logs.time


    def store_keylogs():
        pass


    def my_keyboard_hook(keyboard_event):
        print("Event Name: ",keyboard_event.name)
        print("Event Scan code: ",keyboard_event.scan_code)
        print("Event Time: ",keyboard_event.time)

def main():

    os.chdir(FILEPATH)
    #keyboard.hook(my_keyboard_hook)
    #keyboard.wait('esc')
    login_inst = UserCred()
    login_inst.login_init()

if __name__ == '__main__':
    main()
