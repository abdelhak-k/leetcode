class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            try:
                num= int(token)
                # we push it to the stack if it's a number
                stack.append(num)
                
            except ValueError:
                # else if it's not a number, we perform the operation 
                # on the last two numbers on the stack
                
                # we get the last two numbers
                num2= stack[-1]
                stack.pop()
                num1= stack[-1]
                stack.pop()
                
                # and we perform the operation and push them again to the stack
                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num1-num2)
                elif token == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1 / num2))
        
            print(stack[-1])
        return stack[-1]