class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            
            look = target - nums[i]
            
            if look in seen:
                return [seen[look], i]

            seen[nums[i]] = i
        