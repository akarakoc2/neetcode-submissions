class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prev_sum = [0] * (len(nums) + 1)
        prev = 0
        for i in range(len(nums)+ 1):
            if i == 0:
                continue
            prev = prev + nums[i-1]
            prev_sum[i] = prev

        
        seen = {}
        count = 0

        for j in range(len(prev_sum)):
            diff = prev_sum[j] - k 
            if diff in seen:
                count += seen[diff]
            seen[prev_sum[j]] = seen.get(prev_sum[j], 0) + 1

        return count

        
            