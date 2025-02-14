class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, v in enumerate(nums):
            if target - v in hashMap:
                return [i, hashMap[target - v]]
            hashMap[v] = i