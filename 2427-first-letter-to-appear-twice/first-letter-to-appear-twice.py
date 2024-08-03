class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = set()
        for char in s:
            if char in l: 
                return char
            else: 
                l.add(char)