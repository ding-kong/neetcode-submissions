class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPS = set(["+", "-", "*", "/"])
        s = []
        
        for token in tokens:
            if token in OPS:
                operand_2 = s.pop()
                operand_1 = s.pop()
                
                if token == "+":
                    s.append(operand_1 + operand_2)
                elif token == "-":
                    s.append(operand_1 - operand_2)
                elif token == "*":
                    s.append(operand_1 * operand_2)
                elif token == "/":
                    s.append(int(operand_1 / operand_2))
                
                continue

            s.append(int(token))
        
        return s.pop()