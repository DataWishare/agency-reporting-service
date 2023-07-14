import streamlit as st
from components.hide_footer import hide_footer

hide_footer()

st.image("logo.jpg")

'# Wishare Media Marketing Performance Tracking Service'
''
col1, col2 = st.columns(2)
col1.metric("Customers", "12", "9%")
col2.metric("Platforms", "57", "-6%")
''
''
'*3380 Flair Dr, Unit 110, El Monte, CA 91770*'
'**Wishare Media Group © 2023**'
