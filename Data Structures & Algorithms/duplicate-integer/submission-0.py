class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s_nums = set(nums)

        if len(nums) > len(s_nums):
            return True
        else:
            return False
        