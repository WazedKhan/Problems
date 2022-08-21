"""
    Codeforces
---------------------
A. Way Too Long Words
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output:standard output
"""

"""
[Pseudocode]
step-1: Check if len if input is more then 10 (means < then 10)
step-2: if step-1 take first and last char of the the word then find len of the word without first and last char
step-3: concate first+len+last and print it
step-4: if not step-1 print the word
"""


n = int(input())

for _ in range(n):
    word = input()
    word_len = len(word)
    if word_len > 10:
        print(word[0]+str(word_len-2)+word[-1])
    else:
        print(word)