class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # mono increasing needed
        stack = []
        maxRes = 0 
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                if not stack:
                    area = heights[popped_index] * i
                else:    
                    area = heights[popped_index] * (i - stack[-1] - 1)
                maxRes = max(maxRes, area)
            stack.append(i)

        # i = 1 stack = [1,3,4,5] area = pop(7) * 
        qty = len(heights)
        while stack:
            pop_idx = stack.pop()
            if not stack:
                width = qty
            else:
                width = qty - stack[-1] - 1
            
            area = heights[pop_idx] * width
            maxRes = max(maxRes, area)

        return maxRes
