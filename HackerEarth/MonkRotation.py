
def rotateArray():
    n, k = 5, 5 #map(int, input().split())
    arr = list('1 2 3 4 5 5 9 3 10 12 13 15 45'.split())
    index = n - (k%n)

    for i in range(index, n):
        print(arr[i], end=' ')
    for i in range(index):
        print(arr[i], end=' ')



rotateArray()