from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return [item for items, c in Counter(s).most_common() for item in [items] * c]
            