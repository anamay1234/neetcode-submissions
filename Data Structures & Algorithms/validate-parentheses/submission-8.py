class Solution:
    def isValid(self, s: str) -> bool:

        para = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        stack = []

        for c in s:
            if c in para:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    openingPara = stack.pop()
                    if para[openingPara] == c:
                        continue
                    else:
                        return False



        return True if len(stack) == 0 else False


        