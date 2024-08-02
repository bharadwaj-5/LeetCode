class Solution:
    def checkString(self, s: str) -> bool:
        o = [i for i in s]

        if o == sorted(o):
            return True
        else:
            return False
        