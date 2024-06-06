class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count = Counter(hand)
        for num in count.keys():
            if count[num] == 0:
                continue
            for i in range(1, groupSize):
                if num+i not in count or count[num+i] < count[num]:
                    return False
                count[num+i] -= count[num]
        return True


