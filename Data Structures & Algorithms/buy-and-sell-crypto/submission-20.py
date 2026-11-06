class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        ans = 0
        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0:
                ans = max(ans, profit)
                r += 1
            else:
                l = r
                r = r + 1

        return ans 
        