class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        res = []

        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }


        def dfs(i, string):
            # at base case just append to res
            if i >= len(digits):
                res.append(string)
                return 

            chars = hashmap[digits[i]]
            for char in chars:
                dfs(i+1, string + char)
        
        dfs(0, "")
        return res


        