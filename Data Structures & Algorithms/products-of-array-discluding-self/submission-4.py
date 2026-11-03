class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prev = 1
        suff = 1
        for i in range(len(nums)):
            res[i] = prev * res[i]
            prev = prev * nums[i]

        for j in range(len(nums)-1,-1,-1):
            res[j] *= suff
            suff *= nums[j]
        
        return res