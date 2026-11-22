class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = collections.defaultdict(list)

        for i in range(len(strs)):
            freq[''.join(sorted(strs[i]))].append(strs[i])

        vals = list(freq.values())

        return vals

        