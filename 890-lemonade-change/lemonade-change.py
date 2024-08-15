class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_num = {20: 0, 10: 0, 5: 0}
        for bill in bills:
            bills_num[bill] += 1
            rest = bill - 5
            if rest == 5:
                if bills_num[5] == 0:
                    return False
                bills_num[5] -= 1
            if rest == 15:
                if bills_num[10] > 0 and bills_num[5] > 0:
                    bills_num[10] -= 1
                    bills_num[5] -= 1
                elif bills_num[5] > 2:
                    bills_num[5] -= 3
                else:
                    return False
        return True