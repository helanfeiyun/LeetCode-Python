
def maxProfit(prices):
    #只要比前一天价格高，就有收入。其他情况不考虑
    if len(prices) < 2:
        return 0
    sumPro = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            sumPro += prices[i] - prices[i - 1]
    return sumPro

prices = [7,1,5,3,6,4]
print(maxProfit(prices))