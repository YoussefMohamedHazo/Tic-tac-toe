import random
from collections import deque


board = [' ' for _ in range(9)]


winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]


def bfs_move(board):
    queue = deque([(board, -1)])  
    visited = set()

    while queue:
        state, last_move = queue.popleft()
        visited.add(tuple(state))

        if is_game_over(state):
            return last_move

        for i, cell in enumerate(state):
            if cell == ' ':
                new_state = list(state)
                new_state[i] = 'O'
                if tuple(new_state) not in visited:
                    queue.append((new_state, i))


def is_winner(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw(board):
    return ' ' not in board


def is_game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_draw(board)


def display_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('---------')


def get_user_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move >= 0 and move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")


def play_game():
    print("Welcome to Tic Tac Toe!")

    while True:
        opponent = input("Choose your opponent (AI/Player): ").lower()
        if opponent == 'ai' or opponent == 'player':
            break
        else:
            print("Invalid opponent. Try again.")

    display_board(list(range(1, 10)))

    while not is_game_over(board):
        if opponent == 'player':
            move = get_user_move()
            board[move] = 'X'
        else:
            move = bfs_move(board)
            board[move] = 'O'
            print("AI's move: ", move + 1)

        display_board(board)

    if is_winner(board, 'X'):
        print("Congratulations! You win!")
    elif is_winner(board, 'O'):
        print("AI wins! Better luck next time!")
    else:
        print("It's a draw!")


play_game()
