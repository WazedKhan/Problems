def climbStairs(n):
    p_one, p_two = 1,1
    for i in range(n-1):
        temp = p_one
        p_one = p_one + p_two
        p_two = temp
    return p_one

print(climbStairs(2))