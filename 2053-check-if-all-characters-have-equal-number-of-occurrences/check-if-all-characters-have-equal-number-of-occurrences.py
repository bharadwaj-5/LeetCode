class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(set(Counter(s).values())) == 1:
            return True
        else:
            return False
        