def isPalindrome(x):
    x = str(x)
    return x == x[::-1]

print(isPalindrome(-121))
