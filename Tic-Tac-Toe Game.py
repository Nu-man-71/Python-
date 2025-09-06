# Simple Tic-Tac-Toe Game
board = [' '] * 9
player = 'X'

def show_board():
    print(f'\n {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} \n')

def check_win():
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != ' ':
            return True
    return False

print("Tic-Tac-Toe! Positions 1-9:")
print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 \n")

for turn in range(9):
    show_board()
    
    # Get move
    while True:
        try:
            move = int(input(f"Player {player}, pick 1-9: ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("Taken! Try again.")
        except:
            print("Enter 1-9!")
    
    # Check winner
    if check_win():
        show_board()
        print(f"Player {player} wins! ")
        break
    
    # Switch player
    player = 'O' if player == 'X' else 'X'
else:
    show_board()
    print("It's a tie!")