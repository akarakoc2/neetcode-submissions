class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0

        #area min(l, r) * (r - l)

        while l < r:
            water = min(heights[l], heights[r]) * (r - l) # thats the water stored 
            res = max(res, water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res


