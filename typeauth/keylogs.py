import keyboard

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

