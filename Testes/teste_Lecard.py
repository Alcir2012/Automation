import pyautogui
import time


pegando_arquivos =  'sim'
time.sleep(3)
while pegando_arquivos == 'sim':
    try:
        pyautogui.click(x=-1078, y=474)
        time.sleep(2)
        pyautogui.click(x=-1404, y=299)
        time.sleep(2)
    except:
        img = pyautogui.locateCenterOnScreen("lecard.png", confidence=0.7)
        break