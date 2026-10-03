class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []

        mp = defaultdict(list)

        for s in strs:

            arrKey = [0] * 26
            
            for c in s:
                arrKey[ord(c) - ord('a')] += 1

            mp[tuple(arrKey)].append(s)

        return list(mp.values())

            







        