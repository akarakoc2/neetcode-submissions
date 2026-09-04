class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # taban = abs(rt - st) 
        # yükseklik = min(heights[rt],heights[st]) 
        # optimize max -> taban * yükseklik

        st= 0 
        rt= len(heights) - 1
        max_arr = 0  
        while st < rt:  
            arr = min(heights[rt],heights[st]) * (rt - st)
            if heights[st] < heights[rt]:
                st +=1

            elif heights[st] > heights[rt]:
                rt -=1

            else:
                st +=1
                rt -=1
            if arr > max_arr:
                max_arr = arr

        return max_arr
            


