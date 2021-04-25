import os
from keylogs import KeyLogs
from usercred import UserCred

FILEPATH = os.path.dirname(os.path.abspath(__file__))

def main():

    os.chdir(FILEPATH)
    #keyboard.hook(my_keyboard_hook)
    #keyboard.wait('esc')
    login_inst = UserCred()
    login_inst.login_init()

if __name__ == '__main__':
    main()
