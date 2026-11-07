class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        if len(s) != len(t):
            return False

        charS = collections.defaultdict(list)
        charT = collections.defaultdict(list)

        for i in range(len(s)):
            charS[s[i]].append(i)
            charT[t[i]].append(i)

        return list(charS.values()) == list(charT.values())
                
        