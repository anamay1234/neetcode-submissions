class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if mapping[popped] == char:
                        continue
                    else:
                        return False
                
        return not stack
        