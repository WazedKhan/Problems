import string
alpha = string.ascii_lowercase

n = 5
patterns = []
for i in range(n):
    s = '-'.join(alpha[i:n])
    patterns.append( (s[::-1]+s[1:]).center(n*n, '-') )
    
print('\n'.join(patterns[:0:-1]+patterns))
