import streamlit as st
import os
 
st.set_page_config(page_title="Logs Shellbox", layout="wide")
st.title("📄 Visualizador de Logs - Shellbox")
 
log_path = "shellbox.log"  # Ou coloque o caminho completo, se estiver em outra pasta
 
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as file:
        logs = file.readlines()
 
    filtro = st.text_input("🔍 Filtrar por palavra-chave (ex: erro, baixado, ignorado)")
 
    if filtro:
        logs_filtrados = [linha for linha in logs if filtro.lower() in linha.lower()]
        st.text_area("📝 Resultado filtrado", "".join(logs_filtrados), height=600)
    else:
        st.text_area("📝 Log completo", "".join(logs), height=600)
else:
    st.warning("⚠️ Arquivo de log não encontrado.")