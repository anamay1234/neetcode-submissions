class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        
        for s in strs:
            encodedStr += str(len(s))
            encodedStr += "#"
            encodedStr += s

        return encodedStr


    def decode(self, s: str) -> List[str]:
        stringList = []
        i = 0 
        while i < len(s):
            lengthOfString = ""
            while ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9"):
                lengthOfString += s[i]
                i += 1

            i += 1 

            lengthOfString = int(lengthOfString)
            string = ""
            for j in range(lengthOfString):
                string += s[i]
                i += 1
            
            stringList.append(string)

    
        return stringList


            

