import streamlit as st
import queries.meta_ads as mq
import queries.google_ads as gq
import bootstrap as bs
import altair as alt
from datetime import date

def metrics_today(customer, col1, col2, col3, col4):
    stats = mq.get_stats(bs.meta_ads_accounts[customer], [date.today(), date.today()])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Impressions", stats['Impressions'][0], help='The number of times an ad is viewed in this period of time.')
    col2.metric("Clicks", stats['Clicks'][0], help='The number of times an ad is clicked in this period of time.')
    col3.metric("Cost", stats['Cost'][0], help='The total advertising cost in this period of time, in $USD.')
    col4.metric("CPC", stats['CPC'][0], help='The average cost per click in this period of time, in $USD.')

def metrics(platform, col1, col2, col3, col4):
    '''
    Create a metrics panel that contains impressions, clicks, cost, cpc for the current selected customer and date.
    '''
    dates = [st.session_state.start_date, st.session_state.end_date]
    if platform == 'Meta Ads':
        stats = mq.get_stats(bs.meta_ads_accounts[st.session_state.customer], dates)
    elif platform == 'Google Ads':
        stats = gq.get_stats(bs.google_ads_client, bs.google_ads_ids[st.session_state.customer], dates)
    else:
        raise ValueError("No such platform")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Impressions", stats['Impressions'][0], help='The number of times an ad is viewed in this period of time.')
    col2.metric("Clicks", stats['Clicks'][0], help='The number of times an ad is clicked in this period of time.')
    col3.metric("Cost", stats['Cost'][0], help='The total advertising cost in this period of time, in $USD.')
    col4.metric("CPC", stats['CPC'][0], help='The average cost per click in this period of time, in $USD.')

def line_chart():
    '''
    Create a line chart visualization panel that for the current selected customer, date, and metric.
    '''
    dates = [st.session_state.start_date, st.session_state.end_date]
    stats = mq.get_daily_stats(bs.meta_ads_accounts[st.session_state.customer], dates)
    chart = alt.Chart(stats).mark_line().encode(
        x='Date:T', 
        y=f'{st.session_state.metric}:Q'
    ).properties(width=650).interactive()
    return st.altair_chart(chart)