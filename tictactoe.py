tree = {}  # tuple: [tuple] | int
scores = {}  # tuple: int
CROSS_CELL = 1
ROUND_CELL = -1
EMPTY_CELL = 0
BOARD_SIZE = 9
TUPLE_ORIGINAL = (EMPTY_CELL, EMPTY_CELL, EMPTY_CELL,
                  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL,
                  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL)


def test():
    assert (check_state(TUPLE_ORIGINAL) is None)
    assert (check_state((1, -1, 1, -1, 1, -1, 1, 1, -1)) == 1)


def check_state(board):
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
        if EMPTY_CELL == board[i]:
            return None
    return EMPTY_CELL


def construct_tree(board, is_cross=True):
    if board in tree:
        return
    state = check_state(board)
    if type(state) == int:
        tree[board] = state
        scores[board] = state
        return
    else:
        tree[board] = []
    score = -float('inf') if is_cross else float('inf')
    for i, p in enumerate(board):
        # Au niveau de la lecture on tombe une case prise
        if p != EMPTY_CELL:
            continue
        # Modification du tuple pour inscrire la case dans laquelle on joue
        child_board = list(board)
        child_board[i] = CROSS_CELL if is_cross else ROUND_CELL
        child_board = tuple(child_board)

        tree[board].append(child_board)
        construct_tree(child_board, not is_cross)
        score = max(score, scores[child_board]) if is_cross else min(score, scores[child_board])
    scores[board] = score


test()
construct_tree(TUPLE_ORIGINAL)
count = 0
for k, v in scores.items():
    count += 1
# print(tree)
print(scores)
print(count)
