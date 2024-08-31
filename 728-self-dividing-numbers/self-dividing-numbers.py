class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        o = []
        def div(x):
            res = False
            for i in str(x):
                if i == '0':
                    res = False
                    break
                if x % int(i) == 0:
                    res = True
                else:
                    res = False
                    break
            return res

        for i in range(left, right+1):
            if div(i):
                o.append(i)
        
        return o

        