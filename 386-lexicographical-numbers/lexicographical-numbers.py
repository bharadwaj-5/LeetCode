class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        op = [str(i) for i in range(1, n + 1)]
        op.sort()
        op = [int(i) for i in op]

        return op
        