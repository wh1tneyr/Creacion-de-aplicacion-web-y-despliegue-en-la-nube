import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

st.header('Anuncios de autos a la venta')
st.write('Aplicación en construcción')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
car_model= car_data['model'].reset_index()

if build_histogram: # si la casilla de verificación está seleccionada
    #escribir un mensaje
    st.write(
        'Creación de un histograma para la verificación según el modelo de auto')
    
    #crear un histograma
    fig_2 = px.histogram(car_model, x='model')
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)   

