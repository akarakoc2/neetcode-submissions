class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = [0]
        running = 0

        for x in nums:
            running += x
            pref.append(running)

        seen = {}
        count = 0

        for p in pref:
            count += seen.get(p - k, 0)
            seen[p] = seen.get(p, 0) + 1

        return count


        