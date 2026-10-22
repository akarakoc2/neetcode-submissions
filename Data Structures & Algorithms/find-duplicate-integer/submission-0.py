class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = {}
        
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        
        for a,v in seen.items():
            if v > 1:
                return a


        