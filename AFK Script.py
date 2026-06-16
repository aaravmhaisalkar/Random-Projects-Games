import pyautogui as gui
import time
from pynput import keyboard

running = True

gui.PAUSE = .5
gui.FAILSAFE = True

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        running = False
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    time.sleep(.5)
    gui.moveTo(10,10,1)
    time.sleep(.5)
    gui.moveTo(1700,1000,1)

