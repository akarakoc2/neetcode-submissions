class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        count = {}
        req = {}
        for i in range(len(s1)):
            req[s1[i]] = req.get(s1[i],0) + 1
            
        for i in range(len(s2)):
            if (i-l) < len(s1):
                count[s2[i]] = count.get(s2[i],0) + 1
            else:
                count[s2[i]] = count.get(s2[i],0) + 1
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
            if count == req:
                return True
        
        return False

        

            
        