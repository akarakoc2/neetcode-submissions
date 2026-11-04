class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        pref = [0] * (len(nums) + 1)

        prev = 0
        for i in range(len(nums) + 1):
            if i == 0:
                continue
            prev = prev + nums[i-1]
            pref[i] = prev

        seen = {}
        count = 0

        for j in range(len(pref)):
            diff = pref[j] - k

            if diff in seen:
                count += seen[diff]
            
            seen[pref[j]] = seen.get(pref[j], 0 ) + 1 

        return count



        