import streamlit as st
import pandas as pd
import numpy as np
# from utils import formatNumber
from dataset import since1970NewDfDrivers_reset
# from graphics import ageGroupCounts


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
    st.write('Esta tabela mostra dados de alguns pilotos de F1, tendo como critério os nascidos a partir de 1970.')
    st.metric('Total de Pilotos', len(since1970NewDfDrivers_reset))
    st.dataframe(since1970NewDfDrivers_reset, use_container_width=False)


# Tab 2
with tab2:
    st.subheader("First analisys about Age Group ...")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

# Tab 3
with tab3:
    st.subheader("First analisys about Nationalities...")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
