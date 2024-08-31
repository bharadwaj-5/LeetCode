class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = Counter(nums)

        for j in d.values():
            if j > 2:
                return False
        return True
        