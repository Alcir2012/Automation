import streamlit as st
import os
import re
import pandas as pd
import altair as alt

# ========== CONFIGURAÇÕES ==========
st.set_page_config(page_title="Logs Shellbox", layout="wide")
st.title("📄 Visualizador de Logs - Goodcard")

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
log_path = "goodcard.log"

if os.path.exists(log_path):
    # Leitura estruturada
    df = ler_log_estruturado(log_path)

    if not df.empty:
        # Normaliza tipos de evento
        def normalize_tipo(t):
            t = t.lower()
            if 'baixado' in t:
                return 'Baixado localmente'
            elif 'enviado' in t:
                return 'Enviado para processamento'
            elif 'Ignorado' in t:
                return 'Ignorado não é um arquivo'
            elif 'Erro' in t:
                return 'Erro interno'
            else:
                return t

        df['tipo'] = df['tipo'].apply(normalize_tipo)
        df['data'] = pd.to_datetime(df['data'])

        # ================= KPIs =================
        st.markdown("### 📊 Resumo Geral")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Baixados localmente", df[df['tipo'] == 'Baixado localmente'].shape[0])
        col2.metric("Enviados para processamento", df[df['tipo'] == 'Enviado para processamento'].shape[0])
        #col3.metric("Ignorados", df[df['tipo'] == 'Ignorado não é um arquivo'].shape[0])
        col3.metric("Erros de envio", df[df['tipo'] == 'Erro interno'].shape[0])

        # ========== FILTRO POR DATA ==========
        st.markdown("### 📅 Filtro por Data")
        data_inicio = st.date_input("Data inicial", df['data'].min().date())
        data_fim = st.date_input("Data final", df['data'].max().date())

        df = df[(df['data'].dt.date >= data_inicio) & (df['data'].dt.date <= data_fim)]

        # ========== FILTRO POR NOME DE ARQUIVO ==========
        st.markdown("### 🔍 Buscar por nome de arquivo")
        filtro_arquivo = st.text_input("Digite parte do nome do arquivo:")
        if filtro_arquivo:
            df = df[df['arquivo'].str.contains(filtro_arquivo, case=False)]

        # ========== FILTRO PARA RESUMO (removendo Ignorado e Removido) ==========
        df_filtrado = df[
            (df['tipo'] != 'ignorado') &
            (df['tipo'] != 'Removido localmente'.lower()) &
            (df['tipo'] != 'erro ao mover'.lower())
        ]

        # ========== DETALHAMENTO ==========
        st.subheader("📋 Detalhamento das Ações")
        st.dataframe(df_filtrado[['data', 'tipo', 'arquivo']], use_container_width=True)

        # ========== GRÁFICO DE TIPOS ==========
        contagem = (
            df_filtrado['tipo']
                .value_counts()
                .rename_axis('Tipo')
                .reset_index(name='Quantidade')
        )

        st.subheader("📊 Gráfico Tipos de Eventos")
        chart = (
            alt.Chart(contagem)
               .mark_bar()
               .encode(
                   x=alt.X('Quantidade:Q', title='Quantidade', axis=alt.Axis(format='d')),
                   y=alt.Y('Tipo:N', sort='-x', title='Tipo de Evento'),
                   color='Tipo:N'
               )
        )
        st.altair_chart(chart, use_container_width=True)

       # ========== GRÁFICO DE EVENTOS POR DIA ==========
        st.subheader("📈 Registro dos arquivos em processamento - Dia")

        # 🔹 Primeiro: garantir que estamos só com a data (sem hora)
        df_filtrado['dia'] = df_filtrado['data'].dt.strftime('%Y-%m-%d')  # vira string '2025-04-27'

        # 🔹 Agrupa por dia + tipo
        eventos_por_dia = df_filtrado.groupby(['dia', 'tipo']).size().reset_index(name='quantidade')
    
        # 🔹 Cria gráfico de linha
        chart_dia = alt.Chart(eventos_por_dia).mark_bar(point=True).encode(
            x=alt.X('dia:N', title='Data',
                    sort= 'ascending',
                    axis=alt.Axis(labelAngle=0)),  # ATENÇÃO: dia como Nominal (N) agora, não Temporal (T)
            y=alt.Y('quantidade:Q', title='Quantidade de Eventos'),
            color=alt.Color('tipo:N', title='Tipo de Evento'),
            tooltip=['dia', 'tipo', 'quantidade']
        ).transform_filter(
            alt.FieldEqualPredicate(field='tipo',equal='Enviado para processamento')
        ).properties(
            height=400
        )

        st.altair_chart(chart_dia, use_container_width=True)



        # ========== DOWNLOAD CSV ==========
        st.subheader("📥 Exportar dados")
        st.download_button("Baixar CSV dos eventos filtrados", df_filtrado.to_csv(index=False), file_name="log_filtrado.csv")

    else:
        st.info("Nenhum evento estruturado encontrado no log.")

    st.markdown("---")

    # ========== LOG COMPLETO ==========
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
