import pyautogui
import time
import logging
import os

# Faz o Python trabalhar sempre no diretório do script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Configuração do log
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

time.sleep(5)

areadeBusca = (650, 200, 750, 260)
tentativasMaximas = 3
tentativas = 0
procurandoImagem = True

def abreTudo():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('WinScp')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(12)
    pyautogui.write('shellbox')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)

def faztudoShellbox():
    global tentativas
    while procurandoImagem:
        try:
            img = pyautogui.locateCenterOnScreen('csv11.png', confidence=0.7, region=areadeBusca)
            if img:
                logging.info("Imagem CSV localizada, iniciando processo de transferência.")
                pyautogui.click(img.x, img.y)
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(2)
                pyautogui.keyDown('ctrl')
                time.sleep(1)
                pyautogui.click(x=775, y=226)
                time.sleep(1)
                pyautogui.keyUp('ctrl')
                time.sleep(2)
                pyautogui.moveTo(x=700, y=260)
                time.sleep(0.5)
                pyautogui.drag(-320, 220, duration=2)
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(45)
                pyautogui.click(x=700, y=260)
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(0.5)
                pyautogui.keyDown('ctrl')
                pyautogui.click(x=775, y=226)
                time.sleep(0.5)
                pyautogui.keyUp('ctrl')
                time.sleep(0.5)
                pyautogui.moveTo(x=700, y=260)
                time.sleep(0.5)
                pyautogui.drag(0, -30, duration=2)
                pyautogui.mouseUp()
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'w')

                logging.info("Transferência finalizada com sucesso.")
                reconectarSessao()
            else:
                raise Exception("Imagem CSV não encontrada.")
        except Exception as e:
            tentativas += 1
            logging.warning(f"Tentativa {tentativas}: {e}")
            time.sleep(3)
            if tentativas >= tentativasMaximas:
                logging.error("Limite de tentativas excedido. Encerrando busca.")
                time.sleep(2)
                pyautogui.moveTo(x=700, y=220)
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'w')
                reconectarSessao()

def reconectarSessao():
    time.sleep(3)
    imgReconectar = pyautogui.locateCenterOnScreen('reconectaSessao.png', confidence=0.7)
    if imgReconectar:
        logging.info("Imagem de reconexão encontrada. Reestabelecendo sessão.")
        pyautogui.click(imgReconectar.x, imgReconectar.y)
        time.sleep(7)
        faztudoShellbox()
    else:
        logging.error("Imagem de reconexão não encontrada.")
        pyautogui.alert("Imagem de reconexão não encontrada")
        return
        
def conectaCatalogador():
    time.sleep(3)
    imgCatalogador = pyautogui.locateCenterOnScreen('conectaCatalogador.png',confidence=0.5)
    time.sleep(2)
    pyautogui.click(imgCatalogador.x,imgCatalogador.y)
    time.sleep(2)
    pyautogui.write('catalogador')
    time.sleep(2)
    pyautogui.press('enter')

abreTudo()
faztudoShellbox()
conectaCatalogador()