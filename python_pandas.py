import pandas as pd
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2017,1,1)
end = datetime.datetime.now()
df = web.DataReader("XOM", "morningstar", start, end)
print(df)
