""" 
This is a simple stock price app that shows the stock closing price and volume of Google. ""
"""

import warnings
import yfinance as yf
import pandas as pd
import streamlit as st


warnings.simplefilter(action="ignore", category=FutureWarning)

st.write(
    """
# Simple Stock Price App
Shown are the stock **closing price** and volume of Google!
"""
)

ticker_symbol = "GOOGL"
tickerData = yf.Ticker(ticker_symbol)

tickerDf = tickerData.history(period="1d", start="2010-5-31", end="2023-1-31")

dst_error_hours = pd.to_timedelta(4, unit="h")
tickerDf.index += dst_error_hours

st.write(
    """
         ## Closing Price
         """
)
st.line_chart(tickerDf.Close)

st.write(
    """
         ## Volume Price
         """
)
st.line_chart(tickerDf.Volume)
