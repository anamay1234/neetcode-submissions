class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""
        for string in strs:
            s += str(len(string))
            s += "#"
            s += string

        print(s)
        return s

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        #   j            j
        # i   e       i
        # 3 # r a t  1 1 # c a t t e r p i l e r
        # 0 1 2 3 4  5 6 7 8 9 

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1 : j + 1 + length])
            i = j + 1 + length

        return res
