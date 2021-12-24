"""
Link of the problem set in HackerRank
https://www.hackerrank.com/challenges/bon-appetit

"""

# values = list(map(int, input().rstrip().split()))
n = 4
k = 1
bill = [3, 10, 2, 9]  #list(map(int, input().rstrip().split()))
b = 7  #int(input().strip().split())

def bonAppetit(bill, k, b):
    del bill[k]
    actual_charge = sum(bill)//2
    over_charged = b - actual_charge

    if over_charged != 0:
        print(over_charged)
    else:
        print('Bon Appetit')

bonAppetit(bill, k, b)