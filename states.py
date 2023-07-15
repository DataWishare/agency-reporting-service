import streamlit as st
from datetime import date, timedelta

def init_analytics_states():
    if 'customer' not in st.session_state:
        st.session_state.customer = 'UCM'
    if 'start_date' not in st.session_state:
        st.session_state.start_date = date.today() - timedelta(30)
    if 'end_date' not in st. session_state:
        st.session_state.end_date = date.today()
    if 'metric' not in st.session_state:
        st.session_state.metric = 'Impressions'