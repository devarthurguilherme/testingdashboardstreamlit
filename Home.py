import streamlit as st
import pandas as pd
import numpy as np
from dataset import dfDrivers
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
    st.write('This Dataframa is about ...')
    # st.dataframe(df, use_container_width=True)
    st.dataframe(dfDrivers, use_container_width=True)


# Tab 2
with tab2:
    st.subheader("First analisys about ...")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

# Tab 3
with tab3:
    st.subheader("First analisys about ...")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
