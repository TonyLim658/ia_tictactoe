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


def update_tuple(tuple_to_update, index, val):
    tuple_updated = list(tuple_to_update)
    tuple_updated[index] = val
    tuple_updated = tuple(tuple_updated)
    return tuple_updated


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
        child_board = update_tuple(board, i, CROSS_CELL if is_cross else ROUND_CELL)

        tree[board].append(child_board)
        construct_tree(child_board, not is_cross)
        score = max(score, scores[child_board]) if is_cross else min(score, scores[child_board])
    scores[board] = score


def decision(board, bot_is_cross):
    val, child_board = -float('inf') if bot_is_cross else float('inf'), TUPLE_ORIGINAL
    for child in tree[board]:
        if bot_is_cross and val < scores[child] or not bot_is_cross and val > scores[child]:
            val = scores[child]
            child_board = child
    diff = 0
    while diff < BOARD_SIZE and child_board[diff] == board[diff]:
        diff += 1
    return diff


test()
construct_tree(TUPLE_ORIGINAL)
'''count = 0
for k, v in scores.items():
    count += 1
# print(tree)
print(scores)
print(count)'''

###### PARTIE JEU ############
gameBoard = [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL,
             EMPTY_CELL, EMPTY_CELL, EMPTY_CELL,
             EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]


def transformCell(typeCell):
    if typeCell == CROSS_CELL:
        return 'X'
    elif typeCell == ROUND_CELL:
        return 'O'
    else:
        return ' '


def gameView():
    print('-----------')
    print(' ' + transformCell(gameBoard[0]) + ' | ' + transformCell(gameBoard[1]) + ' | ' + transformCell(gameBoard[2]))
    print('---+---+---')
    print(' ' + transformCell(gameBoard[3]) + ' | ' + transformCell(gameBoard[4]) + ' | ' + transformCell(gameBoard[5]))
    print('---+---+---')
    print(' ' + transformCell(gameBoard[6]) + ' | ' + transformCell(gameBoard[7]) + ' | ' + transformCell(gameBoard[8]))
    print('-----------')


def isPositionable(position):
    if gameBoard[position] == EMPTY_CELL:
        return True
    else:
        return False


def endOfTheGame(state):
    if state == 0:
        print("Draw. Play again!")
    elif state == -1:
        print("Circle player win the game !")
    else:
        print("Cross player win the game !")
    exit(0)


def gameplayUpdate(typeCell, position):
    if isPositionable(position):
        gameBoard[position] = typeCell
        gameView()
        state = check_state(gameBoard)
        if type(state) == int:
            endOfTheGame(state)
        return

    else:
        print("This cell is already taken")
        position = int(input("Enter new position [1-9] : ")) - 1
        gameplayUpdate(typeCell, position)
        return


def playerTurn(cellType):
    position = int(input("Enter a position [1-9] : ")) - 1
    gameplayUpdate(cellType, position)
    return


def botTurn(isFirst, cellType):
    position = decision(tuple(gameBoard), isFirst)
    print("Le bot choisi la position : " + str(position + 1))
    gameplayUpdate(cellType, position)
    return


def askForBegin():
    ans = input("Do you want to start? (y/n) : ")
    if ans == "y":
        return False
    elif ans == "n":
        return True
    else:
        return askForBegin()


##### LANCEMENT DU JEU ####
botStart = askForBegin()
if botStart:
    while check_state(gameBoard) != int:
        botTurn(True, CROSS_CELL)
        playerTurn(ROUND_CELL)
else:
    while check_state(gameBoard) != int:
        playerTurn(CROSS_CELL)
        botTurn(False, ROUND_CELL)
