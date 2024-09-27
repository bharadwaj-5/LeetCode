class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        gcd = 1
        for i in range(2, maxi + 1):
            if mini % i == 0 and maxi % i == 0 and i > gcd:
                gcd = i
        return gcd

        