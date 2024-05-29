# Initialize the board
def initializeBoard():
    return {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

# Print the board


def printBoard(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Check for a win


def checkWhoWin(board, player):
    win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),
                        (1, 5, 9), (3, 5, 7)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check for a draw


def checkForDraw(board):
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

# Insert value into the board


def insertValue(board, position, value):
    board[position] = value

# Minimax algorithm


def minimax(board, isMaximizing, computer, player):
    if checkWhoWin(board, computer):
        return 1
    elif checkWhoWin(board, player):
        return -1
    elif checkForDraw(board):
        return 0

    if isMaximizing:
        bestScore = -100
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False, computer, player)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True, computer, player)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

# Computer move


def computerMove(board, computer, player):
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False, computer, player)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertValue(board, bestMove, computer)

# Main game loop


def main():
    board = initializeBoard()
    player = 'O'
    computer = 'X'
    print("Tic-Tac-Toe: You are O and computer is X")
    printBoard(board)

    while True:
        # Player move
        move = int(input("Enter your move (1-9): "))
        if board[move] == ' ':
            insertValue(board, move, player)
            if checkWhoWin(board, player):
                printBoard(board)
                print("Congratulations! You win!")
                break
            elif checkForDraw(board):
                printBoard(board)
                print("It's a draw!")
                break

            # Computer move
            computerMove(board, computer, player)
            if checkWhoWin(board, computer):
                printBoard(board)
                print("Computer wins!")
                break
            elif checkForDraw(board):
                printBoard(board)
                print("It's a draw!")
                break

            printBoard(board)
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()
