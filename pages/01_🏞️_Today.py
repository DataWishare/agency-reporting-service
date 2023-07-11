import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vega_datasets import data
from datetime import date


f"""
# Today is {date.today()}, {date.today().strftime("%A")}
"""

chart_data = pd.DataFrame(
np.random.randn(200, 3),
columns=['a', 'b', 'c'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})