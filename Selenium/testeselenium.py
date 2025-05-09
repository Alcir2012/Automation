from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#abrir navegador
navegador = webdriver.Chrome()

#acessar um site
navegador.get('https://www.eextrato.com.br/conciliador/pages/painelControleArquivos/painelControleArquivos.xhtml')
navegador.maximize_window()

#Realizando login
login = navegador.find_element("name", "user")

login.click()
login.send_keys("jose.alcir")

time.sleep(0.5)

password = navegador.find_element("id", "password")
password.send_keys("Alcir@2022")

acessar = navegador.find_element("id","entrar")
acessar.click()

#Painel Controle de arquivos
navegador.get('https://www.eextrato.com.br/conciliador/pages/painelControleArquivos/painelControleArquivos.xhtml#')

#Grupo empresa
g_empresa = navegador.find_element("id", "formulario:grupoEmpresa_label")
g_empresa.click()
time.sleep(2)
g_empresa = navegador.find_element("id", "formulario:grupoEmpresa_filter")
g_empresa.send_keys("Todos")
time.sleep(1)
g_empresa.send_keys(Keys.ENTER)

time.sleep(5)

#Empresa
empresa = navegador.find_element("id","formulario:comboEmpresa_label")
empresa.click()
time.sleep(5)
empresa = navegador.find_element("id","formulario:comboEmpresa_filter")
empresa.send_keys("Selecione")
time.sleep(2)
empresa.send_keys(Keys.ENTER)

time.sleep(5)

#Pesquisar
pesquisar = navegador.find_element("id","formulario:j_idt1792")
pesquisar.click()

#pegando operadoras zeradas

time.sleep(20)

linhas = navegador.find_elements(By.XPATH, "//tbody[@id='formulario:tblData_data']/tr")
operadoras_sem_arquivos = []

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    
    if not colunas:
        continue

    nome_operadora = colunas[0].text.strip()
    dados = [col.text.strip() for col in colunas[1:]]

    # Verifica se todos os dados seguintes estão vazios ou zero
    if all(dado in ("", "0") for dado in dados):
        operadoras_sem_arquivos.append(nome_operadora)

print("Operadoras sem arquivos:", operadoras_sem_arquivos)

time.sleep(100) 