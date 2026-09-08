class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for string in strs:
            
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] += 1


            newKey = tuple(key)
            if newKey not in hashmap:
                hashmap[newKey] = []
                hashmap[newKey].append(string)
            else:
                hashmap[newKey].append(string)


        return list(hashmap.values())

        