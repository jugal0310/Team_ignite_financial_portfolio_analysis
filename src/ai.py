import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import yfinance as yf

# Define the start and end dates
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.today()

# Fetch stock data using yfinance
aapl = yf.download('AAPL', start=start, end=end)[['Adj Close']].copy()
ibm = yf.download('IBM', start=start, end=end)[['Adj Close']].copy()
amzn = yf.download('AMZN', start=start, end=end)[['Adj Close']].copy()

# Normalize returns
for stock_df in (aapl, ibm, amzn):
    stock_df['Normed Return'] = stock_df['Adj Close'] / stock_df.iloc[0]['Adj Close']

# Calculate allocations and position values
allocations = [0.2, 0.3, 0.5]
for stock_df, allocation in zip((aapl, ibm, amzn), allocations):
    stock_df['Allocation'] = stock_df['Normed Return'] * allocation
    stock_df['Position Amount'] = stock_df['Allocation'] * 500000

# Calculate total portfolio value
total_pos_vals = [aapl['Position Amount'], ibm['Position Amount'], amzn['Position Amount']]
portf_vals = pd.concat(total_pos_vals, axis=1)
portf_vals.columns = ['Apple Pos', 'IBM Pos', 'Amazon Pos']
portf_vals['Total Pos'] = portf_vals.sum(axis=1)

# Plot total portfolio value
portf_vals['Total Pos'].plot(figsize=(10, 6), title='Total Portfolio Value')
plt.show()

# Plot individual stock allocations after 2019
portf_vals['2019-01-01':].drop('Total Pos', axis=1).plot(figsize=(10, 6), title='Stock Allocations After 2019')
plt.show()

# Calculate daily returns
portf_vals['Daily Return'] = portf_vals['Total Pos'].pct_change()
portf_vals.dropna(inplace=True)

# Portfolio statistics
print('Daily Return Average: ', portf_vals['Daily Return'].mean())
print('Daily Return Standard Deviation: ', portf_vals['Daily Return'].std())

# Plot histogram and KDE of daily returns
portf_vals['Daily Return'].plot(kind='hist', bins=100, figsize=(6, 8), color='green', title='Daily Returns Histogram')
plt.show()

portf_vals['Daily Return'].plot(kind='kde', figsize=(8, 6), color='blue', title='Daily Returns KDE')
plt.show()

# Calculate cumulative return
cumulative_return = 100 * (portf_vals['Total Pos'].iloc[-1] / portf_vals['Total Pos'].iloc[0] - 1)
print('Cumulative Return: ', cumulative_return)

# Sharpe Ratio
SR = portf_vals['Daily Return'].mean() / portf_vals['Daily Return'].std()
ASR = (252 ** 0.5) * SR
print('Annualized Sharpe Ratio: ', ASR)

# Log returns for optimization
stocks = pd.concat([aapl['Adj Close'], ibm['Adj Close'], amzn['Adj Close']], axis=1)
stocks.columns = ['Apple', 'IBM', 'Amazon']
log_returns = np.log(stocks / stocks.shift(1)).dropna()

# Monte Carlo simulation for portfolio optimization
num_ports = 5000
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for ind in range(num_ports):
    weights = np.random.random(3)
    weights /= np.sum(weights)
    all_weights[ind, :] = weights

    # Expected return
    ret_arr[ind] = np.sum(log_returns.mean() * weights * 252)

    # Expected volatility
    vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights)))

    # Sharpe ratio
    sharpe_arr[ind] = ret_arr[ind] / vol_arr[ind]

# Optimal portfolio
max_sr_idx = sharpe_arr.argmax()
optimal_weights = all_weights[max_sr_idx, :]
print('Optimal Weights: ', optimal_weights)

# Plot efficient frontier
plt.figure(figsize=(12, 8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='Spectral', edgecolors='black')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Efficient Frontier')

# Highlight maximum Sharpe ratio portfolio
plt.scatter(vol_arr[max_sr_idx], ret_arr[max_sr_idx], c='red', s=50, edgecolors='black', label='Max Sharpe Ratio')
plt.legend()
plt.show()
