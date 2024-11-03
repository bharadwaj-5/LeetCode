class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        o = []
        for i in range(1, len(s)+1):
            o.append(s[i:] + s[:i])

        if goal in o:
            return True
        else:
            return False   