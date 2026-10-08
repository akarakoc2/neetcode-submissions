class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ''

        for i in s:
            if i.isalnum():
                i=i.lower()
                word = word+i

        index_total = len(word) - 1
        i = 0
        while i < (len(word)-1) / 2:
            left = word[i]
            right = word[index_total]
            if left != right:
                return False
            i += 1
            index_total -= 1
        return True
        
        

        