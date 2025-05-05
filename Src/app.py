import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

#Cabeçalho do app
st.header("Análise do valor de Veículos por KM")

car_data = pd.read_csv(Path("Data/vehicles.csv")) # lendo os dados
graph_button = st.button("Criar gráfico")#Criando um botão
hist_button = st.button("Criar histograma")

if graph_button:#Se o botão de grafico por pressionado
    st.write("Grafico de dispersão: Preço x Quilometragem")
    fig_graph = px.scatter(car_data, x="odometer", y="price") # criando um gráfico de dispersão
    st.plotly_chart(fig_graph, use_container_width=True)


if hist_button:
        st.write("Histograma da quilometragem de veiculos")
        fig_hist = px.histogram(car_data, x="odometer") # criando um histograma
        st.plotly_chart(fig_hist, use_container_width=True)

