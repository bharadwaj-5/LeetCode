class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        o = 0
        for i in range(0, len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                o = i
                break
            else:
                o = -1
                

        return o