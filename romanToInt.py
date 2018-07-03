def romanToInt(s):
    r_to_i = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    for i, j in enumerate(s):
            if r_to_i[s[i]] > r_to_i[s[i-1]] and i > 0:
                result += r_to_i[s[i]] - 2 * r_to_i[s[i-1]]
            else:
                result += r_to_i[j]
    return result

print(romanToInt("MMMCMXCIX"))
