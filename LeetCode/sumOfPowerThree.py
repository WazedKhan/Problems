def checkPowersOfThree(n):
    # pThree = 3
    h_power = 15
    # while pThree <= n:
    #     h_power += 1
    #     pThree *= 3

    check_value, value = n, 0

    for i in range(h_power+1, 0, -1):
        if (3**(i-1)) <= n:
            value += (3**(i-1))
            n -= (3**(i-1))
    return value == check_value



print(checkPowersOfThree(21))