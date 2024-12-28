class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        for i, j in c.items():
            if j > len(nums)//2:
                return i
            