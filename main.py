from XInput import *

import tkinter as tk
from tkinter import ttk

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

set_deadzone(DEADZONE_TRIGGER,10)

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Sensitivity Slider')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .1f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


# label for the slider
slider_label = ttk.Label(
    root,
    text='Sensitivity Slider:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = ttk.Scale(
    root,
    from_=10,
    to=50,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)

current_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)

while 1:

    sensitivity = float(get_current_value())
    
    events = get_events()
    for event in events:
        controller = event.user_index
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
                mouse.press(Button.left)
            elif event.button == "B": 
                mouse.click(Button.right,1)              
            elif event.button == "X":
                pass
            elif event.button == "Y":
                pass
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

    try:          
        root.update()
    except tk.TclError:
        break