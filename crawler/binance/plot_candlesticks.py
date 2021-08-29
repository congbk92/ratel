import plotly.graph_objects as go

import pandas as pd
from datetime import datetime
import time

klines_header = ['open_time', 'open', 'high', 'low', 'close', \
                'volume', 'close_time', 'quote_vol', 'nums_trades', \
                'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'] 

df = pd.read_csv('daily_merged.csv', names=klines_header)

df['open_time'] = df['open_time'].apply(lambda x : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x/1000)))

fig = go.Figure(data=[go.Candlestick(x=df['open_time'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.show()
