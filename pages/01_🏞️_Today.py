import streamlit as st
# import google_ads_queries.queries as gq
# import google_ads_queries.config as gc
from datetime import date
import components.selectors as sl
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