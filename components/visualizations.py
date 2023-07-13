import streamlit as st
import queries.meta_ads as mq
import bootstrap as bs
import altair as alt
from datetime import date

def metrics_today(customer, col1, col2, col3, col4):
    col1, col2, col3, col4 = st.columns(4)
    stats = mq.get_stats(bs.meta_ads_accounts[customer], [date.today(), date.today()])
    col1.metric("Impressions", stats['Impressions'][0])
    col2.metric("Clicks", stats['Clicks'][0])
    col3.metric("Cost", stats['Cost'][0])
    col4.metric("CPC", stats['CPC'][0])

def metrics(col1, col2, col3, col4):
    col1, col2, col3, col4 = st.columns(4)
    stats = mq.get_stats(bs.meta_ads_accounts[st.session_state.customer], [st.session_state.start_date, st.session_state.end_date])
    
    col1.metric("Impressions", stats['Impressions'][0])
    col2.metric("Clicks", stats['Clicks'][0])
    col3.metric("Cost", stats['Cost'][0])
    col4.metric("CPC", stats['CPC'][0])

def line_chart():
    stats_daily = mq.get_stats(
        bs.meta_ads_accounts[st.session_state.customer],
        [st.session_state.start_date, st.session_state.end_date], 1)
    chart = alt.Chart(stats_daily).mark_bar().encode(
        x=alt.X('Date start:T', axis=alt.Axis(title='Date', format='%m-%d')), 
        y=f'{st.session_state.metric}:Q'
    ).properties(width=700).interactive()
    return st.altair_chart(chart)