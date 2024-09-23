# Python3 program to check if a number is Palindrome

# Function to check Palindrome
def check_palindrome(n):
    reverse = 0
    # Copy of the original number so that the original
    # number remains unchanged while finding the reverse
    temp = n
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    # If reverse is equal to the original number, the
    # number is palindrome
    return reverse == n

# Sample Input
n = -121
if check_palindrome(n):
      print("Yes")
else:
      print("No")
