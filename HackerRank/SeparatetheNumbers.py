s = '91011'
b_num = ''
list_ = []

def separateNumbers(s):
    # Write your code here
    n = len(s)
    for i in range(1,1+n//2):
        temp_int = int(s[:i])
        print(temp_int)
    #     j=0
    #     temp_str = ""
    #     while(len(temp_str) < n):
    #         temp_str += str(temp_int + j)
    #         j += 1
    #     if temp_str == s:
    #             return "YES {}".format(temp_int)
    # return 'NO'

separateNumbers(s)