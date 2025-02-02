import datetime
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime.now()
# df = web.DataReader('TSLA','yahoo',start,end)
# # df.reset_index(inplace=True)
# # df.set_index("Date", inplace=True)
# # df = df.drop("Symbol", axis=1)
# df.to_csv('tsla.csv')




df=pd.read_csv('tsla.csv',parse_dates=True,index_col=0)

# df['100ma']= df['Adj Close'].rolling(window=100,min_periods=0).mean()

df_ohlc= df['Adj Close'].resample('10D').ohlc()

df_volume=df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)

# print(df_ohlc.head())

ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()

# ax1.plot(df.index,df['Adj Close'])
# ax1.plot(df.index,df['100ma'])
# ax2.bar(df.index,df['Volume'])
#
# print(df.head())
# print(df.tail(6))
# df['Adj Close'].plot()
# plt.show()