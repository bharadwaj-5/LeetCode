class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move = {
            'U': [1,0],
            'D': [-1,0],
            'L': [0,-1],
            'R': [0,1],
        }
        s = [0,0]
        for i in moves:
            s[0] += move[i][0]
            s[1] += move[i][1]
        
        if s == [0,0]:
            return True
        else:
            return False

        