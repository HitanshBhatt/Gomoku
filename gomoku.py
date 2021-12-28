"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""

def is_empty(board):
    for rows in range(8):
        for columns in range(8):
            if board[rows][columns] == " ":
                return True
    return False
        
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    seq_start = " "
    seq_end = " "

    if (min(y_end, x_end) < 0 or max(y_end, x_end) > 8):
        return "CLOSED"

    #Left to right
    '''if (d_y == 0 and d_x == 1):
        #check if seq_end is within bounds of the board
        if x_end < 8 and board[y_end][x_end+1] == " ":
            seq_end =  "OPEN"
        elif  x_end > 8:
            seq_end =  "CLOSED"
        else:
            seq_end == "CLOSED"'''

    if (d_y == 0 and d_x == 1):
        #check if seq_end is within bounds of the board
        if x_end+d_x <= len(board) and board[y_end][x_end+d_x] == " ":
            seq_end =  "OPEN"
        elif x_end+d_x > len(board):
            seq_end =  "CLOSED"
        else:
            seq_end == "CLOSED"

        #check if seq_start is within bounds of the board
        if  x_end-d_x < 0: #or board[y_end][x_end-(length*d_x)] > 8:
            seq_start == "CLOSED"
        elif board[y_end][x_end-(length*d_x)-1] == " ":
            seq_start  == "OPEN"
        else:
            seq_start == "CLOSED"

    # Top to bottom        
    elif (d_y == 1 and d_x == 0):
        #check if seq_end is within bounds of the board
        if y_end+d_y <= len(board) and board[y_end+d_y][x_end] == " ":
            seq_end = "OPEN"
        elif y_end+d_y > len(board):
            seq_end =  "CLOSED"
        else:
            seq_end =  "CLOSED"    
      
        #check if seq_start is within bounds of the board
        if y_end-d_y < 0:
            seq_start = "CLOSED"
        elif (y_end-d_y) > 0 and board[y_end-(length*d_y)-1][x_end] == " ":
            seq_start =  "OPEN"
        else:
            seq_start = "CLOSED"

    # Upper-left to lower-right
    elif (d_y == 1 and d_x == 1):   
        #check if seq_end is within bounds of the board  
        if (y_end+d_y) < len(board) and (x_end+d_x) < len(board) and board[y_end+d_y][x_end+d_x] == " ":
            seq_end =  "OPEN"
        elif (y_end+d_y) > len(board) or (x_end+d_x) >= len(board):
            seq_end =  "CLOSED"
        else:
            seq_end = "CLOSED"
          
        #check if seq_start is within bounds of the board
        if (y_end-d_y) < 0 or (x_end-d_x) < 0:
            seq_start =  "CLOSED"
        elif (y_end-d_y) >= 0 and (x_end+d_x) >= 0 and board[y_end-(length*d_y)-1][x_end - (length*d_x)-1] == " ":
            seq_start = "OPEN"
        else:
            seq_start = "CLOSED"

    # Upper-right to lower-left      
    elif (d_y == 1 and d_x == -1): 
        #check if seq_end is within bounds of the board    
        if (y_end+d_y) < len(board) and (x_end+d_x) < len(board) and board[y_end+d_y][x_end+d_x] == " ":
            seq_start = "OPEN"
        elif (y_end+d_y) >= len(board) or (x_end+d_x) > len(board):
            seq_start = "CLOSED"
        else:
            seq_start = "CLOSED"

        #check if seq_start is within bounds of the board    
        if (y_end-d_y) < 0 and (x_end-d_x) < 0:
            seq_end =  "CLOSED"
        elif (y_end-d_y) >= 0 and (x_end-d_x) >= 0 and board[y_end-(length*d_y)-d_y][x_end - (length*d_x)-d_x] == " ":
            seq_end = "OPEN"
        else:
            seq_end = "CLOSED"
    
    if seq_start != seq_end:
        return "SEMI-OPEN"
    elif seq_end == "OPEN" and seq_start == "OPEN":
        return "OPEN"
    else:
        return "CLOSED"

''' if (d_y == 0 and d_x == 1 and col == "W"):#left-to-right
        for rows in range(8):
            for columns in range(8):
                if board[y_end][x_end] == "w" or board[y_end][x_end] == board[]:

        pass
    elif (d_y == 1 and d_x == 0):       #top-to-bottom
        pass
    elif (d_y == 1 and d_x == 1):       #upper left - to - lower right
        pass
    elif (d_y == 1 and d_x == -1):      #upper right - to - lower left
        pass'''
'''
    elif (board[y_end][x_end] == "b"):   # Black 
        if x_end <= 8 and board[y_end][x_end+1] == " ":
            return "OPEN"
        elif x_end > 8 or (board[y_end][x_end+1] == "w" or board[y_end][x_end-(length*d_x)-1] == "w"):
            return "CLOSED"
        else:
            return "SEMI-OPEN"
'''
def col_length(board, col, d_y, d_x, y_start, x_start):
    if board[y_start][x_start] != col:
        return None
    
    for i in range(8):
        pass
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    curr_len = 0
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    ####CHANGE ME
    open_seq_count, semi_open_seq_count = 0, 0

    # d_y = 0, d_x = 1
    for rows in range(len(board)):
        num_tuples = detect_row(board, col, rows, 0, length, 0, 1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]
    
    #d_y = 1, d_x = 0
    for columns in range(len(board)):
            num_tuples = detect_row(board, col, 0, columns, length, 1, 0)
            open_seq_count += num_tuples[0]
            semi_open_seq_count += num_tuples[1]
    
    #d_x == 1, d_y == 1
    for diagonals_y in range(len(board)):
        num_tuples = detect_row(board, col, diagonals_y, 0 , length, 1, 1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    for diagonals_x in range(len(board)):
        num_tuples = detect_row(board, col, 0, diagonals_x , length, 1, 1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]
    
    #d_x = -1, d_y = 1
    for diagonals_y in range(len(board)):
        num_tuples = detect_row(board, col, diagonals_y, 0, length, 1, -1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    for diagonals_x in range(len(board), 0, -1):
        num_tuples = detect_row(board, col, 0, diagonals_x , length, 1, -1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]
    #upacking the tuple
    #open_seq_count, semi_open_seq_count = num_tuples

    #print(num_tuples)
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    #return move_y, move_x
    pass

#don't modify
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_filled(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != " ":
                return True


def is_win(board):
    if is_filled(board) == True:
        return "Draw"
    else:
        "Keep playing"


#don't modify
def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                

#don't modify
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
#don't modify
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
#don't modify   
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    test_is_empty()
    test_is_bounded()
    test_detect_rows()