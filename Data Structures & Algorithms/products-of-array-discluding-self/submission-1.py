class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pref = 1 
        suff = 1

        for i in range(len(nums)):
            res[i] = pref * res[i]
            pref = nums[i] * pref

        for i in range(len(nums)-1,-1,-1):
            res[i] = suff * res[i]
            suff = nums[i] * suff


        return res