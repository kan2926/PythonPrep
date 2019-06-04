def heightChecker(heights):
    return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
    
    
print(heightChecker([1,1,4,2,1,3]))