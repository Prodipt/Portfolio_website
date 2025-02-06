import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
winner= None
game_running = True


#printing the game board
def print_board(board):
    print(board[0]+ " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3]+ " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6]+ " | " + board[7] + " | " + board[8])


#take player input
def player_input(board):
    inp = int(input("Enter a number 1 to 9: "))
    if inp>=1 and inp<=9 and board[inp-1] =="-":
        board[inp-1] = current_player
    else:
        print("Oops player already in that spot")

#check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("Game is tied")
        game_running = False

def check_win():
    if check_diag(board) or check_horizontal(board) or check_vertical(board):
        print(f"The winner is {winner}") 

#switch the player
        
def switch_player():
    global current_player
    if current_player == "X":
        current_player= "O"
    else:
        current_player ="X"

#COMUPTER
def computer(board):
    while current_player == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switch_player()

#check the win or tie again
        
while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)