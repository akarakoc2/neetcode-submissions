class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we need to pick a center and 
        # this center would work well if c+1 and c-1 is same and goes o
        word =""
        for i in s:
            if i.isalnum():
                word += i.lower()
        index_total = len(word)-1

        i=0
        while i < ((len(word)-1) / 2):
            left = word[i]
            right = word[index_total - i]
            if left != right:
                return False
            i +=1

        return True




