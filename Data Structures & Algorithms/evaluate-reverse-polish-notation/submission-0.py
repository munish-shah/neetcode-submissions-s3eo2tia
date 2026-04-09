class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x not in ['+', '-', '/', '*']:
                stack.append(int(x))
            else:

                if x == '+':
                    stack.append(stack.pop() + stack.pop())
                elif x == '/':
                    n1, n2 = stack.pop(), stack.pop()

                    stack.append(int(n2 / n1))
                elif x == '-':
                    n1, n2 = stack.pop(), stack.pop()
                    stack.append(n2 - n1)
                elif x == '*':
                    stack.append(stack.pop() * stack.pop())
        return stack[-1]

        