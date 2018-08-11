
def maxProfit(prices):
    #依次找到最低谷和其峰值的差值，并与之前的最大差值比较
    if len(prices) < 2:
        return 0
    minPrice = prices[0]
    maxPro = 0
    for price in prices:
        if price < minPrice:
            minPrice = price
        if price - minPrice > maxPro:
            maxPro = price - minPrice
    return maxPro

prices = [7,1,5,3,6,4]
print(maxProfit(prices))