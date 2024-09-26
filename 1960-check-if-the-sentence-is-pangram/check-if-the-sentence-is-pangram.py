class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = Counter(sentence)

        if len(d) < 26:
            return False
        return True
        