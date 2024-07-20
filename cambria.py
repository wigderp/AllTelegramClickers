import pyautogui as pa
import pygetwindow as gw  # Assuming pygetwindow is imported as gw
import time

# Activate the window named 'Cambria - SunBrowser'
while True:
    sunbrowser_window = gw.getWindowsWithTitle('Cambria - SunBrowser')
    if sunbrowser_window:
        sunbrowser_window[0].activate()  # Activate the first window found with that title
    time.sleep(2)
    pa.click(958, 223)
    time.sleep(5)
    pa.click(694, 625)
    time.sleep(5)
    pa.click(1180, 901)
    time.sleep(5)
    