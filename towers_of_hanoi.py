
def towers_of_hanoi(n, src, dest, temp,res):
    if n==1:
        s = 'disk 1 from ',src,'->',dest
        res.append(s)
        return
    towers_of_hanoi(n-1, src, temp, dest, res)
    s = 'disk ',n, ' from ',src,'->',dest
    res.append(s)
    towers_of_hanoi(n-1, temp, dest, src, res)
    return res
    
def steps_in_tower_of_hanoi(no_of_disks):
    res  = towers_of_hanoi(no_of_disks, 'A', 'C', 'B',[])
    return res

if __name__ == "__main__":

    no_of_disks = int(input())

    res = steps_in_tower_of_hanoi(no_of_disks)

    print('\n'.join([' '.join(map(str, x)) for x in res]))
    print('\n')
