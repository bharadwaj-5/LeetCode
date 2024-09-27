class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        new_nums = []

        while len(nums) != 1:
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1])%10)
            nums = new_nums.copy()
            new_nums.clear()
        return nums[0]
        