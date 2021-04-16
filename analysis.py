#!/usr/bin/env python
# coding: utf-8

# # Stock analysis
# 
# - [WazirX API Docs](https://github.com/WazirX/wazirx-api)
# 

# In[19]:


import os
import json
from datetime import datetime
import requests as req
import numpy as np
import pandas as pd


# In[17]:


TICKERS='https://api.wazirx.com/api/v2/tickers'
TRADE_HISTORY='https://api.wazirx.com/api/v2/trades?market=' # uses a ticker here
MARKET_DEPTH='https://api.wazirx.com/api/v2/depth?market='# uses a ticker here


# In[12]:


# Creating a ticker list
res = req.get(TICKERS)
tickers_list= [ key for key, items in res.json().items()]


# In[36]:


trade_history = req.get(TRADE_HISTORY+tickers_list[1])
# trade_history.json()


# In[34]:


# Converting timestamp to date time
market_depth = req.get(MARKET_DEPTH+tickers_list[1])
market_depth = market_depth.json()
market_depth['timestamp'] = datetime.fromtimestamp(market_depth['timestamp'])


# In[33]:





# In[ ]:




