class Solution:
    def countBits(self, n: int) -> List[int]:
        o = []

        for i in range(0, n+1):
            a = bin(i)
            a = str(a)
            o.append(a.count('1'))

        return o
        