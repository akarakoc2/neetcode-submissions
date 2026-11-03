class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pref = 1
        suff = 1

        for i in range(len(nums)):
            res[i] = res[i] * pref
            pref = pref * nums[i]

        for j in range(len(nums)-1,-1,-1):
            res[j] = res[j] * suff
            suff = suff * nums[j]
        
        return res