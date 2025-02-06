class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        for i in range(0, len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]
        return res
        