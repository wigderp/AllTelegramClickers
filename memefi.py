import time
import pyautogui
import random

total_click_time = 0  # Суммарное время кликов

while True:
    
    # Кликаем 9 минут или до достижения 29 минут
    start_time = time.time()
    while (time.time() - start_time) < 9 * 60:
        x = 1674 + random.randint(-10, 10)
        y = 385 + random.randint(-10, 10)
        pyautogui.click(x, y)
        total_click_time += 1
        if total_click_time >= 29 * 60:
            exit()  # Выходим из программы, если прокликано 29 минут
    