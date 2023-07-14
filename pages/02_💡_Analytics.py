import streamlit as st
import components.selectors as sl
from components.visualizations import metrics, line_chart
from components.state import init_states

init_states()

with st.sidebar:
    '### Select a customer'
    st.selectbox('Customer', ['UCM', 'iTalkBB'], key='customer')

    '### Select a date range'
    col11, col12 = st.columns(2)
    sl.date_range_selector(col11, col12)
    sl.date_buttons(col11, col12)

    '### Select a metric'
    col21, col22 = st.columns(2)
    sl.metric_buttons(col21, col22)

'# 💡 Analytics'
''
tab1, tab2 = st.tabs(["Meta Ads", "Google Ads"])

with tab1:
    ''
    col1, col2, col3, col4 = st.columns(4)
    metrics(col1, col2, col3, col4)
    ''
    line_chart()

with tab2:
    ''
    col1, col2 = st.columns(2)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns", "12", "9%")
    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")