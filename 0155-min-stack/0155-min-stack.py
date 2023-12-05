class MinStack:

    def __init__(self):
        self.array = []
        self.minimums = []
        

    def push(self, val: int) -> None:
        
        self.array.append(val)
        if self.minimums: val = min(val,self.minimums[-1])
        self.minimums.append(val)
        

    def pop(self) -> None:
        
        if self.array:
            self.array.pop()
            self.minimums.pop()
        
        

    def top(self) -> int:
        
        if self.array: return self.array[-1]
        


    def getMin(self) -> int:
        
        return self.minimums[-1]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()