def init_board():
    board = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append('0')
        board.append(row)
    return board

board1 = init_board()
board2 = init_board()

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}


def menu():
    print ("""               ______________________________________________
                          .-'                     _                        '.
                        .'                       |-'                        |
                      .'                         |                          |
                   _.'               p         _\_/_         p              |
                _.'                  |       .'  |  '.       |              |
           __..'                     |      /    |    \      |              |
     ___..'                         .T\    ======+======    /T.             |
  ;;;\::::                        .' | \  /      |      \  / | '.           |
  ;;;|::::                      .'   |  \/       |       \/  |   '.         |
  ;;;/::::                    .'     |   \       |        \  |     '.       |
        ''.__               .'       |    \      |         \ |       '.     |
             ''._          <_________|_____>_____|__________>|_________>    |
                 '._     (___________|___________|___________|___________)  |
                    '.    \;;;;;;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   |
                      '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |
                        '. ~ ~ ~ ~ ~ ~ ~ ~ ~BATTLE SHIP~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
                          '-.______________________________________________.'""")


def ask_player_for_board_position():
    column = input("column (A to E):")
    while column.upper() not in "ABCDE":
        print("That column is wrong! It should be A, B, C, D or E")
        column = input("column (A to E):")

    row = input("row (1 to 5):")
    while row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")
        row = input("row (1 to 5):")

    return int(row) - 1, letters_to_numbers[column.upper()]


def init_player():
    try:
        player = int(input("Give me a number to see if you're player one or two: "))
        return player
    except:
        print("I asked you for a number and you gave me junk. Do it right this time.")
        return init_player()


def get_player(player):
    if (player % 2) == 1:
        player1 = 1
        return player1
    if (player % 2) == 0:
        player2 = 2
        return player2
    player += 1


def print_board(board1, board2, player):
    if player == 1:
        print ("Player One.")
        print("  A B C D E")
        print(" +-+-+-+-+-+")
        row_number1 = 1
        for row in board1:
            print("%d|%s|" % (row_number1, "|".join(row)))
            print(" +-+-+-+-+-+")
            row_number1 = row_number1 + 1        
    elif player == 2:
        print ("Player Two.")
        print("  A B C D E")
        print(" +-+-+-+-+-+")
        row_number2 = 1
        for row in board2:
            print("%d|%s|" % (row_number2, "|".join(row)))
            print(" +-+-+-+-+-+")
            row_number2 = row_number2 + 1
       

def place_ships_on_map(board):
    valid_coordinates = [0,1,2,3,4]
    for n in range(5):
        print(f"Where do you want to place ship no {n+1} ?")
        row_number, column_number = ask_player_for_board_position()
        if board[row_number][column_number] == "X":
            print('That spot is already taken!! Try again')
            row_number, column_number = ask_player_for_board_position()
        
        board[row_number][column_number] = 'X'
        print_board(board1, board2, get_player(init_player()))
        # todo create a function which prints only 1 map


# place_ships_on_map(board1)
# place_ships_on_map(board2)


# Now clear the screen, and the other player starts guessing
print("Now forget every ship the other one has")


def init_board_guessed():
    guesses_board = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append('0')
        guesses_board.append(row)
    return guesses_board

guesses_board1 = init_board_guessed()
guesses_board2 = init_board_guessed()

def shoot_at_map(board, guesses, player):
    print("Guess a battleship location")
    row_number, column_number = ask_player_for_board_position()
    if player % 2 == 1:
        print (guesses_board1)
    while board[row_number][column_number] == 'S':
        print("You already guessed this")
        row_number, column_number = ask_player_for_board_position()

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("HIT!")
        board[row_number][column_number] = 'S'
        guesses = guesses + 1
    else:
        board[row_number][column_number] = 'M'
        print("MISS!")
    return guesses
    # todo print only 1 board
    # print_board(board)


def win():
    guesses_player1 = 0
    guesses_player2 = 0
    game_turn = 0
    while guesses_player1 < 5 or guesses_player2 < 5:
        if game_turn % 2 == 0:
            guesses_player1 = shoot_at_map(board1, guesses_player1, init_player())
        else:
            guesses_player2 = shoot_at_map(board2, guesses_player2, init_player())
        game_turn += 1
    if guesses_player1 == 5:
        print("Player one wins!")
    elif guesses_player2 == 5:
        print("Player two wins!")


def playing_the_game(player):
    init_player
    place_ships_on_map(board1)
    place_ships_on_map(board2)
    if player == 1:
        print("It is now player one's turn!")
        print_board(board1, board2, get_player(init_player()))
    elif player == 2:
        print("It is now player two's turn!")
        print_board(board1, board2, get_player(init_player()))
        print(board1, board2)
    shoot_at_map(board1, win(), get_player(init_player()))
    shoot_at_map(board2, win(), get_player(init_player()))


playing_the_game(get_player(init_player()))