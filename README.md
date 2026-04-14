# 🔍 Anatomia do Capital Digital

### Um Dashboard Crítico sobre Visibilidade no GitHub

---

## 🧠 Sobre o Projeto

Este projeto não busca identificar “os melhores repositórios”.
Ele propõe algo diferente:

> **Analisar como a visibilidade é distribuída dentro do ecossistema de código aberto.**

A partir de dados da API do GitHub, o sistema constrói um painel interativo que permite observar como métricas como *stars* operam como sinais sociais — e não necessariamente como indicadores de qualidade.

---

## ⚖️ Problema

Plataformas digitais frequentemente utilizam métricas quantitativas (ex: estrelas) como proxy de relevância.

No entanto:

* Visibilidade não é distribuída de forma equitativa
* Projetos já populares tendem a acumular ainda mais atenção
* Pequenos projetos permanecem invisíveis

👉 Isso levanta uma questão central:

> **O que realmente está sendo medido — qualidade ou visibilidade acumulada?**

---

## 🎯 Objetivo

Construir um sistema que:

* Colete dados da API do GitHub
* Estruture esses dados em um pipeline analítico
* Apresente visualizações interativas
* Estimule uma leitura crítica sobre métricas de popularidade

---

## 🧱 Arquitetura do Projeto

```bash
github-analytics-dashboard/
│
├── app.py
├── pages/
│   ├── Dashboard.py
│   ├── Analise.py
│   └── Metodologia.py
│
├── utils/
│   └── api.py
│
├── .streamlit/
│   └── secrets.toml
│
├── requirements.txt
└── README.md
```

### 🔄 Fluxo de Dados

```text
GitHub API → Coleta (requests)
           → Cache (Streamlit)
           → Processamento (pandas)
           → Visualização (Plotly)
           → Interface (Streamlit)
```

---

## ⚙️ Tecnologias Utilizadas

* **Python**
* **Streamlit** — interface interativa
* **Pandas** — manipulação de dados
* **Plotly** — visualização
* **Requests** — integração com API
* **Git + GitHub** — versionamento

---

## ⚡ Funcionalidades

* 🔎 Filtro por linguagem de programação
* 📄 Controle de profundidade da coleta (paginação)
* 📊 Ranking de repositórios por visibilidade (stars)
* 📈 Métricas agregadas:

  * Volume total de visibilidade
  * Pico de atenção
  * Número de entidades analisadas
* 🧾 Visualização de dados brutos
* ⚠️ Tratamento de erros da API
* 🔐 Integração com token (segurança + estabilidade)
* ⚡ Cache de dados para performance

---

## 🔐 Segurança

O projeto utiliza variáveis sensíveis via:

```toml
.streamlit/secrets.toml
```

Isso evita exposição de tokens no repositório.

---

## 🚀 Deploy

O projeto está pronto para deploy no Streamlit Cloud.

### Passos:

1. Subir o repositório no GitHub
2. Configurar `secrets.toml` no painel do Streamlit
3. Executar o app

---

## 📊 Insight Principal

Os dados revelam um padrão consistente:

> **A visibilidade é concentrada.**

Poucos repositórios concentram grande parte das estrelas, indicando um efeito de acumulação cumulativa.

Isso sugere que:

* Popularidade gera mais popularidade
* A métrica reforça desigualdades estruturais
* Rankings refletem exposição, não necessariamente mérito técnico

---

## 🧪 Limitações

* Dados limitados pela API do GitHub
* Stars não representam qualidade técnica
* Amostragem parcial (paginação)
* Ausência de análise temporal (ainda)

---

## 🔭 Próximos Passos

* 📈 Análise temporal de crescimento de stars
* 🧠 Modelos de distribuição (desigualdade)
* 📦 Exportação de dados (CSV/Parquet)
* 🌐 API própria para consumo externo

---

## 👤 Autor

**Jhon Max Polins Ribeiro**

---

## 💡 Consideração Final

Este projeto não oferece respostas definitivas.

Ele propõe uma mudança de perspectiva:

> **Visualizar dados não é compreender — é interpretar.**
