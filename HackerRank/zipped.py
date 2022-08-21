# This code is for understanding bulid in zip function of python
n, x= map(int,input().strip().split())

marks = []

for _ in range(x):
    marks.append(list(map(float, input().split())))

for i in zip(*marks):
    print(sum(i)/len(i))