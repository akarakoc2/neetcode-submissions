class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in range(len(strs)):
            cur_len = str(len(strs[i]))
            encode = encode + cur_len + "#" + strs[i]
        return encode




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




