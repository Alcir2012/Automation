import streamlit as st
import pandas as pd
from datetime import datetime
import subprocess

st.set_page_config(page_title="Painel de Operadoras sem Arquivo", layout="wide")
st.title("📊 Painel de Operadoras sem Arquivos")
st.markdown(f"**Data de referência:** {datetime.today().strftime('%d/%m/%Y')}")

def get_last_git_commit_date():
    try:
        result = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd"],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )
        return result.strip()
    except Exception as e:
        return "Não foi possível obter a data de atualização."

last_update = get_last_git_commit_date()

st.sidebar.markdown(f"🕒 Última atualização: **{last_update}**")

# Lê o arquivo gerado hoje
try:
    df_hoje = pd.read_excel("operadoras_sem_arquivos_hoje.xlsx")
    operadoras_excluidas = ["008CARDS","AMEX","BANPARA","BANRICARD","BMGCARD","BNB","BOLETOBB","BRASILCARDNET","BRASILCONVENIOS","CABOSESOLDADOS",
                            "CALCARD","CARTAOPREDATADO","CETELEM","CONVENIOSCARD","CREDNOSSO","CROSCARD","CSF","DESCONHECIDO","DIGIMODAS","ELAVON","GLOBAL PAYMENTS",
                            "HELLOTICKET","INOVEPAY","ITI","KOIN","LINXPAY","LAGOACRED","LOSANGO","MAISFACIL","MAXI CARTÃO","OPERADORA TESTE CODIGO","PAGOLIVRE",
                            "PAGSIMPLES","PAGUELOGO","PEDEPRONTO","PITCARD","PIXBB","RAPPI","REDEMED","REDETREL","SESIMAX","SICREDI","SINDPLUS","SOLUCARD",
                            "SOMA CONTA DIGITAL","SOROCRED","TEGYNBTEN","TESTE","TESTE32","TODOCARTOES","UBEREATS","USACARD","VALECON","VALEMAIS","WEBCARD"]
    df = df_hoje[~df_hoje["Operadora"].isin(operadoras_excluidas)]

    if df_hoje.empty:
        st.info("Todas as operadoras enviaram arquivos hoje!")

    else:
        st.markdown(f"🔍 Total de operadoras sem arquivos hoje: **{df.shape[0]}**")
        st.dataframe(df, use_container_width=True)

        # Lê histórico separado
        try:
            df_hist = pd.read_excel("operadoras_historico.xlsx")
            
            df1 = df_hist[~df_hist["Operadora"].isin(operadoras_excluidas)]

            # Conta quantas vezes cada operadora aparece
            contagem = df1["Operadora"].value_counts().reset_index()
            contagem.columns = ["Operadora", "Qtd Dias Sem Arquivo"]

            st.subheader("📌 Operadoras com mais dias sem arquivo (Histórico)")
            st.dataframe(contagem.head(5))

        except FileNotFoundError:
            st.warning("Arquivo de histórico 'operadoras_historico.xlsx' não encontrado.")

except FileNotFoundError:
    st.error("Arquivo 'operadoras_sem_arquivos_hoje.xlsx' não encontrado. Execute o script Selenium primeiro.")
