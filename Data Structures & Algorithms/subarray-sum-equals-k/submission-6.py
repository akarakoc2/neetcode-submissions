class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        count = 0
        prev = 0
        for num in nums:
            prev = prev + num
            diff = prev - k

            if diff in seen:
                count += seen[diff]
            
            seen[prev] = seen.get(prev, 0 ) + 1
        
        return count