class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []

        for i in tokens:
            if i == '+':
                s.append(s.pop() + s.pop())
            elif i == '-':
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif i == '*':
                s.append(s.pop() * s.pop())   
            elif i == '/':
                a, b = s.pop(), s.pop()
                result = abs(b) // abs(a)
                if (b < 0) ^ (a < 0): 
                    result = -result
                s.append(result)
            else:
                s.append(int(i))

        return s[0]
        