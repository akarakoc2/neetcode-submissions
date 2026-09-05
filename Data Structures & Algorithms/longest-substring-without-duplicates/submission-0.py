class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r = 0,0
        window = set()
        max_len = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            r += 1

            subLen = r - l
            max_len = max(subLen, max_len)

        return max_len




        

            
        
