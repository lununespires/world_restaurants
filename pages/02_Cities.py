import streamlit as st
import plotly.express as px

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
countries = st.sidebar.multiselect('Escolhe os paises que deseja visualizar os dados', df.loc[:, 'country_code'].unique().tolist(), ['Australia', 'Brazil', 'Canada', 'England', 'India', 'United States of America'])

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
    df_rest = df[['country_code', 'restaurant_id', 'city']].groupby(['country_code', 'city']).count().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(df_rest.head(10), x = 'city', y='restaurant_id', text="restaurant_id", title="Top 10 cidades com mais restaurantes na Base de Dados",  color='country_code',  labels={
            "country_code": "Paises",
            "restaurant_id": "Quantidade de Restaurantes",
        }, )
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        df_city_mean_4 = df.loc[df['aggregate_rating'] >=4, ['city', 'restaurant_id', 'country_code']].groupby(['country_code','city']).count().sort_values(['restaurant_id', 'city'], ascending=[False,True]).reset_index()

        fig = px.bar(df_city_mean_4.head(7), x = 'city', y='restaurant_id', text="restaurant_id", title="Top 7 cidades com media acima de 4",  color='country_code',  labels={
            "country_code": "Paises",
            "restaurant_id": "Quantidade de Restaurantes",
        }, )
        st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            df_city_mean_2 = df.loc[df['aggregate_rating'] <=2.5, ['city', 'restaurant_id', 'country_code']].groupby(['country_code','city']).count().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()

            fig = px.bar(df_city_mean_2.head(7), x = 'city', y='restaurant_id', text="restaurant_id", title="Top 7 cidades com media abaixo de 2.5",  color='country_code',  labels={
                "country_code": "Paises",
                "restaurant_id": "Quantidade de Restaurantes",
            }, )
            st.plotly_chart(fig, use_container_width=True)

with st.container():
    df_city_cuisine = df[['city', 'cuisines', 'country_code']].groupby(['city', 'country_code']).nunique().sort_values(['cuisines', 'country_code'], ascending=[False, False]).reset_index()

    fig = px.bar(df_city_cuisine.head(10), x = 'city', y='cuisines', text="cuisines", title="Top 7 cidades com maior numeros de diferentes tipos de culinaria",  color='country_code' )
    st.plotly_chart(fig, use_container_width=True)