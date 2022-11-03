def solution(x, y):
    # Your code here
    count = 0
    m,f = int(x), int(y)
    while m != f:

        if m > f:
            m = (m-f)
            count += 1

        if f > m:
            f = (f-m)
            count += 1

    if m != 1:
        return 'impossible'
    else:
        return str(count)

print(solution(10**8, 1))