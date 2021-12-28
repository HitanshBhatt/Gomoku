def is_empty(board):
    for rows in range(8):
        for columns in range(8):
            if board[rows][columns] == " ":
                return True
    return False


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    counter = 0
    # horizontal sequence
    if d_y == 0 and d_x == 1:
        if x_end - length + 1 == 0:  # if x starting is 0; ie. next to wall
            counter += 1
            if x_end == len(board) - 1:  # if x ends at a wall
                counter += 1
            elif board[y_end][x_end - length] != " ":  # if x ends next to a stone
                counter += 1

        elif x_end - length + 1 != 0:  # if not start next to a wall
            if x_end == len(board) - 1:  # if x ends at a wall
                counter += 1
            elif board[y_end][x_end - length] != " ":  # if start is next to a stone, it is bounded
                counter += 1
                if x_end == len(board) - 1:  # if x ends at a wall
                    counter += 1
                elif board[y_end][x_end - length] != " ":  # if x ends next to a stone
                    counter += 1


    # vertical sequence
    elif d_y == 1 and d_x == 0:
        if y_end - length + 1 == 0:  # if y starting is 0; ie. next to wall
            counter += 1
            if y_end == len(board) - 1:  # if y ends at a wall
                counter += 1
            elif board[y_end - length][x_end] != " ":  # if x ends next to a stone
                counter += 1

        elif y_end - length + 1 != 0:  # if not start next to a wall
            if y_end == len(board) - 1:  # if x ends at a wall
                counter += 1
            elif board[y_end - length][x_end] != " ":  # if start is next to a stone, it is bounded
                counter += 1
                if y_end == len(board) - 1:  # if x ends at a wall
                    counter += 1
                elif board[y_end - length][x_end] != " ":  # if x ends next to a stone
                    counter += 1


    # diagonal sequence 1
    elif d_y == 1 and d_x == 1:
        if (x_end - length + 1 == 0) or (y_end - length + 1 == 0):  # start next to a wall
            counter += 1
        else:
            if board[y_end - length][x_end - length] != " ":  # if start is next to a stone, it is bounded
                counter += 1
        if (x_end == len(board) - 1 or y_end == len(board) - 1):
            counter += 1
        else:
            if board[y_end + 1 + length - length][x_end + 1] != " ":  # end next to stone
                counter += 1


    # diagonal sequence 2
    else:
        if (x_end + length - 1 <= 0) or (y_end - length - (1) <= 0):
            counter += 1
        else:
            if (board[y_end - length][x_end - length] != " "):
                counter += 1
        if (x_end == 0 or y_end == len(board) - 1):
            counter += 1  # if the stone is at the end or begining it must atleast be semi bounded
        else:
            if (board[y_end + 1][x_end - 2 + length - length + 1] != " "):
                counter += 1  # if stone at end increase bounded

    if counter == 1:
        return "SEMIOPEN"
    elif counter == 2:
        return "CLOSED"
    elif counter != 1 or counter != 2:
        return "OPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_sequence_counter = 0
    semi_open_sequence_counter = 0
    length_new = length
    # set counters to 0
    # print(len(board))

    for e in range(9):  # colour specific iteration by for loop
        if (y_start + d_y) > 8:
            return open_sequence_counter, semi_open_sequence_counter
        elif (x_start + d_x) > 8:
            return open_sequence_counter, semi_open_sequence_counter
        elif (y_start + d_y) < 0:
            return open_sequence_counter, semi_open_sequence_counter
        elif (x_start + d_x) < 0:
            return open_sequence_counter, semi_open_sequence_counter
        elif board[y_start][x_start] == col:  # if y_start or x_start is outside board parameters, end loop by returning

            def helper(board, col, y_start, x_start, d_y, d_x):
                y_length = y_start
                x_length = x_start
                length_new = 1

                if board[y_start][x_start] != col:
                    integer_value = 0
                    return integer_value
                for i in range(8):
                    max1_list = []
                    max1_list.append(y_length + d_y)
                    max1_list.append(x_length + d_x)
                    max1_list.sort()

                    min2_list = []
                    min2_list.append(y_length + d_y)
                    min2_list.append(x_length + d_x)
                    min2_list.sort()

                    if max1_list[len(max1_list) - 1] >= len(board):
                        return length_new

                    elif min2_list[0] < 0:
                        return length_new

                    elif board[y_length + d_y][x_length + d_x] != col:
                        length_not_col = length_new
                        return length_not_col

                    length_new += 1
                    y_length += d_y
                    x_length += d_x

            current_len = helper(board, col, y_start, x_start, d_y, d_x)

            if length_new == current_len:
                length_diff = length_new - 1
                sequence = is_bounded(board, y_start + (length_diff) * d_y, x_start + (length_diff) * d_x, length, d_y,
                                      d_x)
                if sequence == "SEMIOPEN":
                    semi_open_sequence_counter += 1
                    y_start += (length_diff) * d_y
                    x_start += (length_diff) * d_x
                elif sequence == "OPEN":
                    open_sequence_counter += 1
                    y_start += (length_diff) * d_y
                    x_start += (length_diff) * d_x

            elif length_new != current_len:  # if length != current_len
                y_start += (current_len - 1) * d_y
                x_start += (current_len - 1) * d_x

        x_start += d_x
        y_start += d_y

    return open_sequence_counter, semi_open_sequence_counter  # returns tuple


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    # d_y = 0, d_x = 1
    for rows in range(len(board)):
        num_tuples = detect_row(board, col, rows, 0, length, 0, 1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    # d_y = 1, d_x = 0
    for columns in range(len(board)):
        num_tuples = detect_row(board, col, 0, columns, length, 1, 0)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    # d_x == 1, d_y == 1
    for diagonals_y in range(len(board)):
        num_tuples = detect_row(board, col, diagonals_y, 0, length, 1, 1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    for diagonals_x in range(len(board)):
        num_tuples = detect_row(board, col, 0, diagonals_x, length, 1, 1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    # d_x = -1, d_y = 1
    for diagonals_y in range(len(board)):
        num_tuples = detect_row(board, col, diagonals_y, len(board) - 1, length, 1, -1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    for diagonals_x in range(len(board) - 1, -1, -1):
        num_tuples = detect_row(board, col, 0, diagonals_x, length, 1, -1)
        open_seq_count += num_tuples[0]
        semi_open_seq_count += num_tuples[1]

    return open_seq_count, semi_open_seq_count


def search_max(board):
    coordinates = ()
    max_score = -100000
    for row in range(len(board)):
        for column in range(len(board)):
            if row == 4 and column == 6:
                print("hi")
            if row == 2 and column == 7:
                print("Hi")
            if board[row][column] == " ":
                board[row][column] = "b"
                current_score = score(board)  # What is my current score when I put black here?
                print_board(board)
                print("current score:", score(board))
                print("max scoire", max_score)
                if current_score >= max_score:  # If my current is better than my max, save max as the current
                    max_score = current_score
                    coordinates = (row, column)
                board[row][column] = " "
            
            
            print(coordinates)
            
            
            # displays where to best place black piece
    return coordinates


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

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win_helper(board, col, y_start, x_start, length, d_y, d_x):
    current_len = 0
    length_new = length
    row_win = False

    for e in range(9):  # colour specific iteration by for loop
        if (y_start + d_y) > 8:
            return row_win
        elif (x_start + d_x) > 8:
            return row_win
        elif (y_start + d_y) < 0:
            return row_win
        elif (x_start + d_x) < 0:
            return row_win
        elif board[y_start][x_start] == col:  # if y_start or x_start is outside board parameters, end loop by returning
            y_length = y_start
            x_length = x_start
            length_new = 1

            if board[y_start][x_start] != col:
                length_new = 0

            for i in range(8):
                max1_list = []
                max1_list.append(y_length + d_y)
                max1_list.append(x_length + d_x)
                max1_list.sort()

                min2_list = []
                min2_list.append(y_length + d_y)
                min2_list.append(x_length + d_x)
                min2_list.sort()

                if max1_list[len(max1_list) - 1] >= len(board):
                    val = length_new
                    break

                if min2_list[0] < 0:
                    val = length_new
                    break

                if board[y_length + d_y][x_length + d_x] != col:
                    val = length_new
                    break

                length_new += 1
                y_length += d_y
                x_length += d_x
            current_len = val

            if length == current_len:
                row_win = True

            elif length != current_len:  # if length != current_len
                y_start += (current_len - 1) * d_y
                x_start += (current_len - 1) * d_x

        x_start += d_x
        y_start += d_y


def is_win(board):
    if detect_win1(board, 'b') == "Black won":
        return "Black won"
    elif detect_win1(board, 'w') == "White won":
        return "White won"
    elif no_more_spaces(board) == 1:
        return "Draw"
    else:
        return "Continue playing"


def no_more_spaces(board):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == " ":
                return 0
    return 1


def detect_win1(board, col):
    if col == 'b':
        for column in range(len(board)):
            for row in range(len(board)):
                for i in range(6, 9):
                    if is_win_helper(board, 'b', row, column, i, -1, 0):  # going down
                        return False
                    if is_win_helper(board, 'b', row, column, i, 1, 0):  # going up
                        return False
                    elif is_win_helper(board, 'b', row, column, i, 0, 1):  # going right
                        return False
                    elif is_win_helper(board, 'b', row, column, i, 0, -1):  # going left
                        return False
                    elif is_win_helper(board, 'b', row, column, i, 1, 1):  # going top right
                        return False
                    elif is_win_helper(board, 'b', row, column, i, -1, -1):  # going bottom left
                        return False
                    elif is_win_helper(board, 'b', row, column, i, 1, -1):  # going top left
                        return False
                    elif is_win_helper(board, 'b', row, column, i, -1, 1):  # going bottom right
                        return False

                if is_win_helper(board, 'b', row, column, 5, -1, 0):  # going down
                    return "Black won"
                if is_win_helper(board, 'b', row, column, 5, 1, 0):  # going up
                    return "Black won"
                elif is_win_helper(board, 'b', row, column, 5, 0, 1):  # going right
                    return "Black won"
                elif is_win_helper(board, 'b', row, column, 5, 0, -1):  # going left
                    return "Black won"
                elif is_win_helper(board, 'b', row, column, 5, 1, 1):  # going top right
                    return "Black won"
                elif is_win_helper(board, 'b', row, column, 5, -1, -1):  # going bottom left
                    return "Black won"
                elif is_win_helper(board, 'b', row, column, 5, 1, -1):  # going top left
                    return "Black won"
                elif is_win_helper(board, 'b', row, column, 5, -1, 1):  # going bottom right
                    return "Black won"
        return False
    elif col == 'w':
        for column in range(len(board)):
            for row in range(len(board)):
                for i in range(6, 9):
                    if is_win_helper(board, 'w', row, column, i, -1, 0):  # going down
                        return False
                    elif is_win_helper(board, 'w', row, column, i, 1, 0):  # going up
                        return False
                    elif is_win_helper(board, 'w', row, column, i, 0, 1):  # going right
                        return False
                    elif is_win_helper(board, 'w', row, column, i, 0, -1):  # going left
                        return False
                    elif is_win_helper(board, 'w', row, column, i, 1, 1):  # going top right
                        return False
                    elif is_win_helper(board, 'w', row, column, i, -1, -1):  # going bottom left
                        return False
                    elif is_win_helper(board, 'w', row, column, i, 1, -1):  # going top left
                        return False
                    elif is_win_helper(board, 'w', row, column, i, -1, 1):  # going bottom right
                        return False

                if is_win_helper(board, 'w', row, column, 5, -1, 0):  # going down
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, 1, 0):  # going up
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, 0, 1):  # going right
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, 0, -1):  # going left
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, 1, 1):  # going top right
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, -1, -1):  # going bottom left
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, 1, -1):  # going top left
                    return "White won"
                elif is_win_helper(board, 'w', row, column, 5, -1, 1):  # going bottom right
                    return "White won"
        return False

        # don't modify


def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])

        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


# don't modify
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


# don't modify
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


# don't modify
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3
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
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
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
    y = 5;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 3
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

    y = 3;
    x = 5;
    d_x = -1;
    d_y = 1;
    length = 2

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

    y = 5;
    x = 3;
    d_x = -1;
    d_y = 1;
    length = 1
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
    # play_gomoku(8)
    test_search_max()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()