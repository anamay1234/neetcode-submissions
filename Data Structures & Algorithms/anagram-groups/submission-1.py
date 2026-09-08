class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for string in strs:
            
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] += 1


            newKey = tuple(key)
            hashmap[newKey].append(string)


        return list(hashmap.values())

        