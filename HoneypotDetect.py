import ctypes
import random
import time
import sys

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

keystrokes = 0
mouse_clicks = 0
double_clicks = 0

class UserDefinedInput(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("dwTime", ctypes.c_ulong)]

def last_inputs():
    struct_UserDefinedInput = UserDefinedInput()
    struct_UserDefinedInput.cbSize = ctypes.sizeof(UserDefinedInput)
    user32.GetUserDefinedInput(ctypes.byref(struct_UserDefinedInput))
    run_time = kernel32.GetTickCount()
    elapsed = run_time - struct_UserDefinedInput.dwTime
    return elapsed

def key_presses():
    global mouse_clicks
    global keystrokes
    for i in range(0, 0xff):
        if user32.GetAsyncKeyState(i) == -32767:
            if i == 0x1:
                mouse_clicks += 1
                return time.time()
            elif i > 32 and i < 127:
                keystrokes += 1

def detect_non_interaction():
    global mouse_clicks
    global keystrokes
    max_keystrokes = random.randint(10, 25)
    max_mouse_clicks = random.randint(5, 25)
    double_clicks = 0
    max_double_clicks = 10
    double_click_threshold = 0.250
    first_double_click = None
    average_mousetime = 0
    max_input_threshold = 30000
    previous_timestamp = None
    detection_complete = False
    last_input = last_inputs()
    if last_input >= max_input_threshold:
        sys.exit(0)
    while not detection_complete:
        keypress_time = key_presses()
        if keypress_time is not None and previous_timestamp is not None:
            elapsed = keypress_time - previous_timestamp
            if elapsed < double_click_threshold:
                double_clicks += 1
                if first_double_click is None:
                    first_double_click = time.time()
                else:
                    if double_clicks == max_double_clicks:
                        if keypress_time - first_double_click <= (max_double_clicks * double_click_threshold):
                            print "Exceeded Threshold"
                            sys.exit(0)
            if keystrokes >= max_keystrokes and double_clicks >= max_double_clicks and mouse_clicks >= max_mouse_clicks:
                return
            previous_timestamp = keypress_time
        elif keypress_time is not None:
            previous_timestamp = keypress_time

detect_non_interaction()
