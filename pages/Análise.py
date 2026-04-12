import streamlit as st
import pandas as pd
import requests
import logging
from datetime import datetime

# =================================================================
# 0. CONFIGURAÇÃO DE INFRAESTRUTURA
# =================================================================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Auditoria Fidedigna v2", layout="wide")

# =================================================================
# 1. MOTOR DE INGESTÃO RESILIENTE (CONECTOR API)
# =================================================================
@st.cache_data(ttl=600, show_spinner="Sincronizando com a Infraestrutura GitHub...")
def fetch_data_resiliente(query: str):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": 20}
    
    try:
        # Timeout curto para não travar a UI se a rede estiver lenta
        response = requests.get(url, params=params, timeout=10)
        
        # Tratamento de erro específico para Rate Limit (Erro 403)
        if response.status_code == 403:
            return "rate_limit", None
        
        response.raise_for_status()
        items = response.json().get('items', [])
        
        if not items:
            return "empty", pd.DataFrame()

        df = pd.DataFrame([{
            "name": i["full_name"],
            "stars": i["stargazers_count"],
            "forks": i["forks_count"],
            "last_update": i["updated_at"]
        } for i in items])

        # Cálculos de Proxies (ACD)
        df["stars_safe"] = df["stars"].replace(0, 1)
        df["appropriation_rate"] = df["forks"] / df["stars_safe"]
        
        # NORMALIZAÇÃO FIDEDIGNA (Pareamento de Escalas)
        max_stars = df["stars"].max()
        max_approp = df["appropriation_rate"].max() if df["appropriation_rate"].max() > 0 else 1
        
        # A densidade simbólica respeita a magnitude real do projeto líder
        df["symbolic_density"] = df["stars"].apply(lambda x: [x / max_stars])
        
        return "success", df

    except requests.exceptions.RequestException as e:
        logger.error(f"Falha na Ingestão: {e}")
        return "error", None

# =================================================================
# 2. INTERFACE DO OBSERVATÓRIO
# =================================================================
st.title("📊 Observatório de Infraestrutura e Trabalho")
st.caption(f"Sincronização Ativa: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

with st.sidebar:
    st.header("🔍 Agente de Ingestão")
    search_query = st.text_input("Alvo da Auditoria:", "language:python", help="Ex: AI, Agents, framework")
    
    st.divider()
    st.markdown("### 🛠️ Status da Conexão")
    status_placeholder = st.empty()

# Execução do Fluxo
status, df = fetch_data_resiliente(search_query)

if status == "success":
    status_placeholder.success("Conectado à API")
    
    max_val = float(df["appropriation_rate"].max())
    
    # Layout Principal
    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "name": st.column_config.TextColumn("Unidade de Produção"),
                "symbolic_density": st.column_config.BarChartColumn(
                    "Densidade Simbólica", 
                    help="Fidedignidade: Proporção real em relação ao líder.",
                    y_min=0, y_max=1
                ),
                "appropriation_rate": st.column_config.ProgressColumn(
                    "Taxa de Trabalho",
                    help="Forks/Stars (Fidedignidade Estatística).",
                    format="%.3f",
                    min_value=0, max_value=max_val
                ),
                "stars": st.column_config.NumberColumn("Estrelas", format="%d ⭐"),
                "forks": st.column_config.NumberColumn("Forks", format="%d 🍴")
            }
        )

    with col_b:
        st.markdown("### ⚖️ Auditoria de Assimetria")
        st.info("""
        **Nota sobre a Régua Visual:**
        As barras de 'Densidade Simbólica' são ancoradas no líder da busca. 
        Isso expõe a **finitude** dos projetos menores frente à hegemonia do topo.
        """)
        st.metric("Teto de Visibilidade", f"{int(df['stars'].max()):,}")

elif status == "rate_limit":
    st.error("🛑 **Rate Limit Atingido!** O GitHub bloqueou novas requisições temporariamente. Aguarde 60 segundos.")
    status_placeholder.error("Bloqueado pela API")

elif status == "empty":
    st.warning("Nenhuma materialidade encontrada para este termo.")
    status_placeholder.warning("Busca Vazia")

else:
    st.error("🚨 **Erro de Sincronização.** Verifique sua conexão ou a sintaxe da busca.")
    if st.button("Forçar Re-sincronização"):
        st.cache_data.clear()
        st.rerun()

# Rodapé Crítico
st.divider()
st.caption("A tecnologia não é neutra. Este dashboard audita a materialidade do código através de proxies de capital simbólico e trabalho digital.")