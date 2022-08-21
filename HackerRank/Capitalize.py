s = '1 w 2 r gg'
for i in s.split():
    s = s.replace(i, i.capitalize())

print(s)