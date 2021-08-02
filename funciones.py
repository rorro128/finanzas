from binance.client import Client
import keys
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime

client = Client(keys.Pkey, keys.Skey)
listado = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE, limit=30)

listado_data_frame = pd.DataFrame(listado)
listado_data_frame_fecha = listado_data_frame[0]

fecha_final = []

for time in listado_data_frame_fecha.unique():
    readable = datetime.datetime.fromtimestamp(int(time/1000))
    fecha_final.append(readable)

listado_data_frame.pop(0)
listado_data_frame.pop(11)

dataframe_fecha_final = df(fecha_final)
dataframe_fecha_final.columns = ['date']

final_dataframe = listado_data_frame.join(dataframe_fecha_final)
final_dataframe.set_index('date', inplace=True)

final_dataframe.columns = ['open','high','low','close','volume','close_time','asser_volume','trade_number','taker_buy_base','taker_buy_quote']
final_dataframe = final_dataframe.drop(columns=['close_time', 'taker_buy_base', 'taker_buy_quote'])

#transformamos a numero los datos necesarios
final_dataframe[["open", "high", "low", "close", "volume"]] = final_dataframe[["open", "high", "low", "close", "volume"]].apply(pd.to_numeric)

print(final_dataframe)
mpf.plot(final_dataframe, type = 'candle', volume = True)


