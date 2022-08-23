import pyautogui

pyautogui.position()

for i in range(10):
    pyautogui.moveTo(2041, 438, duration=0.001)
    pyautogui.moveTo(2041, 438, duration=0.00001)
    pyautogui.click(2041, 438, button='left')

    try:
        while True:
            pyautogui.click(2041, 438, 10000, 0.000001,)
    except KeyboardInterrupt:
        print('\nГотово.')
 
