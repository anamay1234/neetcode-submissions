class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returningList = []

        hashmap = {}

        for string in strs:
            arrayOfChars = [0] * 26
            for char in string:
                arrayOfChars[ord(char) - ord('a')] += 1
            
            if tuple(arrayOfChars) in hashmap:
                hashmap[tuple(arrayOfChars)].append(string)
            else:
                hashmap[tuple(arrayOfChars)] = hashmap.get(tuple(arrayOfChars), [string])
            
        
        for key in hashmap:
            returningList.append(hashmap[key])
        
        return returningList

            

                
            

        