hash_states = {}
CROSS_CELL = 1
ROUND_CELL = -1
EMPTY_CELL = 0
BOARD_SIZE = 9
TUPLE_ORIGINAL = (EMPTY_CELL, EMPTY_CELL, EMPTY_CELL,
                  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL,
                  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL)
# TUPLE_ORIGINAL = (EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL)


def checkState(board):
    # win?
    # lines
    if board[0] == board[1] and board[0] == board[2] and board[0] != EMPTY_CELL:
        return board[0]
    if board[3] == board[4] and board[3] == board[5] and board[3] != EMPTY_CELL:
        return board[3]
    if board[6] == board[7] and board[6] == board[8] and board[6] != EMPTY_CELL:
        return board[6]
    # columns
    if board[0] == board[3] and board[0] == board[6] and board[0] != EMPTY_CELL:
        return board[0]
    if board[1] == board[4] and board[1] == board[7] and board[1] != EMPTY_CELL:
        return board[1]
    if board[2] == board[5] and board[2] == board[8] and board[2] != EMPTY_CELL:
        return board[2]
    # diagonals
    if board[0] == board[4] and board[0] == board[8] and board[0] != EMPTY_CELL:
        return board[0]
    if board[6] == board[4] and board[6] == board[2] and board[6] != EMPTY_CELL:
        return board[6]
    # draw?
    for i in range(BOARD_SIZE):
        if EMPTY_CELL:
            return None
    return EMPTY_CELL


def constructTree(board, is_cross=True):
    if board in hash_states:
        return
    state = checkState(board)
    if state:
        hash_states[board] = state
        return
    else:
        hash_states[board] = []
    for i, p in enumerate(board):
        if p != EMPTY_CELL:
            continue
        # Modification du tuple pour inscrire la case dans laquelle on joue
        child_board = list(board)
        child_board[i] = CROSS_CELL if is_cross else ROUND_CELL
        child_board = tuple(child_board)

        hash_states[board].append(child_board)
        constructTree(child_board, not is_cross)


# def calculate_value(root, board, is_cross=True):
#     for child in root.children:
#         x, y = root.x, root.y
#         board[y][x] = 'X' if is_cross else 'O'
#         calculate_value(child, board, not is_cross)
#         board[y][x] = ' '
#         # TODO COMPLETE


constructTree(TUPLE_ORIGINAL)
count = 0
for k, v in hash_states.items():
    count += 1

# calculate_value(root, BOARD_ORIGINAL)
print(hash_states)
print(count)
