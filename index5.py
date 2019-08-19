from nsepy import get_history
import pandas as pd 
from datetime import date 
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from sklearn.metrics import mean_squared_error

matplotlib.style.use('seaborn')

start = date(2015, 1, 1)
end = date.today()


df = get_history("NIFTY 50", start=start, end=end, index=True)
df['daily_ret'] = df['Close'].pct_change()
# df['daily_ret'] = np.log(df['daily_ret'])
df['target'] = df['daily_ret'].shift(-1)
series = df['target'].dropna() 



































# # plot returns
# # df['target'].plot()
# # plot_pacf(series)
# # plt.show()

# # fit model
# # model = ARIMA(series, order=(5,1,0))
# # model_fit = model.fit(disp=0)
# # print(model_fit.summary())

# # # plot residual errors
# # residuals = pd.DataFrame(model_fit.resid)
# # residuals.plot()
# # plt.show()
# # residuals.plot(kind='kde')
# # plt.show()
# # print(residuals.describe())

# X = series.values
# size = int(len(X) * 0.99)
# train, test = X[0:size], X[size:len(X)]
# history = [x for x in train]
# predictions = list()
# for t in range(len(test)):
# 	model = ARIMA(history, order=(5,1,0))
# 	model_fit = model.fit(disp=0)
# 	output = model_fit.forecast()
# 	yhat = output[0]
# 	predictions.append(yhat)
# 	obs = test[t]
# 	history.append(obs)
# 	print('predicted=%f, expected=%f' % (yhat, obs))
# error = mean_squared_error(test, predictions)
# print('Test MSE: %.3f' % error)
# # plot
# plt.plot(test)
# plt.plot(predictions, color='red')
# plt.show()
