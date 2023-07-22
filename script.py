# flag : flag{wh04m1_15_pr0ud_0f_y0u}


import subprocess
import numpy as np
import random


# Define a function to handle interactive communication
def interact_with_executable():
    executable_path = './minesweeper'

    # Start the process and create pipes for communication
    process = subprocess.Popen(
        executable_path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    while True:
        # Wait for the executable to output some data
        output = []
        lost = False
        for i in range(10):
            output_line = process.stdout.readline().strip()
            
            if (output_line[0] == "G"):
                output_line = process.stdout.readline().strip()
            if (output_line[0] == "Y"):
                lost = True
            
            if ("flag" in output_line):
                print(output_line)

            output.append(output_line)
            
        if (lost):
            break
        
        # Process the output to decide the next input
        next_input = process_output_and_get_input(output)

        if (next_input == "break"):
            break
        
        # Send the next input to the executable
        process.stdin.write(next_input + '\n')
        process.stdin.flush()

    # Close the standard input of the process
    process.stdin.close()


# i --> row  |  j --> column
def output_to_array(output):
    gamestate = np.full((9,9), -1, dtype=int)
    
    for i in range(9):
        for j in range(17):
            
            if (j%2 == 0):
                char = output[i][j]
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
                    
                    gamestate[i][int(j/2)] = char
    
    return gamestate


# ## Gamestate array scheme
# 
# - -1 --> Unknown
# - -2 --> Mine
# - 0 to 8 --> Number of adjacent mines


# Sorry for the messy structure

# Returns an int
def adjacent_unknowns(gamestate, i, j):
    count = 0
    if (i == 0):
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                count += 1
            if (gamestate[i+1][j+1] == -1):
                count += 1
            if (gamestate[i+1][j] == -1):
                count += 1
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                count += 1
            if (gamestate[i+1][j-1] == -1):
                count += 1
            if (gamestate[i+1][j] == -1):
                count += 1
        else:
            if (gamestate[i][j-1] == -1):
                count += 1
            if (gamestate[i+1][j-1] == -1):
                count += 1
            if (gamestate[i+1][j] == -1):
                count += 1
            if (gamestate[i+1][j+1] == -1):
                count += 1
            if (gamestate[i][j+1] == -1):
                count += 1
    elif (i == 8):
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                count += 1
            if (gamestate[i-1][j+1] == -1):
                count += 1
            if (gamestate[i-1][j] == -1):
                count += 1
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                count += 1
            if (gamestate[i-1][j-1] == -1):
                count += 1
            if (gamestate[i-1][j] == -1):
                count += 1
        else:
            if (gamestate[i][j-1] == -1):
                count += 1
            if (gamestate[i-1][j-1] == -1):
                count += 1
            if (gamestate[i-1][j] == -1):
                count += 1
            if (gamestate[i-1][j+1] == -1):
                count += 1
            if (gamestate[i][j+1] == -1):
                count += 1
    else:
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                count += 1
            if (gamestate[i+1][j+1] == -1):
                count += 1
            if (gamestate[i+1][j] == -1):
                count += 1
            if (gamestate[i-1][j+1] == -1):
                count += 1
            if (gamestate[i-1][j] == -1):
                count += 1
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                count += 1
            if (gamestate[i+1][j-1] == -1):
                count += 1
            if (gamestate[i+1][j] == -1):
                count += 1
            if (gamestate[i-1][j-1] == -1):
                count += 1
            if (gamestate[i-1][j] == -1):
                count += 1
        else:
            if (gamestate[i][j-1] == -1):
                count += 1
            if (gamestate[i+1][j-1] == -1):
                count += 1
            if (gamestate[i+1][j] == -1):
                count += 1
            if (gamestate[i+1][j+1] == -1):
                count += 1
            if (gamestate[i-1][j-1] == -1):
                count += 1
            if (gamestate[i-1][j] == -1):
                count += 1
            if (gamestate[i-1][j+1] == -1):
                count += 1
            if (gamestate[i][j+1] == -1):
                count += 1
                
    return (count)


# Returns an int
def adjacent_mines(gamestate, i, j):
    count = 0
    if (i == 0):
        if (j == 0):
            if (gamestate[i][j+1] == -2):
                count += 1
            if (gamestate[i+1][j+1] == -2):
                count += 1
            if (gamestate[i+1][j] == -2):
                count += 1
        elif (j == 8):
            if (gamestate[i][j-1] == -2):
                count += 1
            if (gamestate[i+1][j-1] == -2):
                count += 1
            if (gamestate[i+1][j] == -2):
                count += 1
        else:
            if (gamestate[i][j-1] == -2):
                count += 1
            if (gamestate[i+1][j-1] == -2):
                count += 1
            if (gamestate[i+1][j] == -2):
                count += 1
            if (gamestate[i+1][j+1] == -2):
                count += 1
            if (gamestate[i][j+1] == -2):
                count += 1
    elif (i == 8):
        if (j == 0):
            if (gamestate[i][j+1] == -2):
                count += 1
            if (gamestate[i-1][j+1] == -2):
                count += 1
            if (gamestate[i-1][j] == -2):
                count += 1
        elif (j == 8):
            if (gamestate[i][j-1] == -2):
                count += 1
            if (gamestate[i-1][j-1] == -2):
                count += 1
            if (gamestate[i-1][j] == -2):
                count += 1
        else:
            if (gamestate[i][j-1] == -2):
                count += 1
            if (gamestate[i-1][j-1] == -2):
                count += 1
            if (gamestate[i-1][j] == -2):
                count += 1
            if (gamestate[i-1][j+1] == -2):
                count += 1
            if (gamestate[i][j+1] == -2):
                count += 1
    else:
        if (j == 0):
            if (gamestate[i][j+1] == -2):
                count += 1
            if (gamestate[i+1][j+1] == -2):
                count += 1
            if (gamestate[i+1][j] == -2):
                count += 1
            if (gamestate[i-1][j+1] == -2):
                count += 1
            if (gamestate[i-1][j] == -2):
                count += 1
        elif (j == 8):
            if (gamestate[i][j-1] == -2):
                count += 1
            if (gamestate[i+1][j-1] == -2):
                count += 1
            if (gamestate[i+1][j] == -2):
                count += 1
            if (gamestate[i-1][j-1] == -2):
                count += 1
            if (gamestate[i-1][j] == -2):
                count += 1
        else:
            if (gamestate[i][j-1] == -2):
                count += 1
            if (gamestate[i+1][j-1] == -2):
                count += 1
            if (gamestate[i+1][j] == -2):
                count += 1
            if (gamestate[i+1][j+1] == -2):
                count += 1
            if (gamestate[i-1][j-1] == -2):
                count += 1
            if (gamestate[i-1][j] == -2):
                count += 1
            if (gamestate[i-1][j+1] == -2):
                count += 1
            if (gamestate[i][j+1] == -2):
                count += 1
                
    return (count)


def mark_mines(gamestate, i, j):
    # Using the same base structure as adjacent_unknowns
    
    if (i == 0):
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                gamestate[i][j+1] = -2
            if (gamestate[i+1][j+1] == -1):
                gamestate[i+1][j+1] = -2
            if (gamestate[i+1][j] == -1):
                gamestate[i+1][j] = -2
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                gamestate[i][j-1] = -2
            if (gamestate[i+1][j-1] == -1):
                gamestate[i+1][j-1] = -2
            if (gamestate[i+1][j] == -1):
                gamestate[i+1][j] = -2
        else:
            if (gamestate[i][j-1] == -1):
                gamestate[i][j-1] = -2
            if (gamestate[i+1][j-1] == -1):
                gamestate[i+1][j-1] = -2
            if (gamestate[i+1][j] == -1):
                gamestate[i+1][j] = -2
            if (gamestate[i+1][j+1] == -1):
                gamestate[i+1][j+1] = -2
            if (gamestate[i][j+1] == -1):
                gamestate[i][j+1] = -2
    elif (i == 8):
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                gamestate[i][j+1] = -2
            if (gamestate[i-1][j+1] == -1):
                gamestate[i-1][j+1] = -2
            if (gamestate[i-1][j] == -1):
                gamestate[i-1][j] = -2
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                gamestate[i][j-1] = -2
            if (gamestate[i-1][j-1] == -1):
                gamestate[i-1][j-1] = -2
            if (gamestate[i-1][j] == -1):
                gamestate[i-1][j] = -2
        else:
            if (gamestate[i][j-1] == -1):
                gamestate[i][j-1] = -2
            if (gamestate[i-1][j-1] == -1):
                gamestate[i-1][j-1] = -2
            if (gamestate[i-1][j] == -1):
                gamestate[i-1][j] = -2
            if (gamestate[i-1][j+1] == -1):
                gamestate[i-1][j+1] = -2
            if (gamestate[i][j+1] == -1):
                gamestate[i][j+1] = -2
    else:
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                gamestate[i][j+1] = -2
            if (gamestate[i+1][j+1] == -1):
                gamestate[i+1][j+1] = -2
            if (gamestate[i+1][j] == -1):
                gamestate[i+1][j] = -2
            if (gamestate[i-1][j+1] == -1):
                gamestate[i-1][j+1] = -2
            if (gamestate[i-1][j] == -1):
                gamestate[i-1][j] = -2
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                gamestate[i][j-1] = -2
            if (gamestate[i+1][j-1] == -1):
                gamestate[i+1][j-1] = -2
            if (gamestate[i+1][j] == -1):
                gamestate[i+1][j] = -2
            if (gamestate[i-1][j-1] == -1):
                gamestate[i-1][j-1] = -2
            if (gamestate[i-1][j] == -1):
                gamestate[i-1][j] = -2
        else:
            if (gamestate[i][j-1] == -1):
                gamestate[i][j-1] = -2
            if (gamestate[i+1][j-1] == -1):
                gamestate[i+1][j-1] = -2
            if (gamestate[i+1][j] == -1):
                gamestate[i+1][j] = -2
            if (gamestate[i+1][j+1] == -1):
                gamestate[i+1][j+1] = -2
            if (gamestate[i-1][j-1] == -1):
                gamestate[i-1][j-1] = -2
            if (gamestate[i-1][j] == -1):
                gamestate[i-1][j] = -2
            if (gamestate[i-1][j+1] == -1):
                gamestate[i-1][j+1] = -2
            if (gamestate[i][j+1] == -1):
                gamestate[i][j+1] = -2


# Returns tuple (i,j)
def find_adjacent_unknown(gamestate, i, j):
    if (i == 0):
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                return  ((i, j+1))
            if (gamestate[i+1][j+1] == -1):
                return  ((i+1, j+1))
            if (gamestate[i+1][j] == -1):
                return  ((i+1, j))
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                return  ((i, j-1))
            if (gamestate[i+1][j-1] == -1):
                return  ((i+1, j-1))
            if (gamestate[i+1][j] == -1):
                return  ((i+1, j))
        else:
            if (gamestate[i][j-1] == -1):
                return  ((i, j-1))
            if (gamestate[i+1][j-1] == -1):
                return  ((i+1, j-1))
            if (gamestate[i+1][j] == -1):
                return  ((i+1, j))
            if (gamestate[i+1][j+1] == -1):
                return  ((i+1, j+1))
            if (gamestate[i][j+1] == -1):
                return  ((i, j+1))
    elif (i == 8):
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                return  ((i, j+1))
            if (gamestate[i-1][j+1] == -1):
                return  ((i-1, j+1))
            if (gamestate[i-1][j] == -1):
                return  ((i-1, j))
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                return  ((i, j-1))
            if (gamestate[i-1][j-1] == -1):
                return  ((i-1, j-1))
            if (gamestate[i-1][j] == -1):
                return  ((i-1, j))
        else:
            if (gamestate[i][j-1] == -1):
                return  ((i, j-1))
            if (gamestate[i-1][j-1] == -1):
                return  ((i-1, j-1))
            if (gamestate[i-1][j] == -1):
                return  ((i-1, j))
            if (gamestate[i-1][j+1] == -1):
                return  ((i-1, j+1))
            if (gamestate[i][j+1] == -1):
                return  ((i, j+1))
    else:
        if (j == 0):
            if (gamestate[i][j+1] == -1):
                return  ((i, j+1))
            if (gamestate[i+1][j+1] == -1):
                return  ((i+1, j+1))
            if (gamestate[i+1][j] == -1):
                return  ((i+1, j))
            if (gamestate[i-1][j+1] == -1):
                return  ((i-1, j+1))
            if (gamestate[i-1][j] == -1):
                return  ((i-1, j))
        elif (j == 8):
            if (gamestate[i][j-1] == -1):
                return  ((i, j-1))
            if (gamestate[i+1][j-1] == -1):
                return  ((i+1, j-1))
            if (gamestate[i+1][j] == -1):
                return  ((i+1, j))
            if (gamestate[i-1][j-1] == -1):
                return  ((i-1, j-1))
            if (gamestate[i-1][j] == -1):
                return  ((i-1, j))
        else:
            if (gamestate[i][j-1] == -1):
                return  ((i, j-1))
            if (gamestate[i+1][j-1] == -1):
                return  ((i+1, j-1))
            if (gamestate[i+1][j] == -1):
                return  ((i+1, j))
            if (gamestate[i+1][j+1] == -1):
                return  ((i+1, j+1))
            if (gamestate[i-1][j-1] == -1):
                return  ((i-1, j-1))
            if (gamestate[i-1][j] == -1):
                return  ((i-1, j))
            if (gamestate[i-1][j+1] == -1):
                return  ((i-1, j+1))
            if (gamestate[i][j+1] == -1):
                return  ((i, j+1))

    return  ((69, 69))


# Define a function to process the output and decide the next input

# Has to return string of format "i,j"
def process_output_and_get_input(output):
    gamestate = output_to_array(output)
    
    # Run-through, marking mines
    for i in range(9):
        for j in range(9):
            if (gamestate[i][j] == (adjacent_unknowns(gamestate, i, j) + adjacent_mines(gamestate, i, j))):
                mark_mines(gamestate, i, j)

    # Run-through, trying to find a safe move
    for i in range(9):
        for j in range(9):
            if (gamestate[i][j] == adjacent_mines(gamestate, i, j)):
                valid_move = find_adjacent_unknown(gamestate, i, j)
                if (valid_move[0] != 69):
                    return(f"{valid_move[0]},{valid_move[1]}")
    
    # Return a random valid move
    valid_moves = []
    for i in range(9):
        for j in range(9):
            if (gamestate[i][j] == -1):
                valid_moves.append([i,j])
    valid_move = valid_moves[random.randrange(0, len(valid_moves))]
    
    return(f"{valid_move[0]},{valid_move[1]}")


# Call the function

while (1):
    interact_with_executable()

