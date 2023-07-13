import streamlit as st
import queries.meta_ads as mq
# import google_ads_queries.queries as gq
import altair as alt
import bootstrap as bs
# import google_ads_queries.config as gc
from datetime import date, timedelta, datetime
import pandas as pd

'# 💡 Analytics'

tab1, tab2 = st.tabs(["UCM", "iTalkBB"])
def create_date_range_selector(col11, col12):
    min_date = mq.get_stats(bs.meta_ads_accounts['ucm'])['Date start'][0]
    min_date = datetime.strptime(min_date, "%Y-%m-%d")
    max_date = date.today()

    start_date = col11.date_input("Start Date", max_date - timedelta(30), min_value=min_date, max_value=max_date)
    end_date = col12.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

    return [start_date, end_date]

with tab1:

    '### Select a date range'
    col11, col12 = st.columns(2)

    dates = create_date_range_selector(col11, col12)
    yesterday = date.today() - timedelta(1)
    
    
    col31, col32, col33, col34, col35, col36 = st.columns(6)
    if col31.button('Yesterday'):
        dates = [yesterday, yesterday]
    if col32.button('Last week'):
        dates = [yesterday - timedelta(7), yesterday]
    if col33.button('Last month'):
        dates = [yesterday - timedelta(30), yesterday]
    if col34.button('Last Q'):
        dates = [yesterday - timedelta(120), yesterday]
    if col35.button('Last year'):
        dates = [yesterday - timedelta(365), yesterday]
    if col36.button('Maximum'):
        min_date = mq.get_stats(bs.meta_ads_accounts['ucm'])['Date start'][0]
        min_date = datetime.strptime(min_date, "%Y-%m-%d").date()
        dates = [min_date, yesterday]
    ''
    '### Performance'
    col21, col22, col23, col24 = st.columns(4)
    stats = mq.get_stats(bs.meta_ads_accounts['ucm'], dates)

    col21.metric("Impressions", stats['Impressions'][0])
    col22.metric("Clicks", stats['Clicks'][0])
    col23.metric("Cost", stats['Cost'][0])
    col24.metric("CPC", stats['CPC'][0])
    
    stats = mq.get_stats(bs.meta_ads_accounts['ucm'], dates, 1)
    chart = alt.Chart(stats).mark_bar().encode(x=alt.X('Date start:T').title('Date'), y='Clicks:Q').properties(width=700).interactive()
    st.altair_chart(chart)


with tab2:
    col1, col2 = st.columns(2)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns", "12", "9%")
    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")

