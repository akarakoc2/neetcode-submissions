class Solution:
    def firstUniqChar(self, s: str) -> int:

        seen = collections.defaultdict(list)

        for i in range(len(s)):
            seen[s[i]].append(i)

        ans = float('inf')
        for j in list(seen.values()):
            if len(j) == 1:
                ans = min(ans,j[0])

        return ans if ans < float('inf') else -1
        
        