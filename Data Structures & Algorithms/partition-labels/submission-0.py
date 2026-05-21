class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create hashmap 
        # char | lastIndexOfChar

        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = i


        i = 0
        size = 0
        end = 0
        returnList = []

        while i < len(s):
            if hashmap[s[i]] > end:
                end = hashmap[s[i]]
            size += 1

            if i == end:
                returnList.append(size)
                size = 0
            i += 1
        
        #for key, value in hashmap.items():
            #print(f"{key}: {value}")

        return returnList