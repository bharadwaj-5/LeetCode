class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = pt = 0

        while len(s) > ps and len(t) > pt:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps == len(s)