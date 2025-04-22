import pyautogui
import time

areadeBusca= (650, 200, 750, 260)
procurandoImagem= True
while procurandoImagem == True:
    try:
        img = pyautogui.locateCenterOnScreen('csv11.png', confidence=0.7, region= areadeBusca)
        if img:
                pyautogui.click(img.x,img.y)
                time.sleep(2)
    except:
         pyautogui.alert('Não encontrei')
         time.sleep(2)
    