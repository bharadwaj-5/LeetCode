class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        op = []

        for i in nums:
            i = str(i)
            for j in i:
                op.append(int(j))

        return op
        