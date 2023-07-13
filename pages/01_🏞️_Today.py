import streamlit as st
import queries.meta_ads as mq
# import google_ads_queries.queries as gq
import altair as alt
import bootstrap as bs
# import google_ads_queries.config as gc
from datetime import date, timedelta, datetime
import pandas as pd

'# 🏞️ Today'
f'### Today is {date.today()}, {date.today().strftime("%A")}'
tab1, tab2 = st.tabs(["UCM", "iTalkBB"])
with tab1:
    col21, col22, col23, col24 = st.columns(4)
    stats = mq.get_stats(bs.meta_ads_accounts['ucm'], 'today')

    col21.metric("Impressions", stats['Impressions'][0])
    col22.metric("Clicks", stats['Clicks'][0])
    col23.metric("Cost", stats['Cost'][0])
    col24.metric("CPC", stats['CPC'][0])

with tab2:
    'missing'