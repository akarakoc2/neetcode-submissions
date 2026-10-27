class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = collections.defaultdict(list)
        for i in strs:
            sortes_s = sorted(i)
            seen["".join(sortes_s)].append(i)


        return list(seen.values())
            
        
        


        