import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from utils.api import get_repos

# =================================================================
# 1. CONFIGURAÇÃO
# =================================================================
st.set_page_config(page_title="Espelho Crítico: GitHub", layout="wide")

st.markdown("""
<style>
.critical-box { 
    padding: 20px; 
    border-radius: 8px; 
    border-left: 6px solid #e74c3c; 
    background-color: #1b1f23;
    color: #c9d1d9;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. SIDEBAR
# =================================================================
with st.sidebar:
    st.header("⚙️ Aparelho de Captura")
    st.write("Escolha a lente através da qual você deseja observar o recorte técnico.")

    language = st.selectbox(
        "Território Linguístico",
        ["python", "javascript", "go", "java", "c++", "typescript"]
    )

    pages = st.slider("Profundidade da Escavação (Páginas)", 1, 10, 2)

    st.divider()
    st.caption(
        "⚠️ A ampliação da coleta aumenta a amostra, "
        "mas não elimina vieses da plataforma."
    )

# =================================================================
# 3. MANIFESTO
# =================================================================
st.title("🔍 Anatomia do Capital Digital: Análise de Repositórios")

st.markdown("""
<div class="critical-box">
<strong>MANIFESTO:</strong><br>
Este sistema não mede diretamente valor ou trabalho. Ele reorganiza métricas de visibilidade 
em categorias interpretativas.

'Stars' são tratadas como sinais de atenção e 'forks' como indicadores de reuso potencial. 
O silêncio do dado também é parte da análise.
</div>
""", unsafe_allow_html=True)

# =================================================================
# 4. DADOS
# =================================================================
@st.cache_data
def get_critical_data(lang, pgs):
    raw_data = get_repos(lang, pgs)

    if raw_data is None or (isinstance(raw_data, pd.DataFrame) and raw_data.empty):
        return pd.DataFrame()

    df = pd.DataFrame(raw_data).copy()
    df.columns = df.columns.str.lower()

    # --- TRATAMENTO ROBUSTO ---
    for col in ["stars", "forks"]:
        if col not in df.columns:
            df[col] = 1  # valor técnico mínimo

        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(1)

    # ⚠️ Ajuste crítico: estabilização técnica (não neutra)
    df["stars"] = df["stars"].clip(lower=1)

    # Proxy analítico
    df["appropriation_rate"] = (df["forks"] / df["stars"]) * 100

    return df

df = get_critical_data(language, pages)

if df.empty:
    st.warning("⚠️ O silêncio dos dados: a API não retornou informações.")
    st.stop()

# =================================================================
# 5. MÉTRICAS
# =================================================================
st.subheader("I. Indicadores de Visibilidade (Proxy)")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Entidades Capturadas",
    len(df),
    help="Resultados retornados pela API — não representam o universo total."
)

c2.metric(
    "Volume de Atenção (Stars)",
    f"{int(df['stars'].sum()):,}",
    help="Soma de sinais de visibilidade, não valor absoluto."
)

c3.metric(
    "Reuso Potencial (Forks)",
    f"{int(df['forks'].sum()):,}",
    help="Forks indicam possibilidade de derivação, não trabalho efetivo."
)

st.divider()

# =================================================================
# 6. VISUALIZAÇÃO
# =================================================================
st.subheader("II. Distribuição de Visibilidade")

top10 = df.sort_values("stars", ascending=False).head(10)

fig = px.bar(
    top10.sort_values("stars"),
    x="stars",
    y="name",
    orientation="h",
    color="appropriation_rate",
    title="Top 10 (Recorte de Visibilidade e Reuso)",
    labels={
        "stars": "Visibilidade (Stars)",
        "appropriation_rate": "% Reuso (Proxy)"
    },
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig, use_container_width=True)

# =================================================================
# 7. AUDITORIA
# =================================================================
with st.expander("🔍 Auditoria da Materialidade"):
    st.markdown("""
    Exposição da base técnica dos dados coletados.

    ⚠️ Observação: valores ausentes foram substituídos por valores mínimos 
    para garantir estabilidade computacional.
    """)

    st.dataframe(
        df[["name", "stars", "forks", "description"]],
        use_container_width=True
    )

# =================================================================
# 8. NOTA FINAL
# =================================================================
st.caption(
    "Este sistema transforma métricas técnicas em categorias interpretativas. "
    "A visualização não revela a realidade — ela constrói uma leitura possível."
)