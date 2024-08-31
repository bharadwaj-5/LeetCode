class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)

        while low < high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1

        return letters[high] if high < len(letters) else letters[0] 