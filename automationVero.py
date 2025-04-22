import pyautogui
import time

time.sleep(5)
procurandoImagem = True

while procurandoImagem == True:
    try:
        img = pyautogui.locateCenterOnScreen('vero.png', confidence=0.5)
        if img:
            time.sleep(5)
            pyautogui.click(img.x,img.y)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(4)
            continue
    except:
        pyautogui.alert('Acabou patrao')
        break