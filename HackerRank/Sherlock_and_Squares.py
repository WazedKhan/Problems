# https://www.hackerrank.com/challenges/sherlock-and-squares

import math

def squares(a, b):
    # count = 0
    # for i in range(a,b+1):
    #     if math.sqrt(i)%int(math.sqrt(i))==0:
    #         count += 1
    # print(count)
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    
    print(sqrtB - sqrtA+1)
        

q = int(1)

for q_itr in range(q):
    # first_multiple_input = input().rstrip().split()
    a = int(3)
    b = int(9)
    
print(squares(a, b))
