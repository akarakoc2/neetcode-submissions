class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minLeft = prices[0]
        max_profit = [0]
        for i in range(len(prices)):
            if i==0:
                continue
            sell = prices[i]

            profit = sell - minLeft
            if profit > 0:
                max_profit.append(profit)
            else:
                max_profit.append(0)
            if prices[i] < minLeft:
                minLeft = prices[i]
            
        return max(max_profit)
