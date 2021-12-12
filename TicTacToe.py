def display_board(board):
    """Display the board

    Args:
        board ([list]): [stores the board to be displayed and later dispalys it.]
    """
    print("-------------------")
    print("|  "  " " + "  |" + " "  " " + "   |" + " "  " " + "   |")
    print("|  " + board[1]+ "  |" + "  " + board[2]+ "  |" + "  " + board[3]+ "  |")
    print("|  "  " " + "  |" + " "  " " + "   |" + " "  " " + "   |")
    print("-------------------")
    print("|  "  " " + "  |" + " "  " " + "   |" + " "  " " + "   |")
    print("|  " + board[4]+ "  |" + "  " + board[5]+ "  |" + "  " + board[6]+ "  |")
    print("|  "  " " + "  |" + " "  " " + "   |" + " "  " " + "   |")
    print("-------------------")
    print("|  "  " " + "  |" + " "  " " + "   |" + " "  " " + "   |")
    print("|  " + board[7]+ "  |" + "  " + board[8]+ "  |" + "  " + board[9]+ "  |")
    print("|  "  " " + "  |" + " "  " " + "   |" + " "  " " + "   |")
    print("-------------------")

def player_input():
    """Takes choice for markers from the respective players

    Returns:
        [tuple]: [stores markers for players A and B]
    """
    marker_A = input("Player A - which marker you want, X or O :- ")
    print("_______________________________________________________\n")

    while (marker_A != 'X' and marker_A != 'O'):
        print("Invalid marker. Please choose a valid marker. (Note: Both X and O are capital letters.)")
        marker_A = input("Player A - which marker you want, X or O :- ")
        print("_______________________________________________________\n")

    if marker_A == 'O' or marker_A == 'o':
        marker_B = 'X'
    else:
        marker_B = 'O'
    return (marker_A, marker_B)

def place_marker(board, marker, position):
    """Update the board with the given marker

    Args:
        board ([list]): [stores respective markers of players at the given position]
        marker ([str]): [stores X or O]
        position ([int]): [stores the position where the marker is to be inserted]

    Returns:
        [list]: [updated board]
    """
    board[position] = marker
    return board

def start_greet():
    """Greets the players when the game starts
    """
    print('\nWelcome to Tic Tac Toe!')
    print("-----------------------------------------")
    print('                GAME STARTS')
    print("-----------------------------------------")
    print("GAME KEY : ")
    key_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(key_board)

def end_greet():
    """Greets the winner of TicTacToe 
    """
    print("----------------------------------------------")
    print('|  Congratulations! You have won the game!   |')
    print("----------------------------------------------")

def player_choice(k, mA, mB):
    """Prompts user to enter the position where the marker is to be updated

    Args:
        k ([int]): [counter]
        mA ([str]): [stores the marker of player A]
        mB ([str]): [stores the marker of player B]

    Returns:
        [int]: [returns the position which user entered]
    """
    pos = 0
    while pos > 9 or pos < 1:
            if k % 2 == 0:
                print(f"Player A - {mA}")
            else:
                print(f"Player B - {mB}")

            p = input("Choose your next position: (1-9) :- ")
            pos = int(p)
    return pos

def space_check(user_choice, x):
    """Checks whether the position entered by the player is occupied

    Args:
        user_choice ([list]): [stores all the positions entered by the player]
        x ([int]): [current position of the player]

    Returns:
        [boolean]: [True if position occupied by the player and false otherwise]
    """
    if x in user_choice:
        return True
    return False

def win_check(board,mark):
    """Checks the condition for a win

    Args:
        board ([list]): [contains all the respective markers of both players]
        mark ([str]): [marker thst is being checked for the win condition]

    Returns:
        [boolean]: [True if win and False otherwise]
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def full_board(board):
    """Checks whether the board is completely full which helps in checking for a TIE

    Args:
        board ([list]): [contains all the respective markers of both players]

    Returns:
        [boolean]: [True if board is completely filled, False otherwise]
    """
    c = 0
    for element in board:
        if element == 'X' or element == 'O':
            c += 1
    if c == 9:
        return True
    return False

def main():
    """This is the main function where all the functions are called and the program majorly excecutes
    """
    start_greet()

    user_input = []
    test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    final_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    posn = 0
    
    (mark_A, mark_B) = player_input()

    for i in range(0, 9, 1):
        posn = 0
        
        posn = player_choice(i, mark_A, mark_B)
        
        if space_check(user_input, posn) == True:
            print("This place is already occupied. Please re-enter a new position.\n")
            posn = player_choice(i, mark_A, mark_B)
        # update the board
        if i % 2 == 0:
            final_board = place_marker(test_board, mark_A, posn)
            
            result = win_check(final_board, mark_A)
            if result == True:
                display_board(final_board)
                print("_______________________________________________________")
                print('            Player A is the WINNER!')
                print("_______________________________________________________\n")
                end_greet()
                # Ask user whether he wishes to replay the game
                restart = input("\nDo you want to play again? Enter Yes or No: \nDecision :- ")
                if (restart == 'y' or restart == 'yes' or restart == 'Yes' or restart == 'YES'):
                    main()
                else:
                    print("\nGAME OVER")
                break
        else:
            final_board = place_marker(test_board, mark_B, posn)
            result = win_check(final_board, mark_B)
            
            if result == True:
                display_board(final_board)
                print("_______________________________________________________")
                print("            Player B is the WINNER!")
                print("_______________________________________________________\n")
                end_greet()
                 # Ask user whether he wishes to replay the game
                restart = input("\nDo you want to play again? Enter Yes or No: \nDecision :- ")
                if (restart == 'y' or restart == 'yes' or restart == 'Yes' or restart == 'YES'):
                    main()
                else:
                    print("\nGAME OVER")
                break
        user_input.append(posn)
        if full_board(final_board) == True:
            display_board(final_board)
            print("_______________________________________________________")
            print("       There is a TIE between the two players")
            print("_______________________________________________________\n")
             # Ask user whether he wishes to replay the game
            restart = input("\nDo you want to play again? Enter Yes or No: \nDecision :- ")
            if (restart == 'y' or restart == 'yes' or restart == 'Yes' or restart == 'YES'):
                main()
            else:
                 print("\nGAME OVER")
            break
        
        display_board(final_board)
        print("_______________________________________________________")
        print("_______________________________________________________\n")

main()
