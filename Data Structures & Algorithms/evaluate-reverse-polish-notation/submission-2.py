class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*', '/'])
        stack = []
        val = 0
        for x in tokens:
            if x not in operations:
                stack.append(int(x))
            elif x=='+':
                stack.append(stack.pop() + stack.pop())
            elif x=='-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif x=='*':
                stack.append(stack.pop() * stack.pop())
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
        return stack[0]