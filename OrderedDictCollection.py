"""
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.
"""
"""
Task

You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, .
The next  lines contains the item's name and price, separated by a space.

"""

"""
Pseudocode:
    1: Create a ordered Dictionary
    2: Take 'n' value as number of items
    3: Loop over n times and take inputs for n times
    4: Splits inputs by space and find the str to int convertible str
    5: Try to add the net_price to the 'item_name' if its not found handle it with except of 'KeyError'
    6: If step 5 rise exception add new key and value by 'item_name' and 'net_price' to the Orderd Dictionary

"""

from collections import OrderedDict

ordered_dictionary = OrderedDict()


for _ in range(int(input())):
    val = list(input().split()) #takes inputs, splits the values and store as a list
    item_name = ' '.join(val[:-1]) #joins list with space
    net_price = int(val[-1]) # take the last element of list as its the price and covert it to int value
    try:
        ordered_dictionary[item_name] += net_price
    except KeyError:
        ordered_dictionary[item_name] = net_price

for key, value in ordered_dictionary.items():
    print(f'{key} {value}')