class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        mod = k % total

        n = len(chalk)

        for i in range(n):
            if chalk[i] > mod:
                return i
            mod -= chalk[i]
        
        return mod