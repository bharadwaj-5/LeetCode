class Solution:
    def convertToTitle(self, n: int) -> str:
        o = ''

        while n > 0:
            index = (n - 1) % 26
            o = chr(index + ord('A')) + o
            n = (n - 1) // 26\
            
        return o
        
        