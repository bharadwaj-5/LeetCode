class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
        coun = [i for i in range(0, 26)]

        d = dict(zip(alpha, coun))
        sum_a = ''
        for i in firstWord:
            sum_a += str(d[i])
        sum_b = ''
        for j in secondWord:
            sum_b += str(d[j])
        
        summ = int(sum_a) + int(sum_b)
        sum2 = ''
        for i in targetWord:
            sum2 += str(d[i])
        
        if summ == int(sum2):
            return True
        else:
            return False


        