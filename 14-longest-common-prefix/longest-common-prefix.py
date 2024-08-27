class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)

        a = strs[0]
        b = strs[-1]

        o = ''

        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                return o
            o += a[i]
        return o

