class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        #5#word
        for i in strs:
            res += str(len(i)) + "#" + i
        return res


    def decode(self, s: str) -> List[str]:
        dcd = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1

            lenght = int(s[i:j])
            dcd.append(s[j + 1: j + lenght + 1])
            i = j + lenght + 1

        return dcd 
                
        
            
            


        
