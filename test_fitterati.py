import fitterati
import pandas as pd 
from nsepy import get_history
import datetime

start = datetime.date(2010,1,1)
end = datetime.date.today()
df = get_history("NIFTY BANK", start=start, end=end, index=True)
df['daily_returns'] = df['Close'].pct_change()*100
df = df.dropna()

fitterati = fitterati.Distribution()

fitterati.Fit(df['daily_returns'])
fitterati.Plot(df['daily_returns'])