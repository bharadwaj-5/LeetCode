class Solution:
    def reverseWords(self, s: str) -> str:
        op = [i for i in s.split()]
        a = ''
        for i in op[::-1]:
            a+=(i+" ")
        return a.strip()
        