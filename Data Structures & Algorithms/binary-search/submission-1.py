class Solution:
    def search(self, nums: List[int], target: int) -> int:
        check = {}
        for i in range(len(nums)):
                check[nums[i]] = i
        if target in check:
            return check[target]
        else:
            return -1