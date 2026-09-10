class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        check = collections.defaultdict(list)
        
        for i in strs:
            sorted_i = sorted(i)
            check["".join(sorted_i)].append(i)



        return list(check.values())
        

