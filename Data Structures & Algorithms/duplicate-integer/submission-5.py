class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in range(len(nums)):
            print(i)
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = 1
        return False
            
            

        