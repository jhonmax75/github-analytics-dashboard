# 🔍 Anatomia do Capital Digital

### Um dashboard crítico sobre visibilidade, popularidade e distribuição de atenção no GitHub

## 🧠 Sobre o projeto

O **Anatomia do Capital Digital — GitHub Analytics Dashboard** é um projeto de análise exploratória de dados que investiga como a visibilidade se distribui entre repositórios de código aberto.

Em vez de classificar projetos como os melhores ou piores, a proposta é examinar criticamente as métricas utilizadas para representar sua popularidade, com destaque para as *stars* do GitHub.

Essas métricas funcionam como sinais de reconhecimento e atenção dentro da plataforma, mas não constituem, isoladamente, medidas de qualidade técnica, relevância científica ou impacto social.

A partir de dados obtidos pela API do GitHub, o projeto organiza informações e as apresenta em um dashboard interativo, permitindo explorar padrões de distribuição, concentração e desigualdade de visibilidade.

**Questão central:**

> O que as métricas de popularidade revelam sobre os projetos — e o que deixam de mostrar?

---

## ⚖️ Problema de pesquisa

Em plataformas digitais, métricas quantitativas são frequentemente utilizadas como indicadores de relevância. No GitHub, o número de *stars* pode influenciar a percepção de popularidade e servir como referência para a descoberta de projetos.

Entretanto, a quantidade de estrelas não deve ser confundida com mérito técnico.

Entre as questões que orientam esta investigação estão:

- **Concentração da atenção:** poucos repositórios podem acumular uma parcela expressiva das estrelas.
- **Acumulação de visibilidade:** projetos já conhecidos podem receber mais atenção por sua exposição anterior.
- **Assimetria de reconhecimento:** iniciativas menores podem permanecer menos visíveis, independentemente de suas características técnicas.
- **Limites das métricas:** indicadores quantitativos não representam, por si só, a complexidade, a qualidade ou a utilidade de um projeto.

Essas questões orientam uma análise exploratória, não uma conclusão antecipada sobre todos os repositórios ou sobre o funcionamento integral do ecossistema open source.

## 🎯 Objetivos

### Objetivo geral

Desenvolver um dashboard interativo para explorar a distribuição da visibilidade entre repositórios do GitHub e discutir criticamente os limites das métricas de popularidade.

### Objetivos específicos

- Coletar informações por meio da API do GitHub.
- Organizar e processar os dados em um fluxo analítico.
- Permitir a exploração dos repositórios por linguagem de programação.
- Comparar indicadores de popularidade e distribuição de estrelas.
- Apresentar métricas agregadas e visualizações interativas.
- Tornar os dados observados acessíveis para inspeção.
- Explicitar as limitações metodológicas e os limites de interpretação dos resultados.

---

## 🧱 Estrutura do projeto

A estrutura abaixo representa a organização lógica documentada para o projeto. Os arquivos efetivamente disponíveis no repositório devem ser consultados para confirmar a correspondência entre essa representação e a implementação atual.

```text
github-analytics-dashboard/
├── app.py
├── pages/
│   ├── Dashboard.py
│   ├── Analise.py
│   └── Metodologia.py
├── utils/
│   └── api.py
├── assets/
├── requirements.txt
├── .gitignore
└── README.md
```

### 🔄 Fluxo analítico

```text
API do GitHub
     │
     ▼
Coleta de dados
   (Requests)
     │
     ▼
Cache e controle de consultas
   (Streamlit)
     │
     ▼
Processamento e organização
   (Pandas)
     │
     ▼
Visualização interativa
   (Plotly)
     │
     ▼
Dashboard
   (Streamlit)
```

O fluxo representa a arquitetura conceitual da aplicação. Os componentes e suas responsabilidades devem ser confirmados na implementação correspondente.

---

## ⚙️ Tecnologias

| Tecnologia | Finalidade |
|---|---|
| **Python** | Linguagem principal da aplicação |
| **Streamlit** | Construção da interface interativa |
| **Pandas** | Organização e processamento dos dados |
| **Plotly** | Criação de visualizações interativas |
| **Requests** | Comunicação com a API do GitHub |
| **Git e GitHub** | Versionamento e hospedagem do código |

---

## ⚡ Funcionalidades documentadas

O projeto foi concebido para oferecer recursos de exploração e análise, incluindo:

- 🔎 **Filtro por linguagem:** restringir a exploração a linguagens de programação específicas.
- 📄 **Paginação da coleta:** controlar a quantidade de resultados consultados.
- 📊 **Ranking por estrelas:** comparar repositórios segundo essa métrica de popularidade.
- 📈 **Indicadores agregados:** observar o volume de estrelas e a quantidade de repositórios analisados.
- 🧾 **Inspeção dos dados:** facilitar a consulta dos registros obtidos.
- ⚠️ **Tratamento de erros:** lidar com falhas e restrições de acesso à API.
- 🔐 **Configuração de credenciais:** permitir o uso de tokens sem incorporá-los diretamente ao código-fonte.
- ⚡ **Cache:** reduzir consultas repetidas e melhorar a eficiência da aplicação.

A disponibilidade e o funcionamento de cada recurso dependem da versão efetivamente mantida no repositório.

---

## 🔐 Segurança e configuração

O acesso à API pode utilizar um token do GitHub, conforme a configuração adotada pela aplicação.

Em ambientes Streamlit, credenciais podem ser configuradas por meio de `st.secrets`, utilizando o arquivo local `.streamlit/secrets.toml` durante o desenvolvimento e o gerenciador de segredos da plataforma no deploy.

Exemplo de configuração local:

```toml
# .streamlit/secrets.toml
GITHUB_TOKEN = "seu_token_aqui"
```

**Cuidados importantes:**

- Não inserir tokens reais no código-fonte ou no README.
- Manter arquivos com credenciais fora do controle de versão.
- Incluir os arquivos de segredos no `.gitignore`.
- Revogar e substituir imediatamente qualquer token que tenha sido exposto.
- Conceder somente as permissões necessárias para as consultas realizadas.

O exemplo acima é ilustrativo. O nome da variável e a forma de leitura precisam corresponder ao código da aplicação.

---

## 🚀 Execução e implantação

Para executar o projeto localmente, é necessário ter Python e acesso às dependências declaradas no repositório.

### Execução local

```bash
git clone https://github.com/jhonmax75/github-analytics-dashboard.git
cd github-analytics-dashboard

python -m venv .venv
```

Ative o ambiente virtual conforme seu sistema operacional e instale as dependências:

```bash
pip install -r requirements.txt
```

Se a aplicação utilizar credenciais, configure-as localmente antes da execução.

Para uma aplicação Streamlit cujo ponto de entrada seja `app.py`:

```bash
streamlit run app.py
```

### Deploy no Streamlit Community Cloud

A implantação depende da compatibilidade da aplicação com o ambiente de execução, das dependências instaladas e da configuração correta dos segredos.

Antes de publicar, recomenda-se:

1. Confirmar que a aplicação inicia sem erros.
2. Verificar se `requirements.txt` contém as dependências necessárias.
3. Configurar os segredos diretamente na plataforma.
4. Testar as consultas à API e o comportamento diante de limites ou falhas.
5. Validar a interface e as principais funcionalidades após a implantação.

A disponibilidade para deploy deve ser considerada confirmada somente após a execução bem-sucedida dos testes correspondentes.

---

## 📊 Interpretação dos resultados

Uma das hipóteses investigáveis pelo projeto é que a distribuição de estrelas entre os repositórios analisados seja desigual, com uma parcela dos projetos concentrando uma proporção elevada da atenção observada.

Essa hipótese pode ser explorada por meio de rankings, distribuições, proporções acumuladas e outras medidas estatísticas adequadas.

Entretanto, a concentração de estrelas não deve ser apresentada como resultado universal sem que a amostra, o período de coleta e os procedimentos analíticos sejam explicitados.

Da mesma forma, uma associação entre popularidade e maior visibilidade não demonstra, por si só, uma relação causal.

### O que as estrelas podem indicar?

- Reconhecimento recebido dentro da plataforma.
- Popularidade relativa entre os projetos observados.
- Padrões de concentração de atenção na amostra analisada.

### O que elas não demonstram isoladamente?

- Qualidade ou segurança do código.
- Maturidade da arquitetura.
- Manutenção ativa ou sustentabilidade do projeto.
- Impacto social ou científico.
- Mérito técnico proporcional ao número de estrelas.

**Princípio de interpretação:** métricas são evidências que precisam de contexto, não substitutos para uma avaliação crítica.

---

## 🧪 Limitações metodológicas

Os resultados de uma análise desse tipo dependem da qualidade da coleta e das decisões metodológicas adotadas.

As principais limitações a considerar são:

- **Limites da API:** restrições de acesso, paginação e cotas podem afetar a abrangência da coleta.
- **Representatividade:** os resultados dependem dos critérios de busca e seleção dos repositórios.
- **Viés de seleção:** uma amostra obtida por consultas específicas não representa necessariamente todo o GitHub.
- **Limites das estrelas:** a métrica não equivale a uma avaliação de qualidade técnica.
- **Dimensão temporal:** dados coletados em um único momento não descrevem, por si só, a evolução histórica da popularidade.
- **Reprodutibilidade:** consultas, datas, parâmetros e procedimentos precisam ser documentados para permitir a repetição da análise.
- **Validação empírica:** hipóteses sobre concentração e desigualdade precisam ser sustentadas por dados e medidas adequadas.

Essas limitações devem orientar a leitura dos resultados e o desenvolvimento de versões posteriores.

---

## 🔭 Possíveis evoluções

O projeto oferece uma base para investigações e melhorias futuras, tais como:

- 📈 **Análise temporal:** acompanhar a evolução das estrelas e de outros indicadores ao longo do tempo.
- 📐 **Medidas de desigualdade:** explorar índices de concentração e distribuição, como Gini, quando metodologicamente apropriado.
- 📊 **Análises comparativas:** investigar diferenças entre linguagens, categorias de projetos e faixas de popularidade.
- 📦 **Exportação de dados:** permitir a geração de arquivos CSV ou Parquet.
- 🔁 **Reprodutibilidade:** registrar parâmetros de consulta, datas de coleta e versões das dependências.
- 🧪 **Testes automatizados:** verificar comportamentos críticos da coleta, do processamento e da apresentação.
- 📚 **Documentação metodológica:** registrar critérios, limitações e procedimentos necessários para reproduzir os resultados.
- 🌐 **Integração por API própria:** avaliar a disponibilização dos dados processados por uma interface de consumo externo.

Esses itens representam possibilidades de evolução, não funcionalidades cuja implementação esteja necessariamente concluída.

---

## 🗂️ Contexto histórico e evolução

Este repositório preserva uma etapa inicial do trabalho de desenvolvimento e investigação em torno da análise de dados, da visibilidade digital e da construção de ferramentas analíticas.

Os arquivos e commits mantidos aqui constituem parte do registro técnico dessa etapa. O repositório deve ser compreendido dentro de seu próprio contexto histórico, sem que isso implique representar integralmente o estado atual de iniciativas posteriores.

A evolução do trabalho pode ser documentada futuramente por meio de versões, registros de desenvolvimento e publicações específicas, respeitando a distinção entre o código disponível neste repositório e eventuais implementações posteriores.

Este registro histórico também permite acompanhar decisões iniciais de concepção, escolhas tecnológicas e questões de pesquisa que podem ser retomadas, revisadas ou ampliadas em trabalhos subsequentes.

---

## 👤 Autoria

**Jhon Max Polins Ribeiro**

Projeto de desenvolvimento de software e análise exploratória de dados.

---

## 💡 Consideração final

O *Anatomia do Capital Digital* parte de uma questão simples: o que acontece quando popularidade passa a funcionar como sinônimo de relevância?

Ao transformar dados da plataforma em informações exploráveis, o projeto propõe examinar criticamente os indicadores que organizam a atenção no ambiente digital.

Seu valor não está em oferecer uma classificação definitiva dos projetos, mas em tornar mais visíveis os critérios, os padrões e as limitações envolvidos nessa interpretação.

> **Visualizar dados não é, por si só, compreender a realidade. É criar condições para investigá-la, questioná-la e interpretá-la com rigor.**
