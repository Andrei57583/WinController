from XInput import *

import tkinter as tk

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

set_deadzone(DEADZONE_TRIGGER,10)

sensitivity = 25

while 1:
    events = get_events()
    for event in events:
        controller = event.user_index
        #print(get_battery_information(controller))
        if event.type == EVENT_CONNECTED:
            print(f"Controller {controller} is now connected!")

        elif event.type == EVENT_DISCONNECTED:
            print(f"Controller {controller} is now disconnected!")

        elif event.type == EVENT_STICK_MOVED:
            if event.stick == LEFT:
                l_stick_pos = (int(round(sensitivity * event.x, 0)), int(round(sensitivity * event.y, 0)))
                mouse.move(l_stick_pos[0],-1 * l_stick_pos[1])

            elif event.stick == RIGHT:
                r_stick_pos = (int(round(event.x, 0)), int(round(event.y,0)))
                mouse.scroll(r_stick_pos[0],r_stick_pos[1])

        elif event.type == EVENT_TRIGGER_MOVED:
            if event.trigger == LEFT:
                pass                
            elif event.trigger == RIGHT:
                pass

        elif event.type == EVENT_BUTTON_PRESSED:
            
            if event.button == "A":
                print(f"{event.button}")
                #mouse.click(Button.left,1)
                mouse.press(Button.left)
            elif event.button == "B":
                print(f"{event.button}")  
                mouse.click(Button.right,1)              
            elif event.button == "X":
                print(f"{event.button}")
            elif event.button == "Y":
                print(f"{event.button}")
            elif event.button == "DPAD_LEFT":
                mouse.move(-1 * sensitivity, 0)
            elif event.button == "DPAD_RIGHT":
                mouse.move(1 * sensitivity, 0)
            elif event.button == "DPAD_UP":
                mouse.move(0 ,-1 * sensitivity)
            elif event.button == "DPAD_DOWN":
                mouse.move(0 ,1 * sensitivity)

        elif event.type == EVENT_BUTTON_RELEASED:
            if event.button == "A":
                mouse.release(Button.left)
