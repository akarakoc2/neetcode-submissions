class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        res = []
        for i in range(len(words)):
            target = words[i]
            print(target)
            j = 0
            while j < len(words):
                if i != j and target in words[j]:
                    res.append(target)
                    break
                else:
                    j += 1
            
        return res


        