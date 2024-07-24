import streamlit as st

# Layout Wide Origin Config
st.set_page_config(layout='wide')

# Page Title
st.title("P1")

# Tabs
tab1, tab2, tab3 = st.tabs(
    ['Dataframe', 'Tab 2', 'Tab 3'])
