import streamlit as st
import queries.meta_ads as mq
# import google_ads_queries.queries as gq
import altair as alt
import bootstrap as bs
# import google_ads_queries.config as gc
from datetime import date, timedelta, datetime
import pandas as pd

'# 💡 Analytics'

if 'start_date' not in st.session_state:
    st.session_state.start_date = date.today() - timedelta(30)
if 'end_date' not in st. session_state:
    st.session_state.end_date = date.today()
if 'metric' not in st.session_state:
    st.session_state.metric = 'Impressions'
min_date = mq.get_stats(bs.meta_ads_accounts['ucm'])['Date start'][0]
min_date = datetime.strptime(min_date, "%Y-%m-%d").date()

tab1, tab2 = st.tabs(["UCM", "iTalkBB"])
def select_dates(start, end):
    st.session_state.start_date = start
    st.session_state.end_date = end
def select_metric(metric):
    st.session_state.metric = metric
def create_date_range_selector(col11, col12):
    min_date = mq.get_stats(bs.meta_ads_accounts['ucm'])['Date start'][0]
    min_date = datetime.strptime(min_date, "%Y-%m-%d")
    col11.date_input("Start Date", key='start_date', min_value=min_date, max_value=date.today())
    col12.date_input("End Date", key='end_date', min_value=min_date, max_value=date.today())

with tab1:

    yesterday = date.today() - timedelta(1)
    with st.sidebar:
        '### Select a date range'
        col11, col12 = st.columns(2)

        create_date_range_selector(col11, col12)
        col11.button('Last 3 days', on_click=select_dates, args=[yesterday - timedelta(3), yesterday])
        col12.button('Last week', on_click=select_dates, args=[yesterday - timedelta(7), yesterday])
        col11.button('Last month', on_click=select_dates, args=[yesterday - timedelta(30), yesterday])
        col12.button('Last Quarter', on_click=select_dates, args=[yesterday - timedelta(120), yesterday])
        col11.button('Last year', on_click=select_dates, args=[yesterday - timedelta(365), yesterday])
        col12.button('Maximum', on_click=select_dates, args=[min_date, yesterday])
        '### Select a metric'
        col31, col32 = st.columns(2)
        col31.button('Impressions', on_click=select_metric, args=['Impressions'])
        col32.button('Clicks', on_click=select_metric, args=['Clicks'])
        col31.button('Cost', on_click=select_metric, args=['Cost'])
        col32.button('CPC', on_click=select_metric, args=['CPC'])
    ''
    col21, col22, col23, col24 = st.columns(4)
    stats = mq.get_stats(bs.meta_ads_accounts['ucm'], [st.session_state.start_date, st.session_state.end_date])

    col21.metric("Impressions", stats['Impressions'][0])
    col22.metric("Clicks", stats['Clicks'][0])
    col23.metric("Cost", stats['Cost'][0])
    col24.metric("CPC", stats['CPC'][0])
    
    stats_daily = mq.get_stats(bs.meta_ads_accounts['ucm'], [st.session_state.start_date, st.session_state.end_date], 1)
    chart = alt.Chart(stats_daily).mark_bar().encode(
        x=alt.X('Date start:T', axis=alt.Axis(title='Date', format='%m-%d')), 
        y=f'{st.session_state.metric}:Q'
    ).properties(width=700).interactive()

    st.altair_chart(chart)


    
with tab2:
    col1, col2 = st.columns(2)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns", "12", "9%")
    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")

