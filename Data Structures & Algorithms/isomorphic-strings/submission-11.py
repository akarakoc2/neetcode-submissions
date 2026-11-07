class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False

        charS = collections.defaultdict(list)
        charT = collections.defaultdict(list)

        for i in range(len(s)):
            charS[s[i]].append(i)
            charT[t[i]].append(i)

        
        valueT= list(charT.values())
        valueS = list(charS.values())


        return valueT == valueS
            
        
        
