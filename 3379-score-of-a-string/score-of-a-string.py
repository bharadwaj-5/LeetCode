class Solution:
    def scoreOfString(self, s: str) -> int:
        s = list(s)
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score


