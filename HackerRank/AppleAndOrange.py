def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple = orange = 0
    for drop in apples:
        if t >= a+drop >= s:
            apple += 1
    for drop in oranges:
        if s <= b+drop <= t:
            orange += 1
    print(apple)
    print(orange)

s, t = 7, 11
a, b = 5, 15
m, n = 3, 2
apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)