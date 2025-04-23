import streamlit as st
import os
import re
import pandas as pd

# ========== CONFIGURAÇÕES ==========
st.set_page_config(page_title="Logs Shellbox", layout="wide")
st.title("📄 Visualizador de Logs - Shellbox")

# ========== FUNÇÃO DE PARSE ==========
def ler_log_estruturado(caminho_log):
    with open(caminho_log, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    dados = []
    padrao = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+ - INFO - (.+?): (.+)"

    for linha in linhas:
        match = re.match(padrao, linha)
        if match:
            data, tipo, detalhe = match.groups()
            dados.append({'data': data, 'tipo': tipo.strip(), 'arquivo': detalhe.strip()})

    return pd.DataFrame(dados)

# ========== CAMINHO DO LOG ==========
log_path = "shellbox.log"  # Use caminho absoluto se necessário

if os.path.exists(log_path):
    # === VISUALIZAÇÃO BRUTA ===
    with open(log_path, "r", encoding="utf-8") as file:
        logs = file.readlines()

    filtro = st.text_input("🔍 Filtrar por palavra-chave (ex: enviado, erro, baixado, ignorado)")

    if filtro:
        logs_filtrados = [linha for linha in logs if filtro.lower() in linha.lower()]
        st.text_area("📝 Resultado filtrado", "".join(logs_filtrados), height=300)
    else:
        st.text_area("📝 Log completo", "".join(logs), height=300)

    st.markdown("---")

    # === VISUALIZAÇÃO ESTRUTURADA ===
    st.subheader("📊 Dados Estruturados do Log")
    df = ler_log_estruturado(log_path)

    if not df.empty:
        # Exibir DataFrame
        st.dataframe(df)

        # Converter coluna 'data' para datetime
        df['data'] = pd.to_datetime(df['data'])

        # Agrupamento por tipo (Baixado, Enviado, Ignorado)
        contagem_tipo = df['tipo'].value_counts().reset_index()
        contagem_tipo.columns = ['Tipo', 'Quantidade']

        st.bar_chart(contagem_tipo.set_index('Tipo'))

    else:
        st.info("Log presente, mas sem dados estruturados identificados.")
else:
    st.warning("⚠️ Arquivo de log não encontrado.")
