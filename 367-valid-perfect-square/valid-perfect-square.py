class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            m2 = mid*mid
            if m2 > num:
                right = mid - 1
            elif m2 < num:
                left = mid + 1
            else:
                return True
        
        return False