s= 'We promptly judged antique ivory buckles for the prize'

def pangrams(s):
    # Write your code
    s = s.lower()
    for i in range(97, 123):
        if chr(i) not in s:
            return 'not pangram'
    return 'pangram'

print(pangrams(s))