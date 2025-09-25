Algorithm (Simulated Annealing for Sudoku Puzzle Generation)

Start with a complete Sudoku solution (a valid filled board).

Remove numbers randomly to create a puzzle.

Use simulated annealing to refine:

Candidate state = partially filled grid.

Objective = ensure uniqueness of solution and maintain Sudoku rules.

Neighbor = remove/add/swap a number.

Accept moves that improve fitness or, with some probability, worse moves (escape local minima).

Stop when puzzle has enough blanks and still has a unique valid solution.
