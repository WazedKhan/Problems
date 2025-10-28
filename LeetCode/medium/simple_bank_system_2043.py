# https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26
# 2043. Simple Bank System
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.acc = balance
        self.acc_len = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 < self.acc_len + 1 and 1 <= account2 < self.acc_len + 1:
            if self.acc[account1 - 1] >= money:
                self.acc[account1 - 1] -= money
                self.acc[account2 - 1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account < self.acc_len + 1:
            self.acc[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account < self.acc_len + 1 and self.acc[account - 1] >= money:
            self.acc[account - 1] -= money
            return True
        return False
