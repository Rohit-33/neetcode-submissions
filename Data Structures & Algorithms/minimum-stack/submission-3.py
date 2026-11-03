class MinStack:

    def __init__(self):
        self.ar = []
        self.ar1 = []

    def push(self, val: int) -> None:

        self.ar.append(val)
        self.ar1.append(val)
        self.ar1.sort()

        

    def pop(self) -> None:

        val = self.ar[-1]
        self.ar.pop()
        self.ar1.remove(val)
        self.ar1.sort()
        

    def top(self) -> int:

        return self.ar[-1]
        

    def getMin(self) -> int:
        return self.ar1[0]
        
