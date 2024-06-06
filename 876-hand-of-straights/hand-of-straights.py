class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count = {num: hand.count(num) for num in hand}
        for num in count.keys():
            while count[num] > 0:
                for i in range(1, groupSize):
                    if num+i not in count or count[num+i] == 0:
                        return False
                    count[num+i] -= 1
                count[num] -= 1
        return True


