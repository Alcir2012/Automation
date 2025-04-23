import streamlit as st
import os
import re
import pandas as pd
import altair as alt

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
log_path = "shellbox.log"

if os.path.exists(log_path):
    # Leitura estruturada
    df = ler_log_estruturado(log_path)

    if not df.empty:
        # Normaliza tipos de evento
        def normalize_tipo(t):
            if 'Baixado' in t:
                return 'Baixado'
            elif 'Enviado' in t:
                return 'Enviado'
            elif 'Ignorado' in t:
                return 'Ignorado'
            elif 'Erro' in t:
                return 'Erro'
            else:
                return t

        df['tipo'] = df['tipo'].apply(normalize_tipo)

        # Exibe detalhamento
        st.subheader("📋 Detalhamento das ações")
        st.dataframe(df[['data', 'tipo', 'arquivo']])

        # Prepara dados para gráfico
        df['data'] = pd.to_datetime(df['data'])
        contagem = (
            df['tipo']
              .value_counts()
              .rename_axis('Tipo')
              .reset_index(name='Quantidade')
        )

        # Gráfico de barras horizontal
        st.subheader("📊 Dashboard Tipos de Evento")
        chart = (
            alt.Chart(contagem)
               .mark_bar()
               .encode(
                   x=alt.X('Quantidade:Q', title='Quantidade',axis=alt.Axis(format='d')),
                   y=alt.Y('Tipo:N', sort='-x', title='Tipo de Evento')
               )
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Nenhum evento estruturado encontrado no log.")

    st.markdown("---")

    # Exibição bruta do log
    st.subheader("📝 Log Completo")
    with open(log_path, "r", encoding="utf-8") as file:
        linhas = file.readlines()

    filtro = st.text_input(
        "🔍 Filtrar por palavra-chave (ex: enviado, erro, baixado, ignorado)",
        value=""
    )

    if filtro:
        lines = [l for l in linhas if filtro.lower() in l.lower()]
        st.text_area("Resultado filtrado", "".join(lines), height=300)
    else:
        st.text_area("Log completo", "".join(linhas), height=300)
else:
    st.warning("⚠️ Arquivo de log não encontrado.")
