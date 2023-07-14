import streamlit as st
from datetime import date, timedelta

def _select_dates(start, end):
    st.session_state.start_date = start
    st.session_state.end_date = end

def _select_metric(metric):
    st.session_state.metric = metric

def date_range_selector(col1, col2):
    col1.date_input("Start Date", key='start_date', max_value=date.today())
    col2.date_input("End Date", key='end_date', max_value=date.today())

def date_buttons(col1, col2):
    col1.button('Last week', on_click=_select_dates, args=[date.today() - timedelta(7), date.today()])
    col2.button('Last month', on_click=_select_dates, args=[date.today() - timedelta(30), date.today()])
    col1.button('Last Quarter', on_click=_select_dates, args=[date.today() - timedelta(120), date.today()])
    col2.button('Last year', on_click=_select_dates, args=[date.today() - timedelta(365), date.today()])

def customer_selectbox(customers):
    return st.selectbox('Customer', customers, key='customer')

def metric_buttons(col1, col2):
    col1.button('Impressions', on_click=_select_metric, args=['Impressions'])
    col2.button('Clicks', on_click=_select_metric, args=['Clicks'])
    col1.button('Cost', on_click=_select_metric, args=['Cost'])
    col2.button('CPC', on_click=_select_metric, args=['CPC'])