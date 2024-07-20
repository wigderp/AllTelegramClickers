import os
import random
import time
from turtle import position
import pyautogui

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

print("Для выхода - Ctrl + C")

try:
    while True:
        x, y = pyautogui.position()
        os.system('cls')
        positionStr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)

        print(positionStr, end = '', flush=True)
        time.sleep(0.01)
        
except:
    os.system('cls')
    print("\nПрограмма завершена")
        