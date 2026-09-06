class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = collections.defaultdict()
        l=0
        res = 0
        for i in range(len(s)):
            #frequency
            if s[i] not in count:
                count[s[i]] = 1 
            else:
                count[s[i]] += 1 

            #len(window) - most frequent < k
            freq = count.values()
            
            check = sum(freq) - max(freq) 
            if check <= k:
                res = max(res, sum(freq))
                continue
            else:
                count[s[l]] -= 1 
                l+=1 

        return res
        


            
           


        

        