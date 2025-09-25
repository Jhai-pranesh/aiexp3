import random
import math
import copy

N = 9

# Utility: Check if board is valid
def is_valid(board, row, col, num):
    # Check row and col
    for i in range(N):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j] == num:
                return False
    return True

# Utility: Check if puzzle is solved
def is_solved(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 or not is_valid(board, i, j, board[i][j]):
                return False
    return True

# Generate full Sudoku solution (backtracking)
def solve_board(board):
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                nums = list(range(1, N+1))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    board = [[0]*N for _ in range(N)]
    solve_board(board)
    return board

# Fitness: fewer conflicts = better
def fitness(board):
    conflicts = 0
    for row in range(N):
        conflicts += (N - len(set(board[row])))

    for col in range(N):
        col_vals = [board[row][col] for row in range(N)]
        conflicts += (N - len(set(col_vals)))
    return -conflicts  # higher is better

# Simulated Annealing for Sudoku puzzle generation
def simulated_annealing(iterations=1000, temp=1.0, cooling=0.995):
    # Step 1: Generate full valid board
    solution = generate_full_board()

    # Step 2: Start removing numbers
    puzzle = copy.deepcopy(solution)
    blanks = random.randint(30, 50)  # remove 30–50 cells
    for _ in range(blanks):
        row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    current = puzzle
    current_fit = fitness(current)

    for _ in range(iterations):
        # Neighbor = remove another number
        neighbor = copy.deepcopy(current)
        row, col = random.randint(0, 8), random.randint(0, 8)
        neighbor[row][col] = 0
        neighbor_fit = fitness(neighbor)

        # Accept move?
        if neighbor_fit > current_fit:
            current, current_fit = neighbor, neighbor_fit
        else:
            if random.random() < math.exp((neighbor_fit - current_fit) / temp):
                current, current_fit = neighbor, neighbor_fit

        temp *= cooling  # reduce temperature

    return current

# Run
puzzle = simulated_annealing()
print("Generated Sudoku Puzzle:")
for row in puzzle:
    print(row)
