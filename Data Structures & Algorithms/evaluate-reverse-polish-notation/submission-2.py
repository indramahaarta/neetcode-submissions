class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = -1
        for i in range(0, len(tokens)):
            print(stack)
            if (tokens[i] != "+" and 
                tokens[i] != "-" and 
                tokens[i] != "*" and 
                tokens[i] != "/"
            ):
                stack.append(int(tokens[i]))
            else:
                y = stack.pop()
                x = stack.pop()
                if tokens[i] == '+':
                    stack.append(x + y)
                elif tokens[i] == '-':
                    stack.append(x - y)
                elif tokens[i] == '*':
                    stack.append(x * y)
                else:
                    stack.append(int(x / y))
        
        return stack[-1]