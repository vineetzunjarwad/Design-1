import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.stack = []
        

    def push(self, x: int) -> None:
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
        

    def pop(self) -> None:
        if len(self.stack) != 0:
            popped = self.stack[-1]
            self.stack.pop()
            if self.min == popped:
                self.min = self.stack[-1]
                self.stack.pop()
        else:
            print("Empty stack")

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            print("Empty stack")

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(0)
obj.push(4)
obj.push(7)
obj.pop()
obj.push(-1)
obj.push(77)
param_3 = obj.top()
print("Top: {}".format(param_3))
param_4 = obj.getMin()
print("Min: {}".format(param_4))