question="""
在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
"""

print(question)

stocks = {
    'AAPL': 200.88,
    'GOOG': 1186.96,
    'IBM': 96.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 42.09,
    'SYMC': 21.29
}

print("股票代码和价格：", stocks)

new_stocks = {k: v for k, v in stocks.items() if v > 100}

print("股价大于100元的股票：", new_stocks)