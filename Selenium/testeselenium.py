from selenium import webdriver
import time

#abrir navegador
navegador = webdriver.Chrome()

#acessar um site
navegador.get('https://www.eextrato.com.br/conciliador/pages/painelControleArquivos/painelControleArquivos.xhtml')
navegador.maximize_window()

#selecionar elemento
login = navegador.find_element("name", "user")

login.click()
login.send_keys("jose.alcir")

time.sleep(0.5)

password = navegador.find_element("id", "password")
password.send_keys("Alcir@2022")

acessar = navegador.find_element("id","entrar")
acessar.click()

time.sleep(10)