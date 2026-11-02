class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # there are 3 possbilities 
        # 1 -  itself the target k [0, 2, 1, 2],
        pref_sum = [0] * (len(nums) + 1)
        prev = 0
        for i in range(len(nums) + 1):
            if i == 0:
                continue
            prev = prev + nums[i - 1]
            pref_sum[i] = prev

        seen = {}
        count = 0

        for i in range(len(pref_sum)):
            diff = pref_sum[i] - k
            if diff in seen:
                count += seen[diff]
            seen[pref_sum[i]] = seen.get(pref_sum[i], 0) + 1

        return count
            
        


