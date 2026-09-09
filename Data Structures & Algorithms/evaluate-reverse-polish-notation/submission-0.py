class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda b, a: b + a,
            '-': lambda b, a: b - a,
            '*': lambda b, a: b * a,
            '/': lambda b, a: int(b / a)
        }

        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[i](b,a))
                
        return stack[-1]