class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # length of string + # + string
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # array of string, pointer

        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # has to be from i to j in case the length is more than 2 bits
            res.append(s[j + 1 : j + length + 1])
            i = j + 1 + length
        return res