class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                result = float(firstOperand) + float(secondOperand)
                stack.append(int(result))
            elif token == '-':
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                result = float(firstOperand) - float(secondOperand)
                stack.append(int(result))
            elif token == '*':
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                result = float(firstOperand) * float(secondOperand)
                stack.append(int(result))
            elif token == '/':
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                result = float(firstOperand) / float(secondOperand)
                stack.append(int(result))
            else:
                stack.append(int(token))
        
        return stack.pop()