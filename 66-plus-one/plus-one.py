class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''
        for i in digits:
            n+=str(i)

        op = []
        n = int(n)
        n+=1

        for j in str(n):
            op.append(int(j))
        
        return op
        