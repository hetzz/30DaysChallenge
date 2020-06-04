def maxProfit(prices):
    curr = 0
    profit = 0
    temp = []
    for i in range(len(prices) - 1):
        temp.append(prices[i+1] - prices[i])
    for x in temp:
        if x > 0:
            curr += x
        else:
            profit += curr
            curr = 0
    profit += curr
        
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))