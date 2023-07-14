import streamlit as st
from datetime import date
from components.visualizations import metrics_today

f'# 🏞️ Today is {date.today()}, {date.today().strftime("%A")}'
''
tab1, tab2 = st.tabs(["Meta Ads", "Google Ads"])

with tab1:
    '**UCM**'
    col11, col12, col13, col14 = st.columns(4)
    metrics_today('UCM', col11, col12, col13, col14)

    '**iTalkBB**'

with tab2:
    'missing'