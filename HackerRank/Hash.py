"""
https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
step 1: take input n and tuple elements separated by space
step 2: split tuple elements by space
step 3: convert strign to int and list into tuple
step 4: use hash()
"""

n = int(input())
eli = map(int, input().split())
print(hash(tuple(eli)))

# It was mine
#eli = input().split()

# for i in range(n):
#    eli[i] = int(eli[i])
#t = tuple(eli)
# print(hash(t))
