class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            cur_len = str(len(i))
            encoded = encoded + cur_len + "#" + i
            
        return encoded
        # 5#Hello#
    def decode(self, s: str) -> List[str]:
        dcd_list = list()
        i=0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            dcd_list.append(s[j+1:j+length+1])
            i = j + 1 + length


        return dcd_list



        
        
