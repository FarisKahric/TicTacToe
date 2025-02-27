import random  # Importing random module for PC's move selection

# Welcome message
print("Welcome to Tic Tac Toe!")
print("Rules:")
print("1. The game is played on a 3x3 grid.")
print("2. Two players take turns marking a square with 'X' or 'O'.")
print("3. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) wins!")
print("4. If all squares are filled and no player has three in a row, the game is a draw.")
print("5. Players can only mark an empty square on their turn.")
print("6. Have fun and may the best player win!")


# Initialize a 3x3 matrix (game board) filled with spaces
matrix = [[" " for _ in range(3)] for _ in range(3)]

# Display the initial empty board
for row in matrix:
    print(" | ".join(row))



# Prompt user to choose who plays first (1 = User, 2 = PC)
while True:
    try:
        choose_first = int(input("\nWho do you want to play first?\n"
                                 "1. You\n"
                                 "2. Me\n"
                                 "-> "))
        if choose_first in range(1, 3):
            break
        else:
            print("Please choose 1 or 2!")
    except ValueError:
        print("Invalid input!")



# Prompt user to choose their sign (X or O)
while True:
    try:
        input_sign = input("\nWho do you want to play as?\n"
                           "1. X\n"
                           "2. O\n"
                           "-> ").upper()
        if input_sign == "X" or input_sign == "O":
            break
        else:
            print("Please choose X or O!")
    except ValueError:
        print("Invalid input!")



# Assign signs to user and PC based on selection
pc_sign = ""
user_sign = ""

if input_sign == "X":
    user_sign = "X"
    pc_sign = "O"
else:
    user_sign = "O"
    pc_sign = "X"



# Function for PC to make a move
def pc_plays(sent_sign):
    while True:
        a = random.randint(1, 3)  # Random row selection
        b = random.randint(1, 3)  # Random column selection
        if matrix_input(a, b, sent_sign):  # Place sign if spot is free
            print("\nMy turn!")
            break

    # Print updated board
    for row in matrix:
        print(" | ".join(row))




# Function for User to make a move
def user_plays(sent_sign):
    while True:
        try:
            # Prompt user for row and column input
            a, b = map(int, input("\nYour turn! Input coordinates : ").split())
            if 1 <= a <= 3 and 1 <= b <= 3:
                if matrix_input(a, b, sent_sign):  # Place sign if spot is free
                    break
            else:
                print("Invalid coordinates! Enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input!")

    # Print updated board
    for row in matrix:
        print(" | ".join(row))




# Function to place a sign in the matrix (if space is available)
def matrix_input(a, b, sent_sign):
    if matrix[a - 1][b - 1] == " ":
        matrix[a - 1][b - 1] = sent_sign
        return True
    else:
        print("That place is already taken.")
        return False




# Function to check if there is a winner or a tie
def check_winner():
    # Check diagonals
    if (matrix[0][0] == matrix[1][1] == matrix[2][2] or
        matrix[2][0] == matrix[1][1] == matrix[0][2]) and matrix[1][1] != " ":
        who_wins(matrix[1][1])
        return True

    # Check rows
    for row in matrix:
        if len(set(row)) == 1 and row[0] != " ":
            who_wins(row[0])
            return True

    # Check columns
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != " ":
            who_wins(matrix[0][col])
            return True

    # Check for a tie (if no empty spaces left)
    if " " not in sum(matrix, []):
        print("\nIt's a tie!")
        return True

    return False  # No winner yet




# Function to announce the winner
def who_wins(sign):
    if sign == user_sign:
        print("\nCongratulations! You win.")
    else:
        print("\nI win! Better luck next time.")




# Determine whose turn it is first
user_next = False
pc_next = False
winner = False
if choose_first == 1:
    user_next = True  # User goes first
elif choose_first == 2:
    pc_next = True  # PC goes first



# Main game loop (runs until there is a winner or tie)
while not winner:
    while user_next:
        user_plays(user_sign)
        if check_winner():  # Check if user won
            winner = True
            break
        user_next = False
        pc_next = True  # PC's turn

    while pc_next:
        pc_plays(pc_sign)
        if check_winner():  # Check if PC won
            winner = True
            break
        pc_next = False
        user_next = True  # User's turn

# Game over message
print("Game Over! Thanks for playing. ")