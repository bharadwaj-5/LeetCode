class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        grouped_list = [sorted(group) for key, group in groupby(nums, lambda x: bin(x).count('1'))]      
        return sorted(nums) == [*chain(*grouped_list)]
    
        