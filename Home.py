import streamlit as st
import numpy as np
# from dataset import newDfDrivers
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
    # st.dataframe(newDfDrivers)

# Tab 2
with tab2:
    st.subheader("First analisys about ...")
    # chart_data = ageGroupCounts
    # st.bar_chart(chart_data)

    # st.caption('This is a string that explains something above.')
    # st.caption(
    #     'A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# Tab 3
with tab3:
    st.subheader("Second analisys about ...")
