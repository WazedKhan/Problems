#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# [[input(),float(input())] for _ in range(int(input()))] # for taking input from user
 
marklist = [['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
scound_H_mark = sorted(list(set([marks for name, marks in marklist])))[1]
print('\n'.join([name for name, mark in marklist if scound_H_mark == mark]))
