class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = collections.defaultdict(list)

        for i in strs:
            sorted_i = sorted(i)
            seen[''.join(sorted_i)].append(i)

        return list(seen.values())
            
        