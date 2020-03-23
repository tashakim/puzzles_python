from alpha_vantage.timeseries import TimeSeries

key = 'INCDSOCLUB4EREN7'
ts = TimeSeries(key)
aapl, meta = ts.get_daily(symbol = 'AAPL')
print(aapl['2019-09-12'])

