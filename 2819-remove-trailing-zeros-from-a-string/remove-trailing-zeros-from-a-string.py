class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1
        c = 0
        while i >= 0:
            if num[i] == '0':
                c += 1
            else:
                break
            i -= 1
        print(c)
        return num[0:i+1]


        