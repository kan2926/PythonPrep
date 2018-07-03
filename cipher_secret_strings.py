_,s,k = input(),input(), int(input())
def cipher(c):
    num = ord(c)
    if 97 <= num <= 122:
        return chr(((num-97+k)%26)+97)
    elif 65 <= num <= 90:
        return chr(((num-65+k)%26)+65)
    else: return c
    return [cipher(c) for c in s]
