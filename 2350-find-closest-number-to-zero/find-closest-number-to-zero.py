class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini = nums[0]

        for i in nums:
            if abs(i) < abs(mini):
                mini = i
        
        if mini < 0 and abs(mini) in nums:
            return abs(mini)
        return mini
        