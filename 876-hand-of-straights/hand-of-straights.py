class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        no_groups=len(hand)//groupSize
        hand.sort()
        if no_groups==1:
            for i in range(len(hand)-1):
                if hand[i]!=hand[i+1]-1:
                    return False
            return True
        dict_count = {}
        for n in hand:
            dict_count[n] = 1 + dict_count.get(n, 0)
        #print(dict_count)
        for i in range(len(hand)):
            num=hand[i]
            if dict_count[num]<=0:
                continue
            for j in range(num,num+groupSize):
                if j not in dict_count:
                    return False
                if dict_count[j]>0:
                    dict_count[j]-=1
                else:
                    #print(dict_count)
                    return False
        return True
