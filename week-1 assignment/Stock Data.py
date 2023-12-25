#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')


# In[2]:


import yfinance as yf
import pandas as pd

stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    stock_data.to_csv(f'{symbol}_stock_data.csv')

start_date = '2018-01-01'
end_date = '2022-01-01'

for stock in stocks:
    fetch_stock_data(stock, start_date, end_date)


# In[ ]:




