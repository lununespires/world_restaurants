# Libraries
import folium
import streamlit as st
from PIL import Image
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import plotly.graph_objects as go

from utils.process_data import process_data

raw_data_path = ('./data/zomato.csv')
icon = Image.open('./img/restaurante.png')

df = process_data(raw_data_path)

st.set_page_config(page_title= 'Home', page_icon= icon, layout='wide')

# -----------------
# Sidebar
# -----------------

with st.container():

    col1, col2 = st.sidebar.columns([1,2], gap='small')
    with col1:
        image = Image.open('./img/restaurante.png')
        st.image(image, width=80)
    with col2:
        st.header('pinPop! seu restaurante pelo mundo!')

st.sidebar.subheader('Países')
countries = st.sidebar.multiselect('Escolhe os paises que deseja visualizar os dados', df.loc[:, 'country_code'].unique().tolist(), ['India', 'Australia', 'Brazil', 'Canada', 'England', 'United States of America'])

st.sidebar.markdown("""---""")
st.sidebar.title('Dados tratados')

def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.sidebar.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

# -----------------
# Filter
# -----------------
df = df.loc[(df['country_code'].isin(countries)), :]


# -----------------
# layout
# -----------------
with st.container():
    image = Image.open('./img/restaurante.png')
    st.image(image, width=100)
    st.title('pinPop!')
           
    st.subheader('seu restaurante pelo mundo')
    st.write('Veja abaixo alguns dados de nossas plataforma:')
    
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            df_restaurant = len(df['restaurant_id'].unique())
            st.metric('Restaurantes', df_restaurant)
        
        with col2:
            df_country = len(df['country_code'].unique())
            st.metric('Paises', df_country)
        
        with col3:
            df_city = len(df['city'].unique())
            st.metric('Cidades', df_city)
        
        with col4:
            df_votes = df['votes'].sum()
            st.metric('num. de Avaliacoes', f'{df_votes:,}'.replace(",","."))
        
        with col5:
            df_cuisine = len(df['cuisines'].unique())
            st.metric('Tipo de Culinaria', df_cuisine)

    f = folium.Figure(width=1920, height=1080)
    m = folium.Map(max_bounds=True).add_to(f)
    marker_cluster = MarkerCluster().add_to(m)

    for _, line in df.iterrows():
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["color_name"]}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {} ({}) for two"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
        ).add_to(marker_cluster)

    folium_static(m, width=1024, height=768)
