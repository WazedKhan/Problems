def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j+1):
        if( (x-int(str(x)[::-1]))%k==0 ):
            count += 1
    return count


first_multiple_input = input().rstrip().split()

i = int(first_multiple_input[0])
j = int(first_multiple_input[1])
k = int(first_multiple_input[2])



result =  beautifulDays(i,j,k)
print(result)