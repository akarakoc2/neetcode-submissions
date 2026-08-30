class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = collections.defaultdict(list)

        for i in range(len(strs)):
            s_i = sorted(strs[i])
            s_i = "".join(s_i)
            seen[s_i].append(strs[i])

        return list(seen.values())
           
        