class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        
        def dfs(i, arr):

            if i >= len(s):
                res.append(arr.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    arr.append(s[i:j+1])
                    dfs(j+1, arr)
                    arr.pop()

        dfs(0, [])
        return res

    def isPalindrome(self, string):
        L = 0
        R = len(string) - 1

        while L <= R:
            if string[L] == string[R]:
                L += 1
                R -= 1
                continue
            else:
                return False


        return True

        