import pprint

# get and parse input

# 3, 1, A, 3, C, 8, A
## ABCBCACAB

userInput = input("Enter an input: ").split(", ")

board = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: ""
}

for index, i in enumerate(userInput):
    if index == 0 or index %2 == 0: continue

    board[int(i)] = userInput[index+1]

# try to match the same letter diagonally

# 3, 5, 7
# 1, 5, 9

def checkIfDiagonalWorks(pos: int) -> (bool, [int]): # return str --> left or right
    # Top left to Bottom Right (TO Right)
    # Top Right to Bottom Left (TO Left)
    ## NOTE: 5 would be valid to both

    # use this only assuming in numbers: 1, 3, 5, 7, 9 - (range(1, 10, 2))

    global board

    a = []

    if pos == 1 or pos == 9:
        # TO Right
        print("TO Right")
        a = [1, 5, 9]
        a.remove(pos)

        if not checkIfValid(1) and not checkIfValid(5) and not checkIfValid(9):
            print("Diagonals not valid")

            return (False, None)

    elif pos == 3 or pos == 7:
        # TO Left
        print("TO Left")
        a = [3, 5, 7]
        a.remove(pos)

        if not checkIfValid(3) and not checkIfValid(5) and not checkIfValid(7):
            print("Diagonals not valid")
            print(checkIfValid(3))
            print(checkIfValid(5))
            print(checkIfValid(7))

            return (False, None)
    else:
        print("Both")
        # pos == 5
        ## Have to check both conditions

        a = [1, 3, 7, 9]

        if board[1] == "" and board[9] == "":
            return True, a
        elif board[3] == "" and board[7] == "":
            return True, a
        else: return (False, None)

        return board[1] == "" and board[3] == "" and board[7] == "" and board[9] == ""

    return (board[a[0]] == "" and board[a[1]] == "", a)

for i in range(1, 10, 2):
    if board[i] != "":
        print("---------------------------------------")
        print(f"Found Diagnoal Possibility: {board[i]}")

        # Top left to Bottom Right (TO Right)
        # Top Right to Bottom Left (TO Left)
        ## NOTE: 5 would be valid to both
        ## For now, i will exclude 5 from eval, but TODO: include 5 in evals in future

        diagonalWorks = checkIfDiagonalWorks(i)

        print(f"Diagonal Works? = {diagonalWorks[0]}")

        if diagonalWorks[0]:
            print(f"Filling in diagonal with {board[i]}")

            board[diagonalWorks[1][0]] = board[i]
            board[diagonalWorks[1][1]] = board[i]

            print("New Board: ")
            pprint.pprint(board)
            
            



"""
def checkIfValid(pos: int) -> bool:

    global board

    posLetter = board[pos]
    
    # in every case, check middle row

    if pos >= 4 and pos <= 6:
        print(f"pos at middle board row - checking both {pos}, {posLetter}")
        # return ((board[pos+1] == posLetter and board[pos+2] == posLetter) and (board[pos+3] == posLetter and board[pos+6] == posLetter) and (board[pos-1] == posLetter and board[pos-2] == posLetter) and (board[pos-3] == posLetter and board[pos-6] == posLetter))

        return (((board[pos+1] == posLetter and board[pos+2] == posLetter) and (board[pos+3] == posLetter and board[pos+6] == posLetter)) or ((board[pos+1] == "" and board[pos+2] == "") and (board[pos+3] == "" and board[pos+6] == ""))) or ((board[pos-1] == posLetter and board[pos-2] == posLetter) and (board[pos-3] == posLetter and board[pos-6] == posLetter)) or ((board[pos-1] == "" and board[pos-2] == "") and (board[pos-3] == "" and board[pos-6] == ""))
        
    if pos <= 3:
        print(f"top board row {pos}, {posLetter}")
        # return (board[pos+1] == posLetter and board[pos+2] == posLetter) and (board[pos+3] == posLetter and board[pos+6] == posLetter)

        print(((board[pos+1] == posLetter and board[pos+2] == posLetter) and (board[pos+3] == posLetter and board[pos+6] == posLetter)))
        print(((board[pos+1] == "" and board[pos+2] == "") and (board[pos+3] == "" and board[pos+6] == "")))

        return ((board[pos+1] == posLetter and board[pos+2] == posLetter) and (board[pos+3] == posLetter and board[pos+6] == posLetter)) or ((board[pos+1] == "" and board[pos+2] == "") and (board[pos+3] == "" and board[pos+6] == ""))
    
    print(f"bottom board row {pos}, {posLetter}")
    # return (board[pos-1] == posLetter and board[pos-2] == posLetter) and (board[pos-3] == posLetter and board[pos-6] == posLetter)

    return ((board[pos-1] == posLetter and board[pos-2] == posLetter) and (board[pos-3] == posLetter and board[pos-6] == posLetter)) or ((board[pos-1] == "" and board[pos-2] == "") and (board[pos-3] == "" and board[pos-6] == ""))
"""