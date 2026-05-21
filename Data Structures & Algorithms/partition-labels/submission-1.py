class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create hashmap 
        # char | lastIndexOfChar

        lastIndex = {} # char - last index

        for i in range(len(s)):
            lastIndex[s[i]] = i

        i = 0
        size = 0
        end = 0
        returnList = []

        while i < len(s):
            if lastIndex[s[i]] > end:
                end = lastIndex[s[i]]
            size += 1

            if i == end:
                returnList.append(size)
                size = 0
            i += 1
        
        #for key, value in hashmap.items():
            #print(f"{key}: {value}")

        return returnList