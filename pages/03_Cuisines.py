import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


from utils.process_data import process_data

raw_data_path = ('./data/zomato.csv')

df = process_data(raw_data_path)

st.set_page_config(page_title='Cuisines', layout='wide')

# -----------------
# Sidebar
# -----------------

st.sidebar.title('Filtros')
st.sidebar.subheader('Quantidade de Restaurantes que deseja visualizar')

slider_range = st.sidebar.slider('Valores entre:', 1, 20, 10)
countries = st.sidebar.multiselect('Escolhe os paises que deseja visualizar os dados', df.loc[:, 'country_code'].unique().tolist(), ['Australia', 'Brazil', 'Canada', 'England', 'India', 'United States of America'])

# -----------------
# layout
# -----------------
with st.container():
    st.markdown('# :knife_fork_plate: Tipo de Culinaria')
    st.subheader('Alguns dos melhores restaurantes e tipo culinario:')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        df_italian_rating = df.loc[(df['cuisines'] == 'Italian'), ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_code']].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        st.metric(f'Italiana:', df_italian_rating.iloc[0,1], f'{df_italian_rating.iloc[0,2]}/5 - {df_italian_rating.iloc[0,3]}')

    with col2:
            df_american_rating = df.loc[(df['cuisines'] == 'American'), ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_code']].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
            st.metric(f'American:', df_american_rating.iloc[0,1], f'{df_american_rating.iloc[0,2]}/5 - {df_american_rating.iloc[0,3]}')
    with col3:
                df_arabian_rating = df.loc[(df['cuisines'] == 'Arabian'), ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_code']].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
                st.metric(f'Arabian:', df_arabian_rating.iloc[0,1], f'{df_arabian_rating.iloc[0,2]}/5 - {df_arabian_rating.iloc[0,3]}')
    with col4:
                df_japanese_rating = df.loc[(df['cuisines'] == 'Japanese'), ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_code']].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
                st.metric(f'Japanese:', df_japanese_rating.iloc[0,1], f'{df_japanese_rating.iloc[0,2]}/5 - {df_japanese_rating.iloc[0,3]}')
    with col5:
        df_home_rating = df.loc[(df['cuisines'] == 'Home-made'), ['restaurant_id', 'restaurant_name', 'aggregate_rating', 'country_code']].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        st.metric(f'Home-made:', df_home_rating.iloc[0,1], f'{df_home_rating.iloc[0,2]}/5 - {df_home_rating.iloc[0,3]}')

with st.container():
    st.subheader('Os Top Restaurantes')
    df = df.loc[(df['country_code'].isin(countries)), :]

    col1, col2 = st.columns(2)
    with col1:
        df_top = df.groupby(['restaurant_id', 'restaurant_name', 'city', 'country_code','cuisines', 'aggregate_rating']).mean().sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index()
        st.dataframe(df_top[['restaurant_name', 'city','country_code','cuisines', 'aggregate_rating']].head(slider_range))
    
    with col2:
        fig = go.Figure(data=[go.Pie(labels=df_top['cuisines'].head(slider_range), values=df_top['aggregate_rating'].head(slider_range), title="Tipo de culinaria dos Top restaurantes em percentual", pull=[0, 0.2, 0])])
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        df_top_cuisines = round(df[['cuisines', 'aggregate_rating']].groupby(['cuisines']).mean().sort_values(['aggregate_rating'], ascending=[False]), 2).reset_index()
        fig = px.bar(df_top_cuisines.head(slider_range), x = 'cuisines', y='aggregate_rating', text="aggregate_rating", title="Melhor media das avaliacoes por tipo de culianaria", color='aggregate_rating', labels={
            "cuisines": 'Culinaria',
            "aggregate_rating": "Media das Avaliacoes"}, )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        df_worst_cuisines = round(df[['cuisines', 'aggregate_rating']].groupby(['cuisines']).mean().sort_values(['aggregate_rating']), 2).reset_index()
        fig = px.bar(df_worst_cuisines.head(slider_range), x = 'cuisines', y='aggregate_rating', text="aggregate_rating", title="Pior media das avaliacoes por tipo de culianaria", color='aggregate_rating', labels={
            "cuisines": 'Culinaria',
            "aggregate_rating": "Media das Avaliacoes"}, )
        st.plotly_chart(fig, use_container_width=True)
 

    