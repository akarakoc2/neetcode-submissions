class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = dict()
        t_dict = dict()

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        

        return s_dict == t_dict