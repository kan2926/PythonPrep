def add_digits(num):
    if num == 0 : return 0
    else:return (num - 1) % 9 + 1
        


n = 1234567
print(add_digits(n))
