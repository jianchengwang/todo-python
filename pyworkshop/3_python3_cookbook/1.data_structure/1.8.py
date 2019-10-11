# 字典的运算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 1.8.1
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

# 1.8.2
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# tips zip() 函数创建的是一个只能访问一次的迭代器