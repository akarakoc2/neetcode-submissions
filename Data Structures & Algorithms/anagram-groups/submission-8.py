class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        check = collections.defaultdict(list)
        res = []
        for i in strs:
            sorted_i = sorted(i)
            check["".join(sorted_i)].append(i)
    

        for i in check:
            res.append(check[i])


        return res
        

