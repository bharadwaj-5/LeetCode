class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        op = [i for i in nums]
        for i in nums:
            i = str(i)
            op.append(int(i[::-1]))
        return len(set(op))