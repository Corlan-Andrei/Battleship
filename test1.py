letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}

player = 0
def init_player():
    global player
    try:
        player = int(input("Give me a number to see if you're player one or two: "))
        if player % 2 == 1:
            player = 1
        elif player % 2 == 0:
            player = 2
        return player
    except:
        print("I asked you for a number and you gave me junk. Do it right this time.")
        return init_player()


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

    init_player()


def init_board(z):
    board = []
    for i in range(z):
        row = []
        for j in range(z):
            row.append('0')
        board.append(row)
    return board

board1 = init_board(5)
board2 = init_board(5)

def print_board():
    global player
    global board1
    global board2
    if player == 1:
        print("  A B C D E")
        print(" +-+-+-+-+-+")
        row_number1 = 1
        for row in board1:
            print("%d|%s|" % (row_number1, "|".join(row)))
            print(" +-+-+-+-+-+")
            row_number1 = row_number1 + 1        
        place_ships_on_map()
    elif player == 2:
        print("  A B C D E")
        print(" +-+-+-+-+-+")
        row_number2 = 1
        for row in board2:
            print("%d|%s|" % (row_number2, "|".join(row)))
            print(" +-+-+-+-+-+")
            row_number2 = row_number2 + 1
        place_ships_on_map()

def place_ships_on_map():
    global board1, board2
    if player == 1:
        for n in range(5):
            print("Where do you want to place your ship?")
            row_number1, column_number1 = ask_player_for_board_position()
            board1[row_number1][column_number1] = 'X'
            print_board()
            if board1[row_number1][column_number1] == "X":
                print('That spot is already taken!! Try again')
                row_number1, column_number1 = ask_player_for_board_position()
    elif player == 2:
        for n in range(5):
            print("Where do you want to place your ship?")
            row_number2, column_number2 = ask_player_for_board_position()
            board2[row_number2][column_number2] = 'X'
            print_board()
            if board2[row_number2][column_number2] == "X":
                print('That spot is already taken!! Try again')
                row_number2, column_number2 = ask_player_for_board_position()



def ask_player_for_board_position():
    global player
    if player == 1:
        column1 = input("column (A to E):")
        while column1.upper() not in "ABCDE":
            print("That column is wrong! It should be A, B, C, D or E")
            column1 = input("column (A to E):")
        row1 = input("row (1 to 5):")
        while row1 not in "12345":
            print("That row is wrong! it should be 1, 2, 3, 4 or 5")
            row1 = input("row (1 to 5):")
            place_ships_on_map()
        return int(row1) - 1, letters_to_numbers[column1.upper()]
    elif player == 2:
        column2 = input("column (A to E):")
        while column2.upper() not in "ABCDE":
            print("That column is wrong! It should be A, B, C, D or E")
            column2 = input("column (A to E):")
        row2 = input("row (1 to 5):")
        while row2 not in "12345":
            print("That row is wrong! it should be 1, 2, 3, 4 or 5")
            row2 = input("row (1 to 5):")
            place_ships_on_map()
        return int(row2) - 1, letters_to_numbers[column2.upper()]
    else:
        return init_player()


def init_board_guessed(t):
    guesses_board = []
    for i in range(t):
        row = []
        for j in range(t):
            row.append('0')
        guesses_board.append(row)
    return guesses_board

guesses_board1 = init_board_guessed(5)
guesses_board2 = init_board_guessed(5)


guesses_player1 = 0
guesses_player2 = 0
def shoot_at_map():
    global player
    board = print_board()
    if player == 1:
        print("Guess a battleship location")
        row_number1, column_number1 = ask_player_for_board_position()
        if board2[row_number2][column_number2] == 'S':
            print("You already guessed this")
            return row_number1, column_number1 = ask_player_for_board_position()

        elif board2[row_number2][column_number2] == 'X':
            print("HIT!")
            board2[row_number2][column_number2] = 'S'
            guesses_player1 = guesses_player1 + 1
            player = player + 1
            return guesses_player1, player
        else:
            board[row_number][column_number] = 'M'
            print("MISS!")
            player = player +1
            return player

    elif player == 2:
        print("Guess a battleship location")
        row_number2, column_number2 = ask_player_for_board_position()

        if board1[row_number1][column_number1] == 'S':
            print("You already guessed this")
            row_number2, column_number2 = ask_player_for_board_position()

        elif board1[row_number1][column_number1] == 'X':
            print("HIT!")
            board1[row_number1][column_number1] = 'S'
            guesses_player2 = guesses_player2 + 1
            print_board()
            player = player + 1
            return guesses_player2, player
        else:
            board[row_number][column_number] = 'M'
            print("MISS!")
    if guesses_player1 == 5:
        print("Player one wins!")
    elif guesses_player2 == 5:
        print("Player two wins!")

def play():
    global player
    menu()
    init_board(5)
    init_board_guessed()
    shoot_at_map()

play()