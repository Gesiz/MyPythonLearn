def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    iLen = len(prices)
    profit = 0
    for i in range(1, iLen):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))


