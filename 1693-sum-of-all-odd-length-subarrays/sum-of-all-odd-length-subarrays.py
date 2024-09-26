class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)
        for i in range(1, n+1):
            for j in range(i):
                if len(arr[j:i]) % 2 != 0:
                    s += sum(arr[j:i])
        return s
        