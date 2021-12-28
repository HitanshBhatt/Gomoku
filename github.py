#https://github.com/d-hasan/Gomoku-CSC/blob/master/gomoku.py
"""Gomoku starter code
Author(s): Michael Guerzhoy, Dylan Vogel, and Danial Hasan, with tests contributed by Siavash Kazemian.  
           Last modified: Nov. 13, 2016
"""

def is_empty(board):
    ''' Return True if board board is empty, False otherwise.
        Board is an nxn matrix stored as a list of lists.'''

    for i in range(len(board)):
        for n in range(len(board[i])):
            if board[i][n] != " ":
                return False
    return True
    
def is_full(board):
    ''' Return True or False depending on if board is full of pieces or not.
        Assume board is an nxn matrix.'''
        
    for i in range(len(board)):
        for n in range(len(board[i])):
            if board[i][n] == " ":
                return False
    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    ''' Return "OPEN", "SEMIOPEN", or "CLOSED" depending on the status of sequence length length ending at      
        [y_end][x_end] on board board. 
        Board is a nxn matrix stored as a list of lists; y_end, x_end, and length are positive ints and length 
        is greater than one.
        (d_y, d_x) is one of: (1, 0), (0, 1), or (1, ±1)'''
    
    end_status = ""
    start_status = ""
    
    #check that y_end & x_end are valid coordinates
    if (max(y_end, x_end) >= len(board)) or (min(y_end, x_end) < 0):
        return "CLOSED"
    
    #check the end adjecant to y_end, x_end
    if (min(y_end + d_y, x_end + d_x) < 0) or (max(y_end + d_y, x_end + d_x) >= len(board)):
        end_status = "CLOSED"
    elif board[y_end + d_y][x_end + d_x] == " ":
        end_status = "OPEN"
    else:
        end_status = "CLOSED"
    
    #check the end opposite of y_end, x_end
    if (min(y_end - (d_y * length), x_end - (d_x * length)) < 0) or (max(y_end - (d_y * length), x_end - (d_x * length)) >= len(board)):
        start_status = "CLOSED"
    elif board[y_end - (d_y * length)][x_end - (d_x * length)] == " ":
        start_status = "OPEN"
    else:
        start_status = "CLOSED"
    
    #analyze the status of the sequence
    if end_status != start_status:
        return "SEMIOPEN"
    elif start_status == "OPEN" and end_status == "OPEN":
        return "OPEN"
    else:
        return "CLOSED"
    
def check_length(board, col, y_start, x_start, d_y, d_x):
    ''' Returns an integer length which is the length of sequence of color col, starting at (y_start, x_start) 
        and proceeding in the (d_y, d_x) direction 
        Assume board is a nxn matrix, col is one of 'b' or 'w', (y_start, x_start) are coordinates on the 
        board, and (d_y, d_x) is one of: (1, 0), (0, 1), or (1, ±1).'''
        
    y = y_start
    x = x_start
    length = 1
    
    if board[y_start][x_start] != col:
        return 0
        
    for i in range(len(board)):
        if (max(y + d_y, x + d_x) >= len(board)) or (min(y + d_y, x + d_x) < 0 ) or board[y + d_y][x + d_x] != col:
            return length
        length += 1
        y += d_y
        x += d_x
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    ''' Return a tuple of the number of open and semi-open sequences of colour col and length length
        in the row starting at y_start, x_start and proceeding in the direction d_y, d_x.
        Assume board is a nxn matrix, col is one of 'b' or 'w', length is a positive int greater than one, and
        (d_y, d_x) is one of: (1, 0), (0, 1), or (1, ±1).
        '''
    open_seq_count = 0
    semi_open_seq_count = 0
    cur_length = 0
    
    for i in range(len(board) + 1):
        if y_start + d_y > len(board) or x_start + d_x > len(board) or y_start + d_y < 0 or x_start + d_x < 0:
            return open_seq_count, semi_open_seq_count
        elif board[y_start][x_start] == col:
            cur_length = check_length(board, col, y_start, x_start, d_y, d_x)
            if length == cur_length:
                status = is_bounded(board, y_start + ((length - 1) * d_y), x_start + ((length - 1) * d_x), length, d_y, d_x)
                if status == "OPEN":
                    open_seq_count += 1
                if status == "SEMIOPEN":
                    semi_open_seq_count += 1
                
                y_start += (length - 1) * d_y
                x_start += (length - 1) * d_x
            else:
                
                y_start += (cur_length - 1) * d_y
                x_start += (cur_length - 1) * d_x
        
        y_start += d_y
        x_start += d_x
        

def detect_row_win(board, col, y_start, x_start, length, d_y, d_x):
    ''' Return True or False depending on if sequences of colour col and length 5 in the row starting at    
        y_start, x_start and proceeding in the direction d_y, d_x.
        Assume board is a nxn matrix, col is one of 'b' or 'w', length is 5, and (d_y, d_x) is one of: (1, 0), 
        (0, 1), or (1, ±1).
        '''
    cur_length = 0
    found = False
    
    for i in range(len(board) + 1):
        if y_start + d_y > len(board) or x_start + d_x > len(board) or y_start + d_y < 0 or x_start + d_x < 0:
            return found
        elif board[y_start][x_start] == col:
            cur_length = check_length(board, col, y_start, x_start, d_y, d_x)
            if length == cur_length:
                found = True
            else:
                y_start += (cur_length - 1) * d_y
                x_start += (cur_length - 1) * d_x
        y_start += d_y
        x_start += d_x

def detect_rows(board, col, length):
    ''' Return a tuple of the number of open and semi-open sequences of colour col and length length on board board.
        Assume board is a nxn matrix, col is one of 'b' or 'w', and length is a positive int greater than one and less than 6.
        Board is a nxn matrix stored as a list of lists, col is one of 'b' or 'w', and length is a positive int         
        greater than one.
        '''
    
    open_seq_count, semi_open_seq_count = 0, 0
    
    #check rows
    for row in range(len(board)):
        count_tuple = detect_row(board, col, row, 0, length, 0, 1)
        open_seq_count += count_tuple[0]
        semi_open_seq_count += count_tuple[1]
    
    #check columns
    for column in range(len(board)):
        count_tuple = detect_row(board, col, 0, column, length, 1, 0)
        open_seq_count += count_tuple[0]
        semi_open_seq_count += count_tuple[1]
        
    #check diagonals
    for diagonal in range(len(board) - 1):      # the "- 1" prevents it from double counting the corner diagonals
        #top row
        for dir in (1, -1):
            count_tuple = detect_row(board, col, 0, diagonal, length, 1, dir)
            open_seq_count += count_tuple[0]
            semi_open_seq_count += count_tuple[1]
        #bottom row
            count_tuple = detect_row(board, col, len(board) - 1, diagonal, length, -1, dir)
            open_seq_count += count_tuple[0]
            semi_open_seq_count += count_tuple[1]

    return open_seq_count, semi_open_seq_count


def detect_rows_win(board, col):
    ''' Return True or False if a sequence of colour col and length 5 exists on board board.
        Assume board is an nxn matrix, col is one of 'b' or 'w', and length is 5.
        '''
    length = 5
    #check rows
    for row in range(len(board)):
        if detect_row_win(board, col, row, 0, length, 0, 1):
            return True
    
    #check columns
    for column in range(len(board)):
        if detect_row_win(board, col, 0, column, length, 1, 0):
            return True
        
    #check diagonals
    for diagonal in range(len(board) - 1):      # the "- 1" prevents it from double counting the corner diagonals
        #top row
        for dir in (1, -1):
            if detect_row_win(board, col, 0, diagonal, length, 1, dir):
                return True
        #bottom row
            if detect_row_win(board, col, len(board) - 1, diagonal, length, -1, dir):
                return True
    return False
    

def search_max(board):
    ''' Return coordinates row, column, of the best move black could make given the current board board
        Board is an nxn matrix stored as a list of lists. '''
    
    CUR_SCORE = score(board)
    best_move = (-1, -1)
    
    #create a deep copy of board board
    test_board = []
    for sublist in board:
        test_board.append(sublist[:])
    
    #check for the highest scoring black 'b' move
    for row in range(len(test_board)):
        for column in range(len(test_board)):
            if test_board[row][column] != ' ':
                continue
            test_board[row][column] = 'b'
            new_score = score(test_board)
            if new_score > CUR_SCORE:
                CUR_SCORE = new_score
                best_move = row, column
            test_board[row][column] = ' '
    
    if best_move != (-1, -1):
        return best_move
    else:           #if there is no best move, move to the first empty square
        for row in range(len(test_board)):
            for column in range(len(test_board)):
                if test_board[row][column] == ' ':
                    return row, column
    pass
    
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

    
def is_win(board):
    ''' Return one of "White won", "Black won", "Draw", or "Continue playing" depending on current board status.
        Assume board is an nxn matrix.'''
    
    if detect_rows_win(board, 'b'):
        return 'Black won'
    elif detect_rows_win(board, 'w'):
        return 'White won'
    elif is_full(board):
        return 'Draw'
    else:
        return 'Continue playing'


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
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
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
    
    #Test 1: easy_testset_for_main_functions()
    print("Test 1")
    easy_testset_for_main_functions()
    
    #Test 2: some_test()
    print("===============================================", "\nTest 2")
    board = make_empty_board(8)
    print(len(board))
    some_tests()
    
    #Test 3: is_clear() test
        #Testing w/ empty board
    print("===============================================", "\nTest 3")
    board = make_empty_board(8)
    if is_empty(board):
        print("a)Test Passed")
    
        #Testing w/ non empty board
    board[0][0] = 'w'
    if not is_empty(board):
        print("b)Test Passed")
        
    #Test 4: is_bounded() 
        #Testing semiopen sequence
    print("===============================================", "\nTest 4")
    put_seq_on_board(board, 0, 0, 1, 0, 3, 'b')
    if is_bounded(board, 2, 0, 3, 1, 0) == 'SEMIOPEN':
        print("a)Test Passed")
    
        #Testing open sequence
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 1, 1, 0, 3, 'b')
    if is_bounded(board, 3, 1, 3, 1, 0) == 'OPEN':
        print("b)Test Passed")
    
        #Testing closed sequence
    board = make_empty_board(8)
    put_seq_on_board(board, 5, 0, 1, 1, 3, 'b')
    if is_bounded(board, 7, 2, 3, 1, 1) == 'CLOSED':
        print("c)Test Passed")
        
    #Test 5: detect_row()
        #Testing semiopen sequence
    print("===============================================", "\nTest 5")
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 0, 1, 0, 3, 'b')
    if detect_row(board, 'b', 0, 0, 3, 1, 0) == (0, 1):
        print("a)Test Passed")
    
        #Testing open sequence
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 0, 1, 0, 3, 'b')
    if detect_row(board, 'b', 0, 0, 3, 1, 0) == (1, 0):
        print("b)Test Passed")
    
        #Testing open and semiopen sequence
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 0, 1, 0, 3, 'b')
    put_seq_on_board(board, 5, 0, 1, 0, 3, 'b')
    if detect_row(board, 'b', 0, 0, 3, 1, 0) == (1, 1):
        print("c)Test Passed")
    
        #Testing sequences of varying lengths (4 and 3)
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 0, 1, 0, 4, 'b')
    put_seq_on_board(board, 5, 0, 1, 0, 3, 'b')
    if detect_row(board, 'b', 0, 0, 3, 1, 0) == (0, 1):
        print("d)Test Passed")
    
        #Testing diagonal sequences
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 1, 1, 1, 4, 'b')
    if detect_row(board, 'b', 0, 0, 4, 1, 1) == (1, 0):
        print("e)Test Passed")
    
    board = make_empty_board(8)
    put_seq_on_board(board, 6, 2, -1, 1, 4, 'b')
    if detect_row(board, 'b', 7, 1, 4, -1, 1) == (1, 0):
        print("f)Test Passed")
    
    #Test 6: detect_rows()
    print("===============================================", "\nTest 6")
        #Testing one row-open
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 1, 1, 1, 4, 'b')
    if detect_rows(board, 'b', 4) == (1, 0):
        print("a)Test Passed")
    
        #Testing one row-open, one row-semiopen
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 1, 1, 1, 4, 'b')
    put_seq_on_board(board, 0, 6, 1, 0, 4, 'b')
    if detect_rows(board, 'b', 4) == (1, 1):
        print("b)Test Passed")
    
        #Testing one row-open, one row-semiopen, connected 
    board = make_empty_board(8)
    put_seq_on_board(board, 2, 3, 0, 1, 4, 'b')
    put_seq_on_board(board, 0, 6, 1, 0, 4, 'b')
    if detect_rows(board, 'b', 4) == (1, 1): 
        print("c)Test Passed")
    
        #Testing one row-open but of wrong length
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 1, 1, 1, 4, 'b')
    if detect_rows(board, 'b', 3) == (0, 0):
        print("d)Test Passed")
    
    #Test 7: is_win()
    print("===============================================", "\nTest 7")
        #Testing win for black and white
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 6, 1, 0, 5, 'b')
    if is_win(board) == "Black won":
        print("a)Test Passed")
        
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 6, 1, 0, 5, 'w')
    if is_win(board) == "White won":
        print("b)Test Passed")
        
        #Testing continue playing for sequence of 4, board 1 square short of full, and sequence of 6
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 6, 1, 0, 4, 'b')
    if is_win(board) == "Continue playing":
        print("c)Test Passed")
    
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 6, 1, 0, 4, 'w')
    if is_win(board) == "Continue playing":
        print("d)Test Passed")
        
    board = make_empty_board(8)
    for i in range(4):
        put_seq_on_board(board, 0, i, 1, 0, 8, 'b')
        put_seq_on_board(board, 0, i + 4, 1, 0, 8, 'w')
    board[7][7] = ' '
    if is_win(board) == "Continue playing":
        print("e)Test Passed")
    
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 6, 1, 0, 6, 'w')
    if is_win(board) == "Continue playing":
        print("f)Test Passed")
    
        #Testing draw
    board = make_empty_board(8)
    for i in range(4):
        put_seq_on_board(board, 0, i, 1, 0, 8, 'b')
        put_seq_on_board(board, 0, i + 4, 1, 0, 8, 'w')
    if is_win(board) == "Draw":
        print("g)Test Passed")