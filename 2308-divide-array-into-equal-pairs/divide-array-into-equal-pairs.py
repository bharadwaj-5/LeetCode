class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i)%2==1:
                return False
        return True
        

