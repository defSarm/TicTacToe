import random
from time import sleep
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def printBoard(board):
    for row in board:
        for slot in row:
            print(slot, end=" ")
        print()

def emptySpace(pos):
    if pos > 3 and pos <= 6 :
        if pos == 4:
            pos = 0
        elif pos == 5:
            pos = 1
        else:
            pos = 2
        return board[1][pos] == "-"
    elif pos >6 and pos <= 9:
        if pos == 7:
            pos = 0
        elif pos == 8:
            pos = 1
        else:
            pos = 2
        return board[2][pos] == "-"
    else:
        if pos == 1:
            pos = 0
        elif pos == 2:
            pos = 1
        else:
            pos = 2
        return board[0][pos] == "-"

def Win(le):
    return board[0][0] == le and board[0][1] == le and board[0][2] == le\
        or board[1][0] == le and board[1][1] == le and board[1][2] == le\
            or board[2][0] == le and board[2][1] == le and board[2][2] == le\
                or board[0][0] == le and board[1][0] == le and board[2][0] == le\
                    or board[0][1] == le and board[1][1] == le and board[2][1] == le\
                        or board[0][2] == le and board[1][2] == le and board[2][2] == le\
                            or board[0][0] == le and board[1][1] == le and board[2][2] == le\
                                or board[0][2] == le and board[1][1] == le and board[2][0] == le

def Tie(board):
    t = 0
    for l in board:
        c = l.count("-")
        t += c
    if t == 0 and not(Win("X") or Win("O")):
        return True
    else:
        return False

def playerMove(pos):
    if emptySpace(pos):
        if pos > 3 and pos <= 6 :
            if pos == 4:
                pos = 0
            elif pos == 5:
                pos = 1
            else:
                pos = 2
            board[1][pos] = "X"
        elif pos >6 and pos <= 9:
            if pos == 7:
                pos = 0
            elif pos == 8:
                pos = 1
            else:
                pos = 2
            board[2][pos] = "X"
        else:
            if pos == 1:
                pos = 0
            elif pos == 2:
                pos = 1
            else:
                pos = 2
            board[0][pos] = "X"

    else:
        return False

def player2Move(pos):
    if emptySpace(pos):
        if pos > 3 and pos <= 6 :
            if pos == 4:
                pos = 0
            elif pos == 5:
                pos = 1
            else:
                pos = 2
            board[1][pos] = "O"
        elif pos >6 and pos <= 9:
            if pos == 7:
                pos = 0
            elif pos == 8:
                pos = 1
            else:
                pos = 2
            board[2][pos] = "O"
        else:
            if pos == 1:
                pos = 0
            elif pos == 2:
                pos = 1
            else:
                pos = 2
            board[0][pos] = "O"

    else:
        return False

def AImove():
    pos = random.randint(1, 9)
    while not(emptySpace(pos)) and not(Tie(board)):
        pos = random.randint(1, 9)

    # Horizontal
    if board[0][0] == "X" and board[0][1] == "X" and emptySpace(3):
        board[0][2] = "O"
    elif board[0][1] == "X" and board[0][2] == "X" and emptySpace(1):
        board[0][0] = "O"
    elif board[0][0] == "X" and board[0][2] == "X" and emptySpace(2):
        board[0][1] = "O"

    elif board[1][0] == "X" and board[1][1] == "X" and emptySpace(3):
        board[1][2] = "O"
    elif board[1][1] == "X" and board[1][2] == "X" and emptySpace(1):
        board[1][0] = "O"
    elif board[1][0] == "X" and board[1][2] == "X" and emptySpace(2):
        board[1][1] = "O"

    elif board[2][0] == "X" and board[2][1] == "X" and emptySpace(3):
        board[2][2] = "O"
    elif board[2][1] == "X" and board[2][2] == "X" and emptySpace(1):
        board[2][0] = "O"
    elif board[2][0] == "X" and board[2][2] == "X" and emptySpace(2):
        board[2][1] = "O"

    # Vertical
    elif board[0][0] == "X" and board[1][0] == "X" and emptySpace(7):
        board[2][0] = "O"
    elif board[0][0] == "X" and board[2][0] == "X" and emptySpace(4):
        board[1][0] = "O"
    elif board[1][0] == "X" and board[2][0] == "X" and emptySpace(1):
        board[0][0] = "O"
    
    elif board[0][1] == "X" and board[1][1] == "X" and emptySpace(8):
        board[2][1] = "O"
    elif board[0][1] == "X" and board[2][1] == "X" and emptySpace(5):
        board[1][1] = "O"
    elif board[1][2] == "X" and board[2][1] == "X" and emptySpace(2):
        board[0][1] = "O"
    
    elif board[0][2] == "X" and board[1][2] == "X" and emptySpace(9):
        board[2][2] = "O"
    elif board[0][2] == "X" and board[2][2] == "X" and emptySpace(6):
        board[1][2] = "O"
    elif board[1][2] == "X" and board[2][2] == "X" and emptySpace(3):
        board[0][2] = "O"
    
    # Diagnally
    elif board[0][0] == "X" and board[1][1] == "X" and emptySpace(9):
        board[2][2] = "O"
    elif board[0][0] == "X" and board[2][2] == "X" and emptySpace(5):
        board[1][1] = "O"
    elif board[1][1] == "X" and board[2][2] == "X" and emptySpace(1):
        board[0][0] = "O"

    elif board[0][2] == "X" and board[1][1] == "X" and emptySpace(7):
        board[2][0] = "O"
    elif board[0][2] == "X" and board[2][0] == "X" and emptySpace(5):
        board[1][1] = "O"
    elif board[2][0] == "X" and board[1][1] == "X" and emptySpace(3):
        board[0][2] = "O"

    # Horizontal [AI]
    elif board[0][0] == "O" and board[0][1] == "O" and emptySpace(3):
        board[0][2] = "O"
    elif board[0][1] == "O" and board[0][2] == "O" and emptySpace(1):
        board[0][0] = "O"

    elif board[1][0] == "O" and board[1][1] == "O" and emptySpace(3):
        board[1][2] = "O"
    elif board[1][1] == "O" and board[1][2] == "O" and emptySpace(1):
        board[1][0] = "O"

    elif board[2][0] == "O" and board[2][1] == "O" and emptySpace(3):
        board[2][2] = "O"
    elif board[2][1] == "O" and board[2][2] == "O" and emptySpace(1):
        board[2][0] = "O"

    # Vertical [AI]
    elif board[0][0] == "O" and board[1][0] == "O" and emptySpace(7):
        board[2][0] = "O"
    elif board[0][0] == "O" and board[2][0] == "O" and emptySpace(4):
        board[1][0] = "O"
    elif board[1][0] == "O" and board[2][0] == "O" and emptySpace(1):
        board[0][0] = "O"
    
    elif board[0][1] == "O" and board[1][1] == "O" and emptySpace(8):
        board[2][1] = "O"
    elif board[0][1] == "O" and board[2][1] == "O" and emptySpace(5):
        board[1][1] = "O"
    elif board[1][2] == "O" and board[2][1] == "O" and emptySpace(2):
        board[0][1] = "O"
    
    elif board[0][2] == "O" and board[1][2] == "O" and emptySpace(9):
        board[2][2] = "O"
    elif board[0][2] == "O" and board[2][2] == "O" and emptySpace(6):
        board[1][2] = "O"
    elif board[1][2] == "O" and board[2][2] == "O" and emptySpace(3):
        board[0][2] = "O"
    
    # Diagnally [AI]
    elif board[0][0] == "O" and board[1][1] == "O" and emptySpace(9):
        board[2][2] = "O"
    elif board[0][0] == "O" and board[2][2] == "O" and emptySpace(5):
        board[1][1] = "O"
    elif board[1][1] == "O" and board[2][2] == "O" and emptySpace(1):
        board[0][0] = "O"

    elif board[0][2] == "O" and board[1][1] == "O" and emptySpace(7):
        board[2][0] = "O"
    elif board[0][2] == "O" and board[2][0] == "O" and emptySpace(5):
        board[1][1] = "O"
    elif board[2][0] == "O" and board[1][1] == "O" and emptySpace(3):
        board[0][2] = "O"

    else:
        if pos > 3 and pos <= 6 :
            if pos == 4:
                pos = 0
            elif pos == 5:
                pos = 1
            else:
                pos = 2
            board[1][pos] = "O"
        elif pos >6 and pos <= 9:
            if pos == 7:
                pos = 0
            elif pos == 8:
                pos = 1
            else:
                pos = 2
            board[2][pos] = "O"
        else:
            if pos == 1:
                pos = 0
            elif pos == 2:
                pos = 1
            else:
                pos = 2
            board[0][pos] = "O"

def AIgame():
    print("Welcome to Tic Tac Toe against in AI")
    while not(Win("X") or Win("O")):
        if Tie(board):
            print("Tie Game!")
            printBoard(board)
            break
        printBoard(board)
        try:
            user = int(input("Pick a slot between 1-9: "))
            if user < 1 or user > 9:
                print("Out of range")
                continue
            else:
                move = playerMove(user)
                if move == False:
                    print("That space is taken")
                elif Win("X"):
                    break

                else:
                    AImove()
                    

        except ValueError:
            print("Invalid input")
            continue

    if Win("X"):
        print("Player wins!")
        printBoard(board)
    elif Win("O"):
        print("Bot wins!")
        printBoard(board)
    else:
        print("Good game!")

def Multigame():
    global player1
    global player2
    player1 = True
    player2 = False
    print("Welcome to Tic Tac Toe MULTIPLAYER")
    while not(Win("X") or Win("O")):
        if Tie(board):
            print("Tie Game!")
            printBoard(board)
            break
        printBoard(board)
        try:
            if player1:
                user1 = int(input("Pick a slot between 1-9: "))
                if user1 > 9 or user1 < 1:
                    print("Out of range")
                    continue
                else:
                    move = playerMove(user1)
                    if move == False:
                        print("Space Taken")
                    else:   
                        player1 = False
                        player2 = True
                
            elif player2:
                user2 = int(input("Pick a slot between 1-9: "))
                if user2 > 9 or user2<1:
                    print("Out of range")
                    continue
                else:
                    move2 = player2Move(user2)
                    if move2 == False:
                        print("Space taken")
                    else:
                        player1 = True
                        player2 = False
                              

        except ValueError:
            print("Invalid input")
            continue

    if Win("X"):
            printBoard(board)
            print("X wins!")
        
    elif Win("O"):
        printBoard(board)
        print("O wins!")


        

var = ""
while len(var) == 0 or var != "single player" or var != "multiplayer":
    print("""
    Single Player ☐
    Multiplayer ☐
    Quit
    """)

    var = input("> ").lower()
    if var == "single player":
        print("""
        Single Player ☒
        Multiplayer ☐
        """)
        AIgame()
        break
    elif var == "multiplayer":
        print("""
        Single Player ☐
        Multiplayer ☒
        """)
        Multigame()
        break
    elif var == "quit":
        print("Goodbye")
        break
blank = input("> ")
