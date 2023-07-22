class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        d = {}
        for key in hand:
            if key not in d:
                d[key] = 0
            d[key] += 1
        print(d)
        for num in hand:
            if d[num] > 0:
                for i in range(groupSize):
                    if num+i not in d:
                        return False
                    if d[num+i] > 0:
                        d[num+i] -= 1
                    else:
                        return False
        return True
