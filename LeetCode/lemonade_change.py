import re
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash_drawer = []
        accepted_bill_amount = [5, 10, 20]
        lemonade_cost = 5

        for bill in bills:
            if bill == lemonade_cost:
                cash_drawer.append(bill)

            # for bill is 10
            if bill == accepted_bill_amount[1]:
                # need to check if we 5 in our cash drawer
                if accepted_bill_amount[0] in cash_drawer:
                    cash_drawer.remove(accepted_bill_amount[0])
                    cash_drawer.append(bill)
                else:
                    return False
            if bill == accepted_bill_amount[2]:
                # if bill is 20 then we need to return 15
                # we can return 15 two ways-> 5x3 or 10 and 5
                # check if we have 10 and 5 in our cash drawer
                if 10 in cash_drawer and 5 in cash_drawer:
                    # if we have them then remove them from drawer and insert bill/20 in it
                    cash_drawer.remove(10)
                    cash_drawer.remove(5)
                    cash_drawer.append(bill)
                else:
                    # we need to count number of 5 in our cash drawer
                    if cash_drawer.count(5) >= 3:
                        cash_drawer.remove(5)
                        cash_drawer.remove(5)
                        cash_drawer.remove(5)
                        cash_drawer.append(bill)
                    else:
                        return False

        return True


bills = [5, 5, 5, 10, 20]  # True
bills = [5, 5, 10, 10, 20]  # False
bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]  # True
bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20]  # True
solution = Solution().lemonadeChange(bills=bills)
print(f"Can sell lemonade with bills: {bills}: {solution}")
