import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
# from dataset import df
# from graphics import ageGroupCounts


#################

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)


#########


# Layout Wide Origin Config
st.set_page_config(layout='wide')

# Page Title
st.title("Home")

# Tabs
tab1, tab2, tab3 = st.tabs(
    ['Dataframe', 'Tab 2', 'Tab 3'])

# Dataframe
with tab1:
    st.subheader("Dataset Drivers")
    st.write('This Dataframa is about ...')
    st.dataframe(df, use_container_width=True)
    # st.dataframe(newDfDrivers)
    # Show Full Dataframe
    # st.dataframe(df)

# Tab 2
with tab2:
    st.subheader("First analisys about ...")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    # chart_data = ageGroupCounts
    # st.bar_chart(chart_data)

    # st.caption('This is a string that explains something above.')
    # st.caption(
    #     'A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# Tab 3
with tab3:
    # Dados de exemplo
    categorias = ['A', 'B', 'C']
    valores = [10, 20, 15]

    # Criar o gráfico de barras
    fig = go.Figure(data=[go.Bar(x=categorias, y=valores)])

    # Personalizar o layout do gráfico
    fig.update_layout(
        title='Gráfico de Barras com Plotly',
        xaxis_title='Categorias',
        yaxis_title='Valores'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)
