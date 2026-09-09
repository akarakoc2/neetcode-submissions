class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        
    def push(self, val: int) -> None:
        if self.prefix:
            self.prefix.append(min(self.prefix[-1], val))
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.prefix.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.prefix.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0
        
        
    def getMin(self) -> int:
        if self.prefix:
            return self.prefix[-1]
        else:
            return 0

          
        
