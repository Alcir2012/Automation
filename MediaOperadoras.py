from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pandas as pd

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

time.sleep(70)

# Cabeçalhos com datas
header_data = navegador.find_element(By.XPATH, "//tbody[@id='formulario:tblHeader_data']/tr")
colunas_header = header_data.find_elements(By.TAG_NAME, "td")
datas = [col.text.strip() for col in colunas_header if "Operadora" not in col.text]

# Converte datas para datetime
datas_formatadas = [datetime.strptime(d, "%d/%m/%y").date() for d in datas]
hoje = datetime.today().date()

# Identifica a posição do dia atual
idx_hoje = [i for i, d in enumerate(datas_formatadas) if d == hoje]

# Coleta os dados de todas as operadoras
linhas = navegador.find_elements(By.XPATH, "//tbody[@id='formulario:tblData_data']/tr")
registros = []

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    if not colunas:
        continue

    nome_operadora = colunas[0].text.strip()
    valores = [col.text.strip() for col in colunas[1:]]

    for i, valor in enumerate(valores):
        try:
            qtd = int(valor.replace(".", "").replace(",", "")) if valor else 0
        except:
            qtd = 0

        if i < len(datas_formatadas):
            registros.append({
                "Operadora": nome_operadora,
                "Data": datas_formatadas[i],
                "Quantidade": qtd
            })

# Converte para DataFrame
df = pd.DataFrame(registros)

# Calcula média histórica (sem hoje) e compara
resultados = []

for operadora in df["Operadora"].unique():
    df_op = df[df["Operadora"] == operadora]
    df_passado = df_op[df_op["Data"] < hoje]
    df_hoje = df_op[df_op["Data"] == hoje]

    if not df_passado.empty and not df_hoje.empty:
        media = df_passado["Quantidade"].mean()
        qtd_hoje = df_hoje["Quantidade"].values[0]
        desvio = qtd_hoje - media
        status = "ABAIXO" if qtd_hoje < media else "ACIMA" if qtd_hoje > media else "IGUAL"

        resultados.append({
            "Operadora": operadora,
            "Média (sem hoje)": round(media, 2),
            "Hoje": qtd_hoje,
            "Diferença": round(desvio, 2),
            "Status": status
        })

# Exporta para Excel
df_resultado = pd.DataFrame(resultados)
df_resultado["Média (sem hoje)"] = df_resultado["Média (sem hoje)"].astype(int)
df_resultado["Diferença"] = df_resultado["Diferença"].astype(int)
df_resultado.to_excel("C:/Users/jose.alcir/Documents/Python/Antigos projetos/ProjetosAutomacao/media_arquivos_operadoras.xlsx", index=False)

print("Arquivo gerado com sucesso com comparativo de média!")
