class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        allnums = set([i for i in range(1, len(nums) + 1)])
        return list(allnums - set(nums))
