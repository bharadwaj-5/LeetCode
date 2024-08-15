class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        indices = []
        for i in range(n):
            if number[i] == digit:
                indices.append(i)
        
        op = []

        for i in indices:
            op.append(int((number[:i] + number[i:].replace(number[i], '', 1)))
)
        
        print(op)
        print(indices)
        return str(max(op))