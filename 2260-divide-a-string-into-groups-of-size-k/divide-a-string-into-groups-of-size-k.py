class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        while len(s) % k != 0:
                s += fill
        
        op = []

        for i in range(0, len(s), k):
            op.append(s[i:i+k])

        return op
        