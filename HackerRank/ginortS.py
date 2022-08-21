string = 'Sorting2341'
l_str = u_str = n_str = ''
numbers = ''

def sorting(numbers):
    odd = even = ''
    numbers = ''.join(sorted(numbers))
    for i in numbers:
        if int(i)%2 == 0:
            even += str(i)
        else:
            odd += str(i)
    return odd+even

for i in string:
    if i.upper() != i and i.isdigit() == False:
        l_str += i
    if i.upper() == i and i.isdigit() == False:
        u_str += i
    if i.isdigit() == True:
        numbers += str(i)


lower_words = ''.join(sorted(l_str))
upper_words = ''.join(sorted(u_str))

print(lower_words+upper_words+sorting(numbers))
