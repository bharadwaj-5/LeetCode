class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        n = len(words)
        
        for i in range(n):
            last_char = words[i][-1]
            first_char_next = words[(i + 1) % n][0]

            if last_char != first_char_next:
                return False

        return True
     
        