class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create the combined string with a separator
        combined = s + "#" + s[::-1]
        
        # Compute the KMP table for the combined string
        def computeKMPTable(s):
            table = [0] * len(s)
            j = 0
            for i in range(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = table[j - 1]
                if s[i] == s[j]:
                    j += 1
                    table[i] = j
                else:
                    table[i] = 0
            return table
        
        table = computeKMPTable(combined)
        # The length of the longest palindrome starting at the first character of s
        max_len = table[-1]
        
        # Add the required characters in front of s to make it a palindrome
        add_on = s[max_len:][::-1]
        return add_on + s


