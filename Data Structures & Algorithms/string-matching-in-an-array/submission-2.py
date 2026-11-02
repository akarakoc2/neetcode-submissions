class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        for i in range(len(words)):
            target = words[i]
            j = 0
        
            while j < len(words): 
                
                # 3. Only check if we are NOT looking at the exact same index
                if i != j and target in words[j]:
                    res.append(target)
                    break # Stop looking for this target once found to avoid duplicates
                
                j += 1
                
        return res


        