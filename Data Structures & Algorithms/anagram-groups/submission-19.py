class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = collections.defaultdict(list)
        for i in strs:
            sorted_s = sorted(i)
            seen["".join(sorted_s)].append(i)

        return list(seen.values())

        