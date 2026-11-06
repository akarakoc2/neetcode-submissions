class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        res = 0
        # 1 2 1 4 
        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit >= 0:
                res = max(res, profit)
                r += 1
            else:
                l = r
                r = l + 1

            
        
        return res