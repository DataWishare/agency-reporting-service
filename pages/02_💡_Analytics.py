import streamlit as st
import queries.meta_ads as mq
# import google_ads_queries.queries as gq
import altair as alt
import bootstrap as bs
# import google_ads_queries.config as gc
from datetime import date

f"""
# Browse by Customer
"""

tab1, tab2 = st.tabs(["UCM", "iTalkBB"])
def create_date_range_selector(col1, col2):
    min_date = date(2020, 1, 1)
    max_date = date.today()

    start_date = col11.date_input("Start Date", min_value=min_date, max_value=max_date)
    end_date = col12.date_input("End Date", min_value=min_date, max_value=max_date)
    if end_date < start_date:
        raise ValueError("End date is smaller than start date.")
    return [start_date, end_date]

with tab1:
    try:
        col11, col12 = st.columns(2)
    
        dates = create_date_range_selector(col11, col12)
        col21, col22, col23, col24 = st.columns(4)
        summary = mq.get_summary(bs.meta_ads_accounts['ucm'], dates)
        impressions = summary['Impressions']
        col21.metric("Impressions", int(impressions))

        clicks = summary['Clicks']
        col22.metric("Clicks", int(clicks))

        conversions = summary['CPC']
        col23.metric("CPC", conversions)

        cost = summary['Cost']
        col24.metric("Cost", cost)

    except ValueError as err:
        st.write(str(err))


with tab2:
    col1, col2 = st.columns(2)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns", "12", "9%")
    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")

