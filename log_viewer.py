import streamlit as st
import os
import re
import pandas as pd
import altair as alt  # Biblioteca para o gráfico horizontal

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
            dados.append({
                'data': data,
                'tipo': tipo.strip(),
                'arquivo': detalhe.strip()
            })

    return pd.DataFrame(dados)

# ========== CAMINHO DO LOG ==========
log_path = "shellbox.log"

if os.path.exists(log_path):
    # --- PARTE 1: DASHBOARD ESTRUTURADO ---
    st.subheader("📊 Dashboard de Tipos de Evento")
    df = ler_log_estruturado(log_path)

    if not df.empty:
        # Converte a coluna 'data' para datetime (se precisar de futura filtragem por data)
        df['data'] = pd.to_datetime(df['data'])

        # Prepara tabela de contagem por tipo
        contagem = (
            df['tipo']
            .value_counts()
            .rename_axis('Tipo')
            .reset_index(name='Quantidade')
        )
        st.dataframe(contagem)

        # Gráfico de barras horizontal com Altair
        chart = (
            alt.Chart(contagem)
            .mark_bar()
            .encode(
                x=alt.X('Quantidade:Q', title='Quantidade'),
                y=alt.Y('Tipo:N', sort='-x', title='Tipo de Evento')
            )
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Nenhum evento estruturado encontrado no log.")

    st.markdown("---")

    # --- PARTE 2: VISUALIZAÇÃO BRUTA DO LOG ---
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
