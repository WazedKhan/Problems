N = int(input())
arr = []

for _ in range(N):
    eli = input().split()
    string = eli[0]
    num = eli[1:]
    if string != 'print':
        string += "("+",".join(num)+")"
        eval("arr."+string)
    else:
        print(arr)
