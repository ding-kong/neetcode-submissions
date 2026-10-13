# OPTIMIZED

class MinStack:
    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        
        if len(self.min_s) <= 0:
            self.min_s.append(val)
            return
        
        if val <= self.getMin():
            self.min_s.append(val)

    def pop(self) -> None:
        _top = self.s.pop()
        _min = self.getMin()

        if _top <= _min:
            self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]


# RAW

# class MinStack:
#     def __init__(self):
#         self.s = []
#         self.min_s = []

#     def push(self, val: int) -> None:
#         self.s.append(val)
        
#         if len(self.min_s) <= 0:
#             self.min_s.append(val)
#             return
        
#         if val <= self.getMin():
#             self.min_s.append(val)
#             return
        
#         self.min_s.append(self.getMin())

#     def pop(self) -> None:
#         self.s.pop()
#         self.min_s.pop()

#     def top(self) -> int:
#         return self.s[-1]

#     def getMin(self) -> int:
#         return self.min_s[-1]
