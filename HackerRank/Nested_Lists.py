#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
#[[input(),float(input())] for _ in range(int(input()))]
marklist = [['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]

print(sorted(list(set([marks for name, marks in marklist]))))
print(sorted(set([marks for name, marks in marklist])))
