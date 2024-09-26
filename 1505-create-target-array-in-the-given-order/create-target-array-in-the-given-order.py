class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        op = []

        for i, j in zip(nums, index):
            op.insert(j, i)

        return op
        