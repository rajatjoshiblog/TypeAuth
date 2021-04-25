import keyboard
import sys


def my_keyboard_hook(keyboard_event):
     print("Event Name: ",keyboard_event.name)
     print("Event Scan code: ",keyboard_event.scan_code)
     print("Event Time: ",keyboard_event.time)

def main():
    keyboard.hook(my_keyboard_hook)
    keyboard.wait('esc')

if __name__ == '__main__':
    main()
