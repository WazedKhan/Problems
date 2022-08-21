s = '01:01:00PM'

hour24 = int(s[:2])
if s[-2:] == 'PM':
    hour24 += 12
    if hour24 == 24:
        print(s[:-2])
    else:
        print(str(hour24)+s[2:-2])
elif s[-2:] == 'AM':
    if hour24 == 12:
        print('00'+s[2:-2])

print(s[:-2])