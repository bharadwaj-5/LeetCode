class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        op = []
        hashMap = {}

        for i, v in enumerate(temp):
            if v not in hashMap:
                hashMap[v] = i
        
        for i in nums:
            op.append(hashMap[i])
                
        return op