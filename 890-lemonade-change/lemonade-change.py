class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False

        fives, tens = 0, 0

        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                else:
                    return False
            elif i == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives > 2:
                    fives -= 3
                else:
                    return False
        return True