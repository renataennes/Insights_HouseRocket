import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="House Rocket Dashboard", layout="wide")

# --- FUNÇÕES OTIMIZADAS COM CACHE ---

url = "kc_house_data.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url, sep=None, engine='python')
    df['date'] = pd.to_datetime(df['date'])
    
    # Feature Engineering: Níveis de Preço (Quartis)
    q1, q2, q3 = df['price'].quantile([0.25, 0.5, 0.75])
    def classify(x):
        if x <= q1: return "0-Baixo"
        if x <= q2: return "1-Médio Baixo"
        if x <= q3: return "2-Médio Alto"
        return "3-Alto"
    
    df['level'] = df['price'].apply(classify)
    
    # Insight de Valor: Localização vs Preço m²
    df['price_sqft'] = df['price'] / df['sqft_living']
    avg_price_zip = df.groupby('zipcode')['price'].transform('mean')
    df['value_score'] = avg_price_zip / df['price_sqft']
    
    return df

url = "kc_house_data.csv"
df = load_data(url)

# --- SIDEBAR (FILTROS) ---
st.sidebar.header("Filtros de Busca")
levels = st.sidebar.multiselect("Nível de Preço", df['level'].unique(), default=df['level'].unique())
min_price = int(df['price'].min())
max_price = int(df['price'].max())
price_range = st.sidebar.slider("Faixa de Preço", min_price, max_price, (min_price, max_price))

df_filtered = df[(df['level'].isin(levels)) & (df['price'].between(price_range[0], price_range[1]))]

# --- LAYOUT PRINCIPAL ---
st.title("🏡 House Rocket Data Analysis")

# Métricas principais
c1, c2, c3 = st.columns(3)
c1.metric("Imóveis Disponíveis", len(df_filtered))
c2.metric("Preço Médio", f"$ {df_filtered['price'].mean():,.2f}")
c3.metric("Melhor Oportunidade (Zipcode)", df.loc[df['value_score'].idxmax(), 'zipcode'])

# Gráfico de Linha (Seaborn-style mas em Plotly para interatividade)
st.subheader("📈 Preço Médio por Ano de Construção")
df_year = df_filtered.groupby('yr_built')['price'].mean().reset_index()
fig_line = px.line(df_year, x='yr_built', y='price', title="Tendência de Preços")
st.plotly_chart(fig_line, use_container_width=True)

# Mapa de Localização
st.subheader("🗺️ Mapa de Oportunidades")
st.markdown("O tamanho do ponto indica o **Índice de Valor** (maior = melhor custo-benefício).")
fig_map = px.scatter_mapbox(
    df_filtered.head(2000), # Limite para performance
    lat="lat", lon="long", color="level", size="value_score",
    hover_data=['price', 'zipcode'],
    mapbox_style="open-street-map", zoom=9, height=600
)
st.plotly_chart(fig_map, use_container_width=True)

# Tabela de Dados
st.subheader("📋 Amostra dos Dados")
st.dataframe(df_filtered[['id', 'price', 'zipcode', 'level', 'value_score']].head(50))
