class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        i = 0
        while i < len(s):
            # print(stack, s[i])
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif len(stack) == 0:
                # print("here 1")
                return False
            else:
                if ((s[i] == ')' and stack[-1] != '(') or
                    (s[i] == '}' and stack[-1] != '{') or
                    (s[i] == ']' and stack[-1] != '[')
                ):
                    # print("here 2")
                    return False
                else:
                    stack.pop()
            # print(stack, s[i])
            i += 1
        
        # print(s)
        return True if len(stack) == 0 else False
        