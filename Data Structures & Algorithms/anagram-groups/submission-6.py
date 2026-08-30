class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = collections.defaultdict(list)
        res = []
        for i in range(len(strs)):
            s_i = sorted(strs[i])
            s_i = "".join(s_i)
            seen[s_i].append(strs[i])

        for key in seen:
            res.append(seen[key])

        return res
           
        