class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set(["i", "e", "a", "o", "u", "A", "E", "I", "O", "U"])
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            while s[left] not in v and left < right:
                left += 1
            while s[right] not in v and left < right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        s = ''.join(s)
        return s

        