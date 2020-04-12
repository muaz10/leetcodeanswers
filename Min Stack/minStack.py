class MinStack:
    def __init__(self):
        super().__init__()
        self.stk = []
        self.pointer = -1
        self.min = float('inf')

    def push(self, x: int) -> None:
        if self.pointer < 0:
            self.min = x
        elif x < self.min:
            self.min = x

        self.pointer += 1
        self.stk.insert(self.pointer, x)

    def pop(self) -> None:
        if self.pointer == 0:
            self.min = None
        elif self.stk[self.pointer] == self.min:
            tempmin = self.stk[self.pointer-1]
            for i in range(self.pointer-1):
                if self.stk[i] < tempmin:
                    tempmin = self.stk[i]
            self.min = tempmin
        self.pointer -= 1

    def top(self) -> int:
        print(self.pointer)
        if self.pointer < 0:
            return None
        else:
            return self.stk[self.pointer]

    def getMin(self) -> int:
        return self.min


st1 = MinStack()
st1.push(2147483646)
st1.push(2147483646)
st1.push(2147483647)
print(st1.top())
st1.pop()
print(st1.getMin())
st1.pop()
print(st1.getMin())
st1.pop()
st1.push(2147483647)
print(st1.top())
print(st1.getMin())
st1.push(-2147483648)
print(st1.top())
print(st1.getMin())
st1.pop()
print(st1.getMin())

# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
