class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        for i in tokens:
            if i not in "+-*/":
                operand_stack.append(int(i))
            else:
                right = operand_stack.pop()
                left = operand_stack.pop()

                if i == "+":
                    res = left + right
                elif i == "-":
                    res = left - right
                elif i == "/":
                    res = int(left/right)
                elif i == "*":
                    res = left * right
                operand_stack.append(res)

        return operand_stack[0]
