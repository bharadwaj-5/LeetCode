class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = "".join(str(ord(i) - ord('a') + 1) for i in s)
        
        total = sum(int(i) for i in total)
        
        for _ in range(k - 1):
            total = sum(int(i) for i in str(total))
        
        return total
