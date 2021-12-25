s = 'aba'
n=10
print(s[:n % len(s)].count('a')+s.count("a")*(n // len(s)))
