class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            preMin = self.stack[-1][1]
            if val < preMin:
                self.stack.append([val, val])
            else:
                self.stack.append([val, preMin])


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        
