 
global sol_cnt
sol_cnt = 0

def printSolution(board,n):
    global sol_cnt
    sol_cnt += 1
    print(sol_cnt,'-')
    for i in range(n):
        for j in range(n):
            print( board[i][j],  end= ' ')
        print()

 
# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, row, col,n):
 
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'q':
            return False
 
    # Check upper diagonal on left side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 'q':
            return False
 
    # Check lower diagonal on left side
    for i,j in zip(range(row,n,1), range(col,-1,-1)):
        if board[i][j] == 'q':
            return False
 
    return True
 
def solveNQUtil(board, col, n):
    # base case: If all queens are placed
    # then return true
    if col == n:
        printSolution(board,n)
        return True
 
    # Consider this column and try placing
    # this queen in all rows one by one
    res = False
    for i in range(n):
     
        if isSafe(board, i, col,n):
            # Place this queen in board[i][col]
            board[i][col] = 'q'
 
            # recur to place rest of the queens
            res = (solveNQUtil(board, col+1, n)) | res
 
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = '_'
 
    # if queen can not be place in any row in
    # this colum col  then return false
    return res
 
# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one  of the
# feasible solutions.
def solveNQ(n):
    board = [[ '_' for i in range(n) ] for i in range(n)]
    
    if solveNQUtil(board, 0,n) == False:
        print(" Solution does not exist")
        return False    
    return True
 
# driver program to test above function
n = int(input(' Grid size: '))
solveNQ(n)
 
