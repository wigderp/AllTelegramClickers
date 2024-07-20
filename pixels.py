import pyautogui as pa
import random
import keyboard
import time
import schedule

def step1():
    # это для простых кликов
        x = random.randint(1650, 1770)
        y = random.randint(728, 755)

        pa.moveTo(x, y, duration=0.25)
        pa.click()
        time.sleep(10)
    
def step2():
    # это для захода в магазин
        x1 = random.randint(1616, 1657)
        y1 = random.randint(837, 863)
    
        pa.moveTo(x1, y1, duration=0.474)
        pa.click()
        #time.sleep(1.26)
    
    # выбор 2х буста
        #x2 = random.randint(1496, 1739)
        #y2 = random.randint(470, 525)
    
        #pa.moveTo(x2, y2, duration=0.6284)
        #pa.click()
        
    # выбор 3х буста
        x4 = random.randint(1442, 1731)
        y4 = random.randint(585, 677)
    
        pa.moveTo(x4, y4, duration=0.6284)
        pa.click()
    
    # покупка буста
        x3 = random.randint(1517, 1702)
        y3 = random.randint(789, 813)
    
        pa.moveTo(x3, y3, duration=0.836)
        pa.click()
        print("Буст куплен!")
        time.sleep(1)

schedule.every(4).minutes.do(step2)
print("Программа начала работать, таймер в 4 секунды запущен ыыы")

while True:
    schedule.run_pending()
    step1()
    time.sleep(1)