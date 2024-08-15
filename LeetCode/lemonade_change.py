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

    def lemonade_change(self, bills: List[int]) -> bool:
        """
        Determines if we can provide correct change to each customer in line
        using a limited number of $5 and $10 bills.

        Args:
            bills (List[int]): A list of bills each customer provides (either $5, $10, or $20).

        Returns:
            bool: True if it's possible to provide the correct change to each customer, False otherwise.
        """

        # Counters for the number of $5 and $10 bills
        five_counter = 0
        ten_counter = 0

        # Iterate over each bill in the provided bills
        for bill in bills:
            if bill == 5:
                # Customer pays with a $5 bill
                # Increase the count of $5 bills
                five_counter += 1

            elif bill == 10:
                # Customer pays with a $10 bill
                if five_counter > 0:
                    # If we have a $5 bill, we can give change
                    ten_counter += 1
                    five_counter -= 1
                else:
                    # No $5 bill to give as change, return False
                    return False

            else:  # bill == 20
                # Customer pays with a $20 bill
                if ten_counter > 0 and five_counter > 0:
                    # If we have a $10 and a $5 bill, give one of each as change
                    ten_counter -= 1
                    five_counter -= 1
                elif ten_counter <= 0 and five_counter >= 3:
                    # If no $10 bill but at least three $5 bills, give three $5 bills as change
                    five_counter -= 3
                else:
                    # Not enough change to give, return False
                    return False

        # If we successfully give change to every customer, return True
        return True


# install all the requirements: pip install -r requirement.txt
# to check it run: pytest
