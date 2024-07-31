import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


symbol = st.sidebar.text_input("Hisse Senedi Sembolü",value='ASELS')
st.title(symbol+ " Hisse Senedi Grafiği")

start_date = st.sidebar.date_input("Baslangıc Tarihi", value=datetime(2020,1,1))
end_date = st.sidebar.date_input("Bitis Tarihi", value=datetime.now())

df = yf.download(symbol+ ".IS",start=start_date,end=end_date)
st.subheader("Hisse Senedi Trend Grafiği")
st.line_chart(df['Close'])
st.subheader("Hisse Senedi Fiyatlar Tablosu")
st.write(df)









