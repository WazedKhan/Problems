# https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26
# 2043. Simple Bank System
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        """
        Initialize the Bank with accounts mapping 1-based account IDs to their balances.
        
        Parameters:
            balance (List[int]): List of initial balances where the account ID for balance[i] is i + 1.
        """
        self.account = {i + 1: bal for i, bal in enumerate(balance)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfer money from one account to another if both accounts exist and the source has sufficient funds.
        
        Parameters:
            account1 (int): Source account ID (1-based).
            account2 (int): Destination account ID (1-based).
            money (int): Amount to transfer.
        
        Returns:
            bool: `True` if the transfer was completed, `False` otherwise.
        """
        if account1 in self.account and account2 in self.account:
            if self.account[account1] >= money:
                self.account[account1] -= money
                self.account[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposit money into an existing account.
        
        Parameters:
            account (int): 1-based account ID.
            money (int): Amount to add to the account balance.
        
        Returns:
            bool: True if the account exists and the deposit was applied, False otherwise.
        """
        if account in self.account:
            self.account[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        """
        Attempt to withdraw a specified amount from an account.
        
        Parameters:
            account (int): 1-based account ID to withdraw from.
            money (int): Amount to withdraw.
        
        Returns:
            bool: `true` if the account exists and had at least `money` (withdrawal performed), `false` otherwise.
        """
        if account in self.account and self.account[account] >= money:
            self.account[account] -= money
            return True
        return False