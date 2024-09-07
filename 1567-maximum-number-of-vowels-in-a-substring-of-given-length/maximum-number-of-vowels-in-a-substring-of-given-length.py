class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {'a','e','i','o','u'}
        n = len(s)
        
        curr = 0
        maxi = 0

        for i in range(k):
            if s[i] in v:
                curr += 1
            maxi = curr

        for i in range(k, n):
            if s[i - k] in v:
                curr -= 1
            if s[i] in v:
                curr += 1
            
            maxi = max(curr, maxi)

        return maxi
        