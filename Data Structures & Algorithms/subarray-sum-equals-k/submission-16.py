class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prev = [0]

        for i in range(len(nums)):
            prev.append(nums[i]+prev[-1])


        seen = {}
        count = 0
        for i in range(len(prev)):
            target = prev[i] - k
            if target in seen:
                count += seen[target]
            seen[prev[i]] = seen.get(prev[i], 0) + 1
        
        return count
            
        
        
            

        