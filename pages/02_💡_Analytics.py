import streamlit as st
import queries.meta_ads as mq
# import google_ads_queries.queries as gq
import altair as alt
import bootstrap as bs
# import google_ads_queries.config as gc

f"""
# Browse by Customer
"""

tab1, tab2 = st.tabs(["UCM", "iTalkBB"])

date = ["2022-11-01", "2022-11-30"]

with tab1:
    col1, col2, col3, col4 = st.columns(4)

    campaign_stats = mq.get_campaign_stats(bs.meta_ads_accounts['ucm'], ["2022-11-01", "2022-11-30"])
    campaign_count = campaign_stats.shape[0]
    col1.metric("Campaigns", campaign_count)

    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")


with tab2:
    col1, col2 = st.columns(2)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns", "12", "9%")
    col2.metric("Impressions", "57", "-6%")
    col3.metric("Conversions", "57", "-6%")
    col4.metric("Cost", "57", "-6%")

