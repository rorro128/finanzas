import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import mplfinance as mpf

start = dt.datetime(2021,4,1)
end = dt.datetime(2021,4,18)

ntdo = web.DataReader('BTC-USD', 'yahoo', start, end)
print(ntdo["High"].max())


mpf.plot(ntdo, type = 'candle', volume = True)

