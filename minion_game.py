s = 'BANANA'
vowels = 'AEIOU'
kevin = 0
stuart = 0

for i in range(len(s)):
    if s[i] in vowels:
        kevin += len(s)-i
        
    else:
        stuart += len(s)-i

if stuart > kevin:
    print('Stuart ', stuart)
elif kevin > stuart:
    print('Kevin ', kevin)
else:
    print("Draw")