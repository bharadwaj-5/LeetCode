class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pos = sorted(score, reverse = True)

        for i in range(0, len(score)):
            if pos.index(score[i]) + 1 == 1:
                score[i] = "Gold Medal"
            elif pos.index(score[i]) + 1 == 2:
                score[i] = "Silver Medal"
            elif pos.index(score[i]) + 1 == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(pos.index(score[i]) + 1)
        return score
            
        