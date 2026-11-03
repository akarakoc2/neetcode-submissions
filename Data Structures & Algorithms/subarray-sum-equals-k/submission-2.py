class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        pref_sum = [0] * (len(nums) + 1)
        prev = 0
        for i in range(len(nums) + 1):
            if i == 0:
                continue
            prev = prev + nums[i-1]
            pref_sum[i] = prev
        

        seen = dict()
        count = 0
        for j in range(len(pref_sum)):
            diff = pref_sum[j] - k
            if diff in seen:
                count += seen[diff]
            seen[pref_sum[j]] = seen.get(pref_sum[j], 0 ) + 1 
        
        return count


        

        