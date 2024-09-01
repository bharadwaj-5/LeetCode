class Solution:
    def construct2DArray(self, arr: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(arr):
            return []
        
        o = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                o[i][j] = arr[idx]
        
        return o
