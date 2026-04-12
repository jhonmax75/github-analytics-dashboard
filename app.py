import streamlit as st
import pandas as pd
import logging
import requests
from typing import Dict, List

# =================================================================
# 0. LOGGING E CONFIGURAÇÃO
# =================================================================
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Digital Labor Observatory", layout="wide")

# =================================================================
# 1. DESIGN (INTERFACE CRÍTICA)
# =================================================================
def apply_custom_design():
    st.markdown("""
    <style>
        :root { --accent: #58a6ff; --bg-card: #0d1117; --border: #30363d; --text-dim: #8b949e; }
        .critico-card {
            background-color: var(--bg-card);
            border: 1px solid var(--border);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
        }
        .badge-status {
            background-color: #238636; color: white; padding: 2px 10px;
            border-radius: 10px; font-size: 0.65rem; font-weight: 800;
        }
    </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# =================================================================
# 2. MOTOR DE INGESTÃO (API DO GITHUB - CONECTOR DINÂMICO)
# =================================================================
@st.cache_data(ttl=3600) # Mantém os dados frescos por 1 hora
def fetch_live_data(query: str = "language:python", sort: str = "stars") -> pd.DataFrame:
    """Extrai dados em tempo real, quebrando a estaticidade da infraestrutura."""
    logger.info(f"Iniciando Ingestão de Dados: {query}")
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": sort, "order": "desc", "per_page": 50}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            items = response.json().get('items', [])
            data = [{
                'name': i['full_name'],
                'stars': i['stargazers_count'],
                'forks': i['forks_count'],
                'description': i['description'],
                'url': i['html_url']
            } for i in items]
            return pd.DataFrame(data)
        else:
            st.error(f"Erro na API: {response.status_code}")
            return pd.DataFrame()
    except Exception as e:
        logger.error(f"Falha na conexão: {e}")
        return pd.DataFrame()

# =================================================================
# 3. CAMADA ANALÍTICA (ACD)
# =================================================================
def enrich_and_analyze(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica métricas de apropriação e capital simbólico."""
    if df.empty: return df
    df = df.copy()
    df['stars'] = df['stars'].replace(0, 1) # Evita divisão por zero
    # Taxa de Apropriação: Forks (Trabalho) / Stars (Capital Simbólico)
    df['appropriation_rate'] = df['forks'] / df['stars']
    return df

# =================================================================
# 4. SIDEBAR E CONTROLE DE FLUXO
# =================================================================
with st.sidebar:
    st.header("⚙️ Agente de Busca")
    tech_query = st.text_input("Termo de Busca (ex: AI, Agent, LLM)", "language:python")
    sort_mode = st.selectbox("Ordenar por", ["stars", "forks", "updated"])
    
    st.divider()
    st.markdown("### 🧠 Perspectiva Analítica")
    mode = st.selectbox("Modo de Interpretação", ["Capital Digital", "Trabalho Colaborativo"])
    
    st.caption("Conexão ativa com a infraestrutura do GitHub via API v3.")

# =================================================================
# 5. EXECUÇÃO E INTERFACE
# =================================================================
st.title("📊 Observatório do Trabalho Digital")
st.caption("Análise em tempo real de infraestruturas de código e hegemonias algorítmicas.")

# Aciona a Ingestão (Baseado na imagem: Ingestion -> Vector DB)
raw_df = fetch_live_data(query=tech_query, sort=sort_mode)
df = enrich_and_analyze(raw_df)

if not df.empty:
    labels = {
        "Capital Digital": {"m": "Taxa de Apropriação", "s": "Capital Simbólico", "f": "Trabalho Acumulado"},
        "Trabalho Colaborativo": {"m": "Intensidade de Uso", "s": "Visibilidade", "f": "Contribuições"}
    }.get(mode)

    col1, col2 = st.columns([2, 1])

    with col1:
        top_repo = df.iloc[0]
        st.markdown(f"""
        <div class="critico-card">
            <span class="badge-status">Hegemonia Detectada</span>
            <h2 style="color:white; margin:10px 0;">{top_repo['name']}</h2>
            <p style="color:var(--text-dim);">{top_repo['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.metric(labels["m"], f"{df['appropriation_rate'].mean():.2%}", delta="Live Data")
        with st.container(border=True):
            st.caption("**Nota do Agente:** Projetos com alta taxa de forks em relação a estrelas indicam infraestruturas que exigem mais trabalho derivado.")

    st.divider()
    st.subheader("🛠️ Auditoria das Unidades de Produção")
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "name": "Projeto",
            "stars": st.column_config.NumberColumn(labels["s"]),
            "forks": st.column_config.NumberColumn(labels["f"]),
            "appropriation_rate": st.column_config.ProgressColumn(labels["m"], format="%.3f", min_value=0, max_value=float(df['appropriation_rate'].max())),
            "url": st.column_config.LinkColumn("Link")
        }
    )
else:
    st.warning("Aguardando entrada do Agente de Busca...")

# Reflexividade (Conforme o seu interesse em ACD)
st.divider()
st.markdown("### 🧩 Reflexividade do Observatório")
st.caption("Este sistema não é neutro. Ele mapeia a economia política do software aberto, onde estrelas são capital simbólico e forks são vetores de trabalho digital.")