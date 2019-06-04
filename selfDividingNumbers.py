
def selfDividingHelper(num):
        temp = num
        while temp:
            if not temp % 10 or num % (temp % 10): return False
            temp = temp//10
        return True

def selfDividingNumbers(left, right):
    result = []
    for num in range(left, right+1):
        if selfDividingHelper(num): result.append(num)
    return result
if __name__ == '__main__':
    print(selfDividingNumbers(1,25))