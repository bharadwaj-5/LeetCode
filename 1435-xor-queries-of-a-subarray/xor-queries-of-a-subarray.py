class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        a[:]=accumulate(a,xor);return [(l and a[l-1])^a[r] for l,r in q]      