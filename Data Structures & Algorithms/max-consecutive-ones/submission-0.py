class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0
        ans = 0
        for i in nums:
            if i == 1:
                ans += 1
            else:
                print(i)
                res = max(res, ans)
                ans = 0
            res = max(res,ans)
        return res