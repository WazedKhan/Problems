# https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26
# 2043. Simple Bank System
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.account = {i + 1: bal for i, bal in enumerate(balance)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.account and account2 in self.account:
            if self.account[account1] >= money:
                self.account[account1] -= money
                self.account[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.account:
            self.account[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.account and self.account[account] >= money:
            self.account[account] -= money
            return True
        return False
