import pyautogui
import time

pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.write('WinScp')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(23)

procurando_imagem = 'sim'

while procurando_imagem == 'sim':
    try:
        img = pyautogui.locateCenterOnScreen('tela.png', confidence=0.7)
        pyautogui.click(img.x,img.y)
        time.sleep(30)

    except:
        time.sleep(30)
        print("não encontrei")