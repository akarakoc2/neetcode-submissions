class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current = 0
        best = 0

        for x in nums:
            if x == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best

                


            

        