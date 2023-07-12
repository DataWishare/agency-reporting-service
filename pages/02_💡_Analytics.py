import streamlit as st
import queries.meta_ads as mq
# import google_ads_queries.queries as gq
import altair as alt
import bootstrap as bs
# import google_ads_queries.config as gc
from datetime import date, timedelta, datetime

f"""
# Browse by Customer
"""

tab1, tab2 = st.tabs(["UCM", "iTalkBB"])
def create_date_range_selector(col11, col12):
    min_date = mq.get_stats(bs.meta_ads_accounts['ucm'])['Date start'][0]
    min_date = datetime.strptime(min_date, "%Y-%m-%d")
    max_date = date.today()

    start_date = col11.date_input("Start Date", max_date - timedelta(30), min_value=min_date, max_value=max_date)
    end_date = col12.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

    return [start_date, end_date]

with tab1:

    col11, col12 = st.columns(2)

    dates = create_date_range_selector(col11, col12)
    col21, col22, col23, col24 = st.columns(4)
    stats = mq.get_stats(bs.meta_ads_accounts['ucm'], dates)

    col21.metric("Impressions", stats['Impressions'][0])
    col22.metric("Clicks", stats['Clicks'][0])
    col23.metric("CPC", stats['CPC'][0])
    col24.metric("Cost", stats['Cost'][0])


with tab2:
    col1, col2 = st.columns(2)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns", "12", "9%")
    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")

