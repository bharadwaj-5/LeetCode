class Solution:
    def bitwiseComplement(self, n: int) -> int:
        m = bin(n).split('b')
        m = m[1]

        s = ''
        for i in m:
            if i == '0':
                s += '1'
            else:
                s += '0'
        return int(s, 2)
        