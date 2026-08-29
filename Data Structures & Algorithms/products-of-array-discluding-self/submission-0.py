class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            res[i]  = prefix * res[i]
            prefix = prefix * nums[i]

        for i in range(len(nums)-1, -1,-1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]
        
        return res
        
        
            

        