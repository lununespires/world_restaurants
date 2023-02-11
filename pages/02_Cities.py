import pandas as pd
import streamlit as st
import plotly.express as px
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

from utils.process_data import process_data

raw_data_path = ('./data/zomato.csv')

df = process_data(raw_data_path)

st.set_page_config(page_title="Cities", layout="wide")

# -----------------
# Sidebar
# -----------------

st.sidebar.title('Filtros')
st.sidebar.subheader('Faixa de Preco')
slider_range = st.sidebar.slider('Valores entre:', 0, 4, 4)
st.sidebar.write('###### 1 = barato / 2 = normal / 3 = caro / 4 = gourmet')

st.sidebar.subheader('Países')
countries = st.sidebar.multiselect('Escolhe os paises que deseja visualizar os dados', df.loc[:, 'country_code'].unique().tolist(), ['India', 'Australia', 'Brazil', 'Canada', 'England'])

# -----------------
# Filter
# -----------------
df = df.loc[(df['price_range']<=slider_range), :]
df = df.loc[(df['country_code'].isin(countries)), :]


# -----------------
# layout
# -----------------
with st.container():
    st.markdown("# :cityscape: Visão Cidades")
    





