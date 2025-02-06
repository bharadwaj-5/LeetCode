class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float('inf')

        for i in strs:
            if len(i) < minLen:
                minLen = len(i)
        
        i = 0
        while i < minLen:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            
            i += 1
        
        return strs[0][:i]