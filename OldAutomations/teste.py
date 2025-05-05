from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Configurações básicas
service =Service(executable_path="C:/Users/jose.alcir/Documents/Python/Antigos projetos/ProjetosAutomacao/Selenium/geckodriver.exe")  # IMPORTANTE: ./ no começo indica 'na mesma pasta'

# Inicializar o driver do Firefox
driver = webdriver.Firefox(service=service)

# Exemplo de teste
driver.get('https://www.google.com')
print(driver.title)

time.sleep(5)
driver.quit()
