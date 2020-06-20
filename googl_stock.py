from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt


ts = TimeSeries(key = 'YOUR_API_KEY', output_format = 'pandas')
data, meta_data = ts.get_intraday(symbol = 'GOOGL', interval='1min', outputsize = 'full')
pprint(data.head(4))
data['4. close'].plot()
plt.title('Intraday Times Series for the GOOGL stock (1 min)')
plt.show()

