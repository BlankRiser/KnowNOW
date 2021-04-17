
from dotenv import load_dotenv
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import os
import io
import datetime
import requests as req
import numpy as np
import pandas as pd

from helper_functions import *

# Setting streamlit page options
st.set_page_config(layout="wide")
# left, right = st.beta_columns((4, 1))
# left.title("Graphs")
# right.title("Options")

st.title("Analyze stocks, ETFs, and Cryptocurrencies ")
st.text("Made with 💗 by Ram Shankar Choudhary")

# load_dotenv()
# ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

# for Heroku
ALPHAVANTAGE_KEY = os.environ['ALPHAVANTAGE_API_KEY']


digital_list = pd.read_csv("digital_currency_list.csv")

# Input a symbol for stock, ETF, or Crypto
SYMBOL = 'IBM'
SYMBOL_INPUT = st.text_input('Enter a symbol')
if SYMBOL_INPUT == "":
    SYMBOL_INPUT = 'DOGE'


digital_list = pd.read_csv("physical_currency_list.csv")
marketOptions = list(digital_list['currency code'])
# Select the market you want to compare to
MARKET_INPUT = st.selectbox('Market', marketOptions)
if MARKET_INPUT == "":
    MARKET_INPUT = 'INR'


CRYPTO_RATING = 'https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol=' + \
    SYMBOL_INPUT+'&apikey='+ALPHAVANTAGE_KEY

if SYMBOL_INPUT is not None:
    # Crypto Daily - Candlestcik

    DIGITAL_CURRENCY_DAILY = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=' + \
        SYMBOL_INPUT+'&market='+MARKET_INPUT+'&apikey='+ALPHAVANTAGE_KEY+'&datatype=csv'

    res = req.get(DIGITAL_CURRENCY_DAILY)
    res = res.content
    rawData = pd.read_csv(io.StringIO(res.decode('utf-8')))

    # converting timestamp to datetime
    rawData['timestamp'] = pd.to_datetime(rawData['timestamp'])

    # Options to choose price actvity
    options = numericalValues(rawData)

    # Adding year and month
    rawData['Year'] = pd.DatetimeIndex(rawData['timestamp']).year
    rawData['Month'] = pd.DatetimeIndex(rawData['timestamp']).month

    st.subheader(
        f'Candlestick(OHLC) chart of {SYMBOL_INPUT} of {MARKET_INPUT} market')

    # Candlestick chart
    fig_candlestick = go.Figure(
        data=[
            go.Candlestick(
                x=rawData['timestamp'],
                open=rawData[f'open ({MARKET_INPUT})'],
                high=rawData[f'high ({MARKET_INPUT})'],
                low=rawData[f'low ({MARKET_INPUT})'],
                close=rawData[f'close ({MARKET_INPUT})']
            )
        ]
    )

    fig_candlestick.update_layout(
        title=f'{SYMBOL_INPUT} in {MARKET_INPUT} ',
        yaxis_title=f'{SYMBOL_INPUT}',
    )

    # st.plotly_chart(fig_candlestick, use_container_width=True)
    st.plotly_chart(fig_candlestick, use_container_width=True)

    chartOptionOne = st.selectbox("Select Price activity", options=options)

    # Scatter Chart
    fig_scatter = go.Figure(
        [go.Scatter(x=rawData['timestamp'], y=rawData[f'high ({MARKET_INPUT})'])])

    st.plotly_chart(fig_scatter, use_container_width=True)

    # Line Chart
    fig_line = px.line(rawData, x=rawData['timestamp'], y=[
                       f'high ({MARKET_INPUT})'], color="Year")

    fig_line.update_layout(
        title=f'{SYMBOL_INPUT} in {MARKET_INPUT} ',
        yaxis_title=f'{SYMBOL_INPUT} - {chartOptionOne}',

    )

    fig_line.add_hline(y=rawData[f'high ({MARKET_INPUT})'].mean(), line_dash="dot",
                       annotation_text="Summed Average",
                       annotation_position="bottom right")

    st.plotly_chart(fig_line, use_container_width=True)
else:
    st.subtitle("Please select a symbol")
