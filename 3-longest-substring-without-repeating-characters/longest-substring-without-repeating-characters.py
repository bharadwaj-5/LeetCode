class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()

        max_len = 0
        left = 0
        n = len(s)
        for right in range(n):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            
            w = right - left + 1

            max_len = max(max_len, w)

            hash_set.add(s[right])

        return max_len