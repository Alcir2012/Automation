from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from openpyxl import load_workbook


load_dotenv()
email_usuario = os.getenv("EMAIL_USUARIO")
senha_email = os.getenv("EMAIL_SENHA")

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

time.sleep(5)

#Indo até o MAO
navegador.get('https://www.eextrato.com.br/conciliador/pages/monitoramentoArquivoOperadora/monitoramentoArquivoOperadora.xhtml')

time.sleep(5)

#selecionando todas empresas
wait = WebDriverWait(navegador,10)
empresa = navegador.find_element(By.ID,"formulario:j_idt1759:j_idt1769")
time.sleep(1)
empresa.click()
time.sleep(2)
empresa = navegador.find_element(By.ID,"formulario:j_idt1759:j_idt1769_filter")
empresa.click()
time.sleep(3)
empresa.send_keys("SELECIONE")
time.sleep(1)
empresa.send_keys(Keys.ENTER)
time.sleep(5)

#Filtrando data
data_hoje = datetime.today().strftime('%d/%m/%Y')
campo_data = navegador.find_element(By.ID, "formulario:j_idt1759:dataVendaIInputDate")
time.sleep(2)
campo_data.click()
time.sleep(0.5)
campo_data.clear()
time.sleep(0.5)
campo_data.send_keys(data_hoje)
time.sleep(0.5)
campo_data = navegador.find_element(By.ID,"formulario:j_idt1759:dataVendaFInputDate")
time.sleep(2)
campo_data.click()
time.sleep(0.5)
campo_data.clear()
time.sleep(0.5)
campo_data.send_keys(data_hoje)
time.sleep(2)
pesquisar1 = navegador.find_element(By.ID,"formulario:j_idt1838")
pesquisar1.click()

time.sleep(20)

# Localiza a tabela pelo ID
tabela = navegador.find_element(By.ID, "formulario:tblData")

# Encontra todos os <tbody> da tabela
todos_tbody = tabela.find_elements(By.TAG_NAME, "tbody")

# Lista para armazenar os dados
dados_tabela = []

# Percorre cada <tbody>

#gerando excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "dados MAO"

# Define o cabeçalho
ws.append([
    "ignorar", "ignorar", "data", "catalogador", "proc1", "proc2",
    "ativo", "empresa", "operadora", "nome original", "novo nome",
    "tamanho em kb", "checksum"
])
total_linhas = 0

for tbody in todos_tbody:
    linhas = tbody.find_elements(By.TAG_NAME, "tr")
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        dados_linha = []

        for coluna in colunas:
            try:
                img = coluna.find_element(By.TAG_NAME, "img")
                dados_linha.append(img.get_attribute("title").strip())
            except:
                dados_linha.append(coluna.text.strip())

        if any(dados_linha):  # Apenas se tiver conteúdo
            # Garante que tenha 13 colunas
            while len(dados_linha) < 13:
                dados_linha.append("")
            ws.append(dados_linha[:13])  # Limita a 13 no máximo
            total_linhas += 1

# Exibe todos os dados coletados
'''for linha in dados_tabela:
    print(linha)'''

#salvar arquivo
wb.save("dados_MAO.xlsx")

time.sleep(80)