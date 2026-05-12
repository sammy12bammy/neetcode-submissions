class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = ['+', '-', "*", "/"]

        for i in range(len(tokens)):
            cur = tokens[i]
            # if its a number add to stack.
            # if its a op, pop stack, do op and then add to stack
            if cur not in ops:
                s.append(int(cur))
            else:
                if cur == '+':
                    # pop last 2
                    m = s.pop()
                    n = s.pop()
                    s.append(m+n)
                elif cur == '-':
                    m = s.pop()
                    n = s.pop()
                    s.append(n-m)
                elif cur == '*':
                    m = s.pop()
                    n = s.pop()
                    s.append(m*n)
                else:
                    # divide
                    m = s.pop()
                    n = s.pop()
                    s.append(int(n / m))
        return s[0]


