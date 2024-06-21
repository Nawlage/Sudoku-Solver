# Naive Backtracking Algorithm

def read_board(file):
    f=open(file, "r")
    next(f)
    i,j = 0,0
    board = [[0 for x in range(9)] for y in range(9)]
    
    while True:
        char = f.readline()
        for c in char:
            board[i][j] = int(c)
            j += 1
            if j == 9:
                j = 0
                i += 1
                break
        if i == 9:
            break
    return board


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - "*6)
            
        for j in range(len(board[i])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")
        
          
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board,num,pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False


board = read_board("test5.txt")
print("Start\n")
print_board(board)
print("\n")
print("**"*50 + "\n")
solve(board)
print("Solution\n")
print_board(board)