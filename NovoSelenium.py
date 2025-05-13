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

time.sleep(80)