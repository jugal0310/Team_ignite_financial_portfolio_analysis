# project name

Financial Portfolio Analysis

# Team Members:
Jugal Prajapati (ku2407u095)

Krish Bhatt (ku2407u113)

Ved Patel (ku2407u446)

Ved Prajapati (ku2407u233)

 # Overwiew
 
The goal of this project is to:

Optimize a stock portfolio consisting of AAPL, IBM, and AMZN using historical stock price data.
Calculate portfolio performance metrics such as expected returns, volatility, and the Sharpe ratio.
Identify the portfolio allocation that maximizes the Sharpe ratio using Python.

## TOOLS USED:
Programming Language: Python
Libraries:

numpy: For mathematical calculations.

pandas: For data manipulation and analysis.

matplotlib: For visualizing portfolio performance.

seaborn: For enhanced data visualization.

yfinance: To fetch historical stock price data.

statsmodels: For statistical computations.


## Requirements
Python 3.x
### Required Python libraries:
pandas
matplotlib
seaborn
tkinter (for file selection dialog)
json
os 

## Data Source(s)

Historical stock price data was obtained from:

Yahoo Finance
The data includes:

Adjusted closing prices for Apple (AAPL), IBM, and Amazon (AMZN).
Time period: From 2015-01-01 to the present.


## Execution Steps
To run the project, follow these steps:

Install Required Libraries: Run the following command to install the required Python libraries:

bash
Copy code
pip install numpy pandas matplotlib seaborn statsmodels yfinance
Clone the Repository: Clone the GitHub repository:

bash
Copy code
git clone https://github.com/[Your-GitHub-Username]/[Repository-Name].git
cd [Repository-Name]
Fetch Data:

Ensure the Python script includes the code to fetch data using yfinance.
Alternatively, place the pre-downloaded CSV files (AAPL_historical_data.csv, IBM_historical_data.csv, AMZN_historical_data.csv) in the project folder.
Run the Python Script: Execute the script to perform portfolio optimization:

bash
Copy code
python portfolio_optimization.py
View Outputs:

The program generates visualizations of portfolio allocations, volatility vs. return, and daily returns.
Key metrics like cumulative returns, Sharpe ratio, and the optimal weights will be printed.


### Summary of Results

Optimal Portfolio Weights: Example output: [AAPL: 0.4, IBM: 0.2, AMZN: 0.4].
Expected Annual Return: 15.2%
Portfolio Volatility: 10.8%
Sharpe Ratio: 1.41
Maximum Sharpe Ratio Portfolio was visualized with a red dot on the risk-return plot.


## Challenges Faced

Data Fetching Issues:

Encountered API deprecations while using pandas_datareader.
Resolved by switching to yfinance.
Data Preprocessing:

Ensuring clean, consistent data format (adjusting for missing values or incorrect timestamps).
Computational Challenges:

Running Monte Carlo simulations for 5000+ portfolios was computationally intensive.
Optimized by reducing unnecessary iterations.
Sharpe Ratio Maximization:

Ensuring the results matched theoretical expectations required several tests and adjustments.

## Author
Developed by Team IGNITE.
Thank You.
