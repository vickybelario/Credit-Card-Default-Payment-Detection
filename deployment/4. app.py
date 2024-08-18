import streamlit as st
import pandas as pd
import numpy as np
import eda


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Graded Challenge 5')
    st.write('Nama      : Vicky Belario')
    st.write('Batch     : 017')
    st.write('Tujuan    : Graded Challenge 5 ini dilakukan untuk mengaplikasikan model classification pada dataset credit_card_default')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
elif page == 'Exploration Data Analysis':
    eda.run()  # Assuming eda.run() function handles the EDA and outputs necessary visuals
else:
    st.write('') 
