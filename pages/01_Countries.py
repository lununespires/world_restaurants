import pandas as pd
import streamlit as st
import plotly.express as px
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

from utils.process_data import process_data

raw_data_path = ('./data/zomato.csv')

df = process_data(raw_data_path)

st.set_page_config(page_title="Countries", layout="wide")

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
    st.markdown("# :earth_americas: Visão Países")
    df_rest = df[['country_code', 'restaurant_id']].groupby(['country_code']).count().sort_values('restaurant_id', ascending=False).reset_index()
    
    fig = px.bar(df_rest, x = 'country_code', y='restaurant_id', text="restaurant_id", title="Quantidade de Restaurantes Registrados por País",    labels={
            "country_code": "Paises",
            "restaurant_id": "Quantidade de Restaurantes",
        },)
    st.plotly_chart(fig, use_container_width=True)

    df_cities = df[['country_code', 'city']].groupby(['country_code']).nunique().sort_values('city', ascending=False).reset_index()
    fig = px.bar(df_cities, x = 'country_code', y='city', text="city", title="Quantidade de cidades por País",    labels={
            "country_code": "Paises",
            "city": "Quantidade de cidades",
        },)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2, gap='small')
    with col1:
        df_votes_mean = round(df[['country_code','votes']].groupby('country_code').mean().sort_values('votes', ascending=False), 2).reset_index()
        fig = px.bar(df_votes_mean, x = 'country_code', y = 'votes', text='votes', title='Media de avaliacoes por Pais', labels={
            'country_code' : 'Paises',
            'votes': 'Media da Quantidade de Avaliacoes'
        })
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        df_cost_for_two = round(df[['country_code','average_cost_for_two']].groupby('country_code').mean().sort_values('average_cost_for_two', ascending=False), 2).reset_index()
        fig = px.bar(df_cost_for_two, x = 'country_code', y = 'average_cost_for_two', text='average_cost_for_two', title='Preco medio de um prato para 2 pessoas', labels={
            'country_code' : 'Paises',
            'average_cost_for_two': 'Media de um prato para 2 pessoas'
        })
        st.plotly_chart(fig, use_container_width=True)


    






