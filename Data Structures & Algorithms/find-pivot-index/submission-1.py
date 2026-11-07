class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prev = 0
        total = sum(nums)
        for i in range(len(nums)):
            if prev == (total - nums[i] - prev):
                return i
            prev = prev + nums[i]
        
        return -1
