from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
from datetime import datetime
from dotenv import load_dotenv
import os
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

time.sleep(7)

#Pesquisar
pesquisar = navegador.find_element(By.CLASS_NAME,"btn-padrao")
pesquisar.click()

time.sleep(20)

#pegando operadoras zeradas

header_data = navegador.find_element(By.XPATH, "//tbody[@id='formulario:tblHeader_data']/tr")
colunas_header = header_data.find_elements(By.TAG_NAME,"td")
datas = [col.text.strip() for col in colunas_header if "Operadora" not in col.text]

datas_formatadas = [datetime.strptime(d, "%d/%m/%y") for d in datas]

hoje = datetime.today()

data_hoje = [i for i, data in enumerate(datas_formatadas) if data.date() == hoje.date()]

linhas = navegador.find_elements(By.XPATH, "//tbody[@id='formulario:tblData_data']/tr")
operadoras_sem_arquivos = []

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    
    if not colunas:
        continue

    nome_operadora = colunas[0].text.strip()
    dados = [col.text.strip() for col in colunas[1:]]

    dias_sem_arquivo = [datas[i] for i in data_hoje if i < len(dados) and dados[i] in ("", "0")]

    if dias_sem_arquivo:
        operadoras_sem_arquivos.append([nome_operadora, ", ".join(dias_sem_arquivo)])


    # Verifica se todos os dados seguintes estão vazios ou zero
    '''if any(dado in ("", "0") for dado in dados):
        operadoras_sem_arquivos.append(nome_operadora)'''

#print("Operadoras sem arquivos:", operadoras_sem_arquivos)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Operadoras sem arquivos"

# Cabeçalho
ws.append(["Operadora", "Dias com 0 arquivos"])

# Dados
for operadora, dias in operadoras_sem_arquivos:
    ws.append([operadora, dias])

# Salva arquivo
wb.save("C:/Users/jose.alcir/Documents/Python/Antigos projetos/ProjetosAutomacao/operadoras_sem_arquivos_hoje.xlsx")

print("Arquivo gerado com sucesso!")

# Lê ou cria histórico
arquivo_hist = "C:/Users/jose.alcir/Documents/Python/Antigos projetos/ProjetosAutomacao/operadoras_historico.xlsx"
if os.path.exists(arquivo_hist):
    df_hist = pd.read_excel(arquivo_hist)
else:
    df_hist = pd.DataFrame(columns=["Operadora", "Data"])

# Garante que a data seja string formatada
data_hoje_str = hoje.strftime('%d/%m/%Y')

# Lista com novas linhas (evitando duplicatas)
novas_linhas = []

for operadora, _ in operadoras_sem_arquivos:
    if not ((df_hist["Operadora"] == operadora) & (df_hist["Data"] == data_hoje_str)).any():
        novas_linhas.append({"Operadora": operadora, "Data": data_hoje_str})

# Se tiver novas, salva
if novas_linhas:
    df_novo = pd.DataFrame(novas_linhas)
    df_hist = pd.concat([df_hist, df_novo], ignore_index=True)
    df_hist.to_excel(arquivo_hist, index=False)
    print("Histórico atualizado.")
else:
    print("Nenhuma nova entrada para o histórico.")

'''#Enviando e-mail

msg = MIMEMultipart()
msg['Subject'] = 'Aviso: Operadoras sem arquivos'
msg['From'] = email_usuario
msg['To'] = 'monitoramento@eextrato.com.br'

corpo_html = "<h3>Operadoras sem arquivos hoje:</h3><ul>"
for operadora, dias in operadoras_sem_arquivos:
    corpo_html += f"<li><b>{operadora}</b>: {dias}</li>"
corpo_html += "</ul>"

msg.attach(MIMEText(corpo_html, 'html'))

# Anexo
with open("operadoras_sem_arquivos_hoje.xlsx", "rb") as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="operadoras_sem_arquivos_hoje.xlsx"')
    msg.attach(part)

with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.starttls()
    smtp.login(email_usuario, senha_email)
    smtp.send_message(msg)

print("E-mail enviado com sucesso!")'''

time.sleep(100)