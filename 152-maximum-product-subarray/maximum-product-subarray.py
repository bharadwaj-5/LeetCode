class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float('-inf')
        leftProduct = 1
        rightProduct = 1
        n = len(nums)
        
        for i in range(n):
            if leftProduct == 0:
                leftProduct = 1
            leftProduct *= nums[i]
            maxProduct = max(maxProduct, leftProduct)
            
            if rightProduct == 0:
                rightProduct = 1
            rightProduct *= nums[n - 1 - i]
            maxProduct = max(maxProduct, rightProduct)
        
        return maxProduct


        