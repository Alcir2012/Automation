import time
import pyautogui

time.sleep(5)
pyautogui.hotkey('ctrl','t')
pyautogui.sleep(3)
pyautogui.write('banpara')
pyautogui.press('enter')
pyautogui.sleep(15)
pyautogui.click(x=944, y=229)
pyautogui.sleep(2)
pyautogui.drag(-320,270,duration=3)
pyautogui.sleep(4)
pyautogui.mouseUp()
pyautogui.sleep(3)
pyautogui.hotkey('ctrl','w')
pyautogui.sleep(2)

procurandoImagem = True
tentativasMaximas = 5
tentativas = 0

#Conectar em nova conexão
while procurandoImagem and tentativas<tentativasMaximas:
    try:
        # Tenta encontrar a imagem e clicar nela
        img = pyautogui.locateCenterOnScreen('Reconectar.png', confidence=0.7)
        pyautogui.click(img.x, img.y)
        time.sleep(10)
        
        # Segunda conexão Banpara
        pyautogui.sleep(5)
        pyautogui.click(x=944, y=229)
        pyautogui.sleep(2)
        pyautogui.drag(-320, 270, duration=3)
        pyautogui.sleep(4)
        pyautogui.mouseUp()
        pyautogui.sleep(3)
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.sleep(2)
        
        # Volta a procurar a imagem
        tentativas = 0
        continue
    except:
        # Se a imagem não for encontrada, espera 3 segundos e tenta novamente
        tentativas += 1
        time.sleep(3)
        print("Não encontrei")

    if tentativas>= tentativasMaximas:
        pyautogui.alert("Limite de tentativas excedidas. Parando busca")
        procurandoImagem = False

time.sleep(5)
pyautogui.hotkey('ctrl','t')
time.sleep(5)
pyautogui.write('catalogador')
time.sleep(2)
pyautogui.press('enter')
time.sleep(9)
pyautogui.click(x=729, y=217)
time.sleep(3)
pyautogui.write('banpara')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=455, y=218)
time.sleep(2)
pyautogui.hotkey('ctrl','a')
time.sleep(2)
pyautogui.dragTo(1400, 600, duration=2)
pyautogui.mouseUp()
pyautogui.alert('Finalizado')