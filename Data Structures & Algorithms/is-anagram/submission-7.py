class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dct = {}
        t_dct = {}

        for i in range(len(s)):
            s_dct[s[i]]= s_dct.get(s[i], 0) + 1

        
        for j in range(len(t)):
            t_dct[t[j]]= t_dct.get(t[j], 0) + 1


        return True if s_dct == t_dct else False