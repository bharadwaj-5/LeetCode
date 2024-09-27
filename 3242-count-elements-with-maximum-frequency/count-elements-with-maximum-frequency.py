class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter = list(counter.values())
        maxCount = max(counter)
        return counter.count(maxCount) * maxCount
