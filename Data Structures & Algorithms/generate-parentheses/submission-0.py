class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []


        def dfs(openCount, closeCount, string):
            if openCount == n and closeCount == n:
                res.append(string)
                return
            
            if openCount == closeCount:
                string += "("
                dfs(openCount + 1, closeCount, string)
            elif openCount > closeCount:
                if openCount < n:
                    string += "("
                    dfs(openCount + 1, closeCount, string)
                    string = string[:-1]
                
                string += ")"
                dfs(openCount, closeCount + 1, string)





            
        dfs(0, 0, "")
        return res 
        