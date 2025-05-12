import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Painel de Operadoras sem Arquivo", layout="wide")

# Título
st.title("📊 Painel de Operadoras sem Arquivos")
st.markdown(f"**Data de referência:** {datetime.today().strftime('%d/%m/%Y')}")

# Lendo Excel
try:
    df = pd.read_excel("operadoras_sem_arquivos_hoje.xlsx")

    if df.empty:
        st.info("🎉 Todas as operadoras enviaram arquivos hoje!")
    else:
        # Mostrando total
        st.markdown(f"🔍 Total de operadoras sem arquivos hoje: **{df.shape[0]}**")
        
        # Ordenando por quantidade de dias
        df["Qtd Dias Sem Arquivo"] = df["Dias com 0 arquivos"].apply(lambda x: len(str(x).split(',')))
        df_sorted = df.sort_values(by="Qtd Dias Sem Arquivo", ascending=False)

        st.dataframe(df_sorted[["Operadora", "Dias com 0 arquivos"]], use_container_width=True)

        # Destaques
        st.subheader("📌 Operadoras com mais dias sem arquivo")
        st.write(df_sorted.head(5)[["Operadora", "Dias com 0 arquivos"]])

except FileNotFoundError:
    st.error("Arquivo 'operadoras_sem_arquivos_hoje.xlsx' não encontrado. Execute o script Selenium primeiro.")
