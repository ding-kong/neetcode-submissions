class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        OPS = set(["+", "C", "D"])
        for op in operations:
            if op not in OPS:
                stack.append(int(op))
                continue
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
        return sum(stack)