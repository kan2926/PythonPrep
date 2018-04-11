def get_all_anagrams(so_far, rem):
    if rem == '':
        print(so_far)
    else:
        for i in range(0,len(rem)):
            next_pick = so_far + rem[i]
            rest = rem[0:i] + rem[i+1:]
            get_all_anagrams(next_pick, rest)

i = input("enter a string:")
get_all_anagrams('',i)
