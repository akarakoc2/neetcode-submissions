class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pref = [0] * (len(nums) + 1)
        prev = 0

        for i in range(1, len(nums) + 1):
            prev += nums[i-1]
            pref[i] = prev

        seen = {}
        count = 0
        
        for j in range(len(pref)):
            target = pref[j] - k

            if target in seen:
                count += seen[target]

            seen[pref[j]] = seen.get(pref[j], 0) + 1
        print(seen)
        return count
        