'''import pyautogui

Posicao = pyautogui.position()
pyautogui.sleep(4)
print(Posicao)

pyautogui.alert('Finalizado')

pyautogui.sleep(3)

pyautogui.click(Posicao)
'''

import pyautogui
import time


print("Mova o mouse sobre o local desejado. Pressione Ctrl + C para sair.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição do mouse: X={x}, Y={y}", end="\r")  # Atualiza na mesma linha
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nFinalizado.")
