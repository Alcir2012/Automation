import streamlit as st
import pandas as pd
import altair as alt

# Carregar dados
df = pd.read_excel("media_arquivos_operadoras.xlsx")

st.set_page_config(page_title="Monitoramento de Operadoras", layout="wide")
st.title("📦 Monitoramento de Arquivos por Operadora")

# =========================
# 🔴 TOPO: Destaque Abaixo da Média
# =========================
st.markdown("## 🚨 Operadoras abaixo da média (HOJE)")

df["Diferença %"] = ((df["Média (sem hoje)"] - df["Hoje"]) / df["Média (sem hoje)"]) * 100
df["Diferença %"] = df["Diferença %"].round(1)

# Filtrar abaixo da média com mais de 7%
abaixo_df = df[(df["Status"] == "ABAIXO") & (df["Diferença %"] >= 9.99) & (df["Média (sem hoje)"] >= 70)]

if abaixo_df.empty:
    st.success("Todas as operadoras estão com envios dentro ou acima da média hoje!")
else:
    for idx, row in abaixo_df.iterrows():
        with st.container():
            st.markdown(f"### ❗ {row['Operadora']}")
            col1, col2, col3 = st.columns(3)
            col1.metric("📈 Média", int(row["Média (sem hoje)"]))
            col2.metric("📤 Hoje", int(row["Hoje"]))
            col3.metric("📉 Diferença", f"{row['Diferença %']}%", delta_color="inverse")
            st.divider()

# =========================
# 📋 MEIO: Tabela geral
# =========================
st.markdown("## 📋 Tabela Geral de Operadoras")

st.dataframe(df.style.applymap(
    lambda val: 'color: red;' if isinstance(val, str) and val == "ABAIXO" else ''
), use_container_width=True)

# =========================
# 🔍 BASE: Seleção Individual
# =========================
st.markdown("## 🔎 Análise Individual de Operadora")

operadora_selecionada = st.selectbox("Selecione uma operadora:", df["Operadora"].unique())
dados_op = df[df["Operadora"] == operadora_selecionada].iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("📛 Operadora", dados_op["Operadora"])
col2.metric("📈 Média", int(dados_op["Média (sem hoje)"]))
col3.metric("📤 Hoje", int(dados_op["Hoje"]))
col4.metric("📉 Diferença", int(dados_op["Diferença"]), delta_color="inverse")

st.markdown(f"#### 🧭 Status: **:red['{dados_op['Status']}']**" if dados_op["Status"] == "ABAIXO" else f"#### 🧭 Status: **:green['{dados_op['Status']}']**")

# Gráfico da operadora selecionada
graf_op = pd.DataFrame({
    "Tipo": ["Média (sem hoje)", "Hoje"],
    "Quantidade": [dados_op["Média (sem hoje)"], dados_op["Hoje"]]
})

chart = alt.Chart(graf_op).mark_bar().encode(
    x="Tipo",
    y="Quantidade",
    color="Tipo",
    tooltip=["Tipo", "Quantidade"]
).properties(
    width=400,
    height=300,
    title=f"Comparativo de envios - {dados_op['Operadora']}"
)

st.altair_chart(chart)

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Alcir 🧠 com Streamlit")
