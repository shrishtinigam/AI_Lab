# incremental formulation

# print board
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 1):
                print("Q", end = " ")
            else:
                print("-", end = " ")
        print("\n")
    print("\n")

# checks if the we can put the queen in r,c position, (i.e. it checks if it being attacked)
def not_attacking(board, r, c):
    n = len(board)
    # checks if there are any other queens in that row on the left side
    for i in range(c):
        if(board[r][i] == 1):
            return False
    # diagonally checks top left
    j = c
    for i in range(r, 0, -1):
        if(board[i][j] == 1):
            return False
        j -= 1
    # diagonally checks bottom left
    j = c
    for i in range(r, n):
        if(board[i][j] == 1):
            return False
        j -= 1
    return True

def solver(board, c):
    n = len(board)
    if(c >= n):       
        return True, board
    for i in range(n):
        if(not_attacking(board, i, c)):
            board[i][c] = 1
            b, board = solver(board, c + 1)
            if(b):
                return True, board
            board[i][c] = 0
    return False, board

n = int(input("Enter the value of N: "))
board = [[0 for i in range(n)] for i in range(n)]
a, ans = solver(board, 0)
print_board(ans)