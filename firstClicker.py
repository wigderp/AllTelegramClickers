import pyautogui
import random
import keyboard
import time

while True:
    x = random.randint(1547, 1908)
    y = random.randint(196, 600)
    
    pyautogui.mouseDown(x, y)
    time.sleep(0.00001)
    pyautogui.mouseUp(x, y)
    
    if keyboard.is_pressed("Esc"):
        break