
def add_upto_target(a, i, n, target, result):
    if i == n :
        print(result)
        return result
    
    rest = a[0:i]+a[i+1:]
    print("rest --- ",rest)
    add_upto_target(a, i+1, n, target,result)
    total = int(a[i]) + int(rest)
    if total == target:
        app_str = a[i],"+",rest
        result.append(app_str)
    print(total)
    add_upto_target(a, i+1, n, target,result)

    return result


def generate_all_expressions(a, target):
    result = add_upto_target(a, 0, len(a), target,[])
    return result

if __name__ == "__main__":
    try:
        s = str(input())
    except:
        s = None

    target = int(input());

    res = generate_all_expressions(s, target);
    for res_cur in res:
        print( str(res_cur) + "\n" )

