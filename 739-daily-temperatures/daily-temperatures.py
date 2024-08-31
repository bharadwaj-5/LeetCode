class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        stack = []

        for i, t in enumerate(nums):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop() 
                ans[stack_i] = i - stack_i

            stack.append((t, i))

        return ans
