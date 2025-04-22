import pyautogui
import time

time.sleep(10)
pyautogui.click(x=381, y=609)
time.sleep(1)
pyautogui.write('processados')
time.sleep(1)
pyautogui.click(x=381, y=609)
time.sleep(1)
pyautogui.hotkey('ctrl','a')
time.sleep(2)
pyautogui.keyDown('ctrl')
time.sleep(5)

procurando_imagem = 'sim'

while procurando_imagem == 'sim':
    try:
        img = pyautogui.locateCenterOnScreen('processados.png', confidence=0.7)
        pyautogui.click(img.x,img.y)
        pyautogui.keyDown('ctrl')
        break
        
    except:
        time.sleep(3)
        print("não encontrei")
        pyautogui.click(x=901, y=613)
    
pyautogui.moveTo(x=563, y=530)
time.sleep(2)
pyautogui.mouseDown()
time.sleep(2)

while procurando_imagem == 'sim':
    try:
        img = pyautogui.locateCenterOnScreen('processados.png', confidence=0.7)
        pyautogui.moveTo(img.x,img.y)
        pyautogui.keyDown('ctrl')
        break
        
    except:
        time.sleep(3)
        print("não encontrei")

    
    #pyautogui.click(x=356, y=433)
    #time.sleep(1)
    #pyautogui.keyUp('ctrl')
    #time.sleep(1)
    #pyautogui.moveTo(x=513, y=479)
    #time.sleep(1)
    #pyautogui.mouseDown()
    #time.sleep(1)
    #pyautogui.moveTo(x=877, y=708)
    #time.sleep(1)
    #pyautogui.mouseUp()