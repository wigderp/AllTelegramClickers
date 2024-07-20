import pyautogui as pa
import keyboard

while True:
    if keyboard.is_pressed("Z"):
        pa.click()
    
    if keyboard.is_pressed("Esc"):
        break