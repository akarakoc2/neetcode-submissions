class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = dict()
        for i in strs:
            key = "".join(sorted(i))


            if key not in groups:
                groups[key] = [i]
            else:
                groups[key].append(i)
        
        anagram = list()
        for key,value in groups.items():
            anagram.append(value)

        return anagram


        



        