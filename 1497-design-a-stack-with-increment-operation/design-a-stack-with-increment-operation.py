class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = [0] * maxSize  
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1  
        
        index = len(self.stack) - 1
        result = self.stack.pop() + self.inc[index] 
        
        if index > 0:
            self.inc[index - 1] += self.inc[index]
        
        self.inc[index] = 0
        
        return result

    def increment(self, k: int, val: int) -> None:
        
        limit = min(k, len(self.stack))
        if limit > 0:
            self.inc[limit - 1] += val  


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)