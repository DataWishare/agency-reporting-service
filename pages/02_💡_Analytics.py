from states import init_analytics_states
init_analytics_states()

import streamlit as st
import components.selectors as sl
from components.visualizations import metrics, line_chart
from components.hide_footer import hide_footer

hide_footer()

with st.sidebar:

    '### Select a customer'
    st.selectbox('Customer', ['UCM', 'iTalkBB', 'Youtube'], key='customer')

    '### Select a date range'
    col11, col12 = st.columns(2)
    sl.date_range_selector(col11, col12)
    sl.date_buttons(col11, col12)

    '### Select a metric'
    col21, col22 = st.columns(2)
    sl.metric_buttons(col21, col22)

'# 💡 Analytics'
''
tab1, tab2 = st.tabs(['Meta Ads', 'Google Ads'])

with tab1:
    ''
    col1, col2, col3, col4 = st.columns(4)
    try:
        metrics('Meta Ads', col1, col2, col3, col4)
        ''
        line_chart()
    except:
        'Meta ads is not supported for this customer'


with tab2:
    ''
    col1, col2, col3, col4 = st.columns(4)
    try:
        metrics('Google Ads', col1, col2, col3, col4)
    except:
        'Google ads is not supported for this customer'