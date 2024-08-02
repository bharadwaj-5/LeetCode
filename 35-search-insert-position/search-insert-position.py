class Solution:
    def searchInsert(self, arr: List[int], x: int) -> int:
        n = len(arr)  # size of the array
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1  # look on the right

        return ans
            