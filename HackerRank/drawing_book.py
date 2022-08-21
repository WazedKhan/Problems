# https://www.hackerrank.com/challenges/drawing-book

def pageCount(n, p):
    
    return min(p//2, (n//2 - p//2))
n = 6
p = 5

pageCount(n, p)
