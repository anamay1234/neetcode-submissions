class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False 
        hashmap = { '(': ')', 
                    '{': '}',
                    '[': ']'}

        stack = []

        for paranthesis in s:
            if paranthesis in hashmap:
                stack.append(hashmap[paranthesis])
                continue
            else:
                if len(stack) == 0:
                    return False

                correctClosingParanthesis = stack.pop()
                if correctClosingParanthesis == paranthesis:
                    continue
                else:
                    return False

        if len(stack) == 0:
             return True 
        else:
            return False
        
        