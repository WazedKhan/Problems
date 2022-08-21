# https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, ar):
    pair = 0
    count = 0
    while len(ar) != 0:
        for i in ar:
            if ar[0] == i:
                count += 1
        if count//2 > 0:
            pair += count//2
        ar = list(filter(lambda x: x != ar[0], ar))
        count = 0
    print(pair)


n = 7
list_ = [10, 20, 20, 10, 10, 30, 50, 10, 20]

sockMerchant(n, list_)