import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api import get_repos
st.set_page_config(page_title="Espelho Crítico: GitHub", layout="wide")
st.markdown("""
<style>
    :root {
        --bg-sidebar: #0d1117;
        --accent: #1abc9c;
    }
    .manifesto-card {
        background-color: #f8f9fa;
        border-left: 6px solid var(--accent);
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 25px;
        color: #2c3e50;
    }
    .stDataFrame { border: 1px solid #e6e9ef; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)
st.title("🔍 Anatomia do Capital Digital")
st.markdown("""
<div class="manifesto-card">
<strong>Manifesto:</strong> Este sistema não mede valor intrínseco do código. 
Ele reorganiza sinais de visibilidade em narrativas interpretativas.
Pergunta central: o que é considerado relevante — e o que permanece invisível?
</div>
""", unsafe_allow_html=True)
with st.sidebar:
    st.header("🔍 Territórios Técnicos")
    
    language = st.selectbox(
        "Linguagem (Recorte Analítico)",
        ["python", "javascript", "go", "java", "c++", "typescript"],
        help="⚠️ A escolha da linguagem altera o recorte, não o sistema em si."
    )
    
    pages = st.slider(
        "Profundidade da Coleta",
        1, 10, 2,
        help="Mais páginas ampliam a amostra, mas não eliminam vieses da API."
    )
    
    st.divider()
    st.caption("⚡ Interface construída sob lente crítica (ACD)")
df_raw = get_repos(language, pages)
if isinstance(df_raw, dict) and df_raw.get("error"):
    st.error(f"Erro na API: {df_raw['status_code']}")
    st.json(df_raw["message"])
    st.stop()
if not df_raw:
    st.warning("⚠️ O silêncio dos dados: a API não retornou informações.")
    st.stop()
df_raw = pd.DataFrame(df_raw)
if df_raw.empty:
    st.warning("⚠️ O silêncio dos dados: a API não retornou informações.")
    st.stop()
df = df_raw.copy()
if "description" in df.columns:
    df["description"] = df["description"].fillna("Ausência de narrativa")
else:
    df["description"] = "Ausência de narrativa"
if "stars" in df.columns:
    df["stars"] = pd.to_numeric(df["stars"], errors="coerce").fillna(0)
else:
    df["stars"] = 0
df["visibility"] = df["stars"]
st.subheader("1. Dinâmica de Visibilidade (Proxy)")
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(
        "Entidades Observadas",
        f"{len(df)} repos",
        help="Unidades retornadas pela API (não universo total)."
    )
with m2:
    st.metric(
        "Volume de Visibilidade",
        f"{int(df['stars'].sum()):,}",
        delta="Soma de atenção acumulada",
        help="Stars são sinais sociais, não valor absoluto."
    )
with m3:
    st.metric(
        "Pico de Atenção",
        f"{int(df['stars'].max()):,}",
        delta="Concentração máxima",
        help="Indica assimetria, não qualidade."
    )
st.divider()
col_graph, col_text = st.columns([1.5, 1])
with col_graph:
    top10 = df.sort_values("stars", ascending=False).head(10)
    
    fig = px.bar(
        top10.sort_values("stars"),
        x="stars",
        y="name",
        orientation="h",
        color="stars",
        color_continuous_scale="Tealgrn",
        template="plotly_white",
        title=f"Top 10 (Recorte de Visibilidade) — {language.title()}"
    )
    
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
with col_text:
    st.markdown("### ⚖️ Efeito de Acumulação")
    st.write("""
    As estrelas operam como um mecanismo de **acumulação cumulativa**: 
    projetos já visíveis tendem a concentrar ainda mais atenção.
    ⚠️ Este gráfico não representa “os melhores projetos”, 
    mas apenas os mais visíveis dentro deste recorte.
    """)
    
    st.info(
        "Você está observando o topo da distribuição. "
        "Aumentar as páginas amplia o campo, mas não elimina a desigualdade estrutural."
    )
st.subheader("3. Auditoria da Materialidade")
with st.expander("🛠️ Ver Dados Brutos (Interpretação Mínima)", expanded=False):
    st.dataframe(
        df[["name", "stars", "description"]],
        use_container_width=True,
        column_config={
            "name": "Identidade",
            "stars": st.column_config.NumberColumn("Stars (Visibilidade)", format="%d"),
            "description": st.column_config.TextColumn("Narrativa", width="large")
        }
    )
st.caption(
    "Dados de plataformas refletem dinâmicas sociais mediadas por algoritmos. "
    "Visualizar não é compreender — é interpretar."
)