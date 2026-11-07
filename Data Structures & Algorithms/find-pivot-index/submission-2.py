class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0] * (len(nums))
        prev = 0
        for i in range(len(nums)):
            pref[i] = prev
            prev = prev + nums[i]
        
        suffix = [0] * (len(nums))
        suff = 0 
        for j in range(len(nums)-1,-1,-1):
            suffix[j] = suff
            suff = suff + nums[j]
        # total - li - nums
        for i in range(len(nums)):
            if suffix[i] == pref[i]:
                return i
        
        return -1
