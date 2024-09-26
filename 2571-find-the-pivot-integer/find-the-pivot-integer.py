class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2  
        left_sum = 0
        
        for i in range(1, n + 1):
            left_sum += i  
            right_sum = total_sum - left_sum  
            
            if left_sum == right_sum + i:
                return i
        
        return -1 



        