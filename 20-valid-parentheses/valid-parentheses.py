class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping.keys():
                if stack == [] or stack[-1] != mapping[i]:
                    return False
                stack.pop()
            else:
                return False
            
        return len(stack) == 0




        