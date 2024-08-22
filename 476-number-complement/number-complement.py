class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num).split('b')
        m=n[1]
        s=''
        for i in m:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)

        