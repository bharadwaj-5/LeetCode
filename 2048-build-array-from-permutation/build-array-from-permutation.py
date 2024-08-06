class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        o = []

        for i in range(0, len(nums)):
            o.append(nums[nums[i]])

        return o

        