import datetime as date
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pyfolio
import warnings
%matplotlib inline

def get_data(index):
    data = pdr.get_data_yahoo(index, start=startdate, end=enddate)
    return data

startdate = date.datetime(2021,3,1)
enddate = date.datetime(2021,3,31)

amzn = get_data('AMZN')
tsla = get_data('TSLA')
spy = get_data('^GSPC')

print(amzn.head())

#divide el cierra con la primera entrada del cierre (primera fecha)
for stock in (amzn, tsla, spy):
    stock['Returns'] = stock['Adj Close'] / stock['Adj Close'].iloc[0]

print(amzn.head())
print(tsla.head())
print(spy.head())

#distribucion de la inversion (2%, 4%, 4%) total 100%
for stock, allocation in zip((amzn, tsla, spy), [.2, .4, .4]):
    stock['Allocation'] = stock['Returns'] * allocation

print(amzn.head())
print(tsla.head())
print(spy.head())

#posicion de cada inversion x 1000
for stock in (amzn, tsla, spy):
    stock['Position'] = stock['Allocation'] * 1000

print(amzn.head())
print(tsla.head())
print(spy.head())

#creacion de portafolio
portafolio = pd.concat([amzn['Position'], tsla['Position'], spy['Position']], axis=1)
portafolio.columns = ['AMZN', 'TSLA', 'SPY']
print(portafolio.head())

#ploteamos portafolio
portafolio_total = portafolio.sum(axis=1)
print(portafolio_total.head())
#portafolio_total.plot()
#portafolio.plot()
#plt.show()

#retornos diarios
portafolio_returns = portafolio_total.pct_change().dropna()
print(portafolio_returns.head())

benchmark = spy['Adj Close']
bench = benchmark.pct_change().dropna()
bench.rename('Benchmark SP500')

warnings.filterwarnings('ignore')
pyfolio.create_returns_tear_sheet(portafolio_returns)