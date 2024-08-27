class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        o = [i**2 for i in nums]
        return sorted(o)
        