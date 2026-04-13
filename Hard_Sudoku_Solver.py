# https://www.codewars.com/kata/55171d87236c880cea0004c6/train/python
from random import shuffle


def solve(board):
    """Solve a 9x9 Sudoku board in place and return it."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []

    def box_index(row, col):
        return (row // 3) * 3 + (col // 3)

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            if value == 0:
                empties.append((row, col))
            else:
                box = box_index(row, col)
                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)

    def backtrack():
        if not empties:
            return True

        best_index = -1
        best_candidates = None

        # Choose the empty cell with the fewest valid choices first.
        for index, (row, col) in enumerate(empties):
            box = box_index(row, col)
            used = rows[row] | cols[col] | boxes[box]
            candidates = [num for num in range(1, 10) if num not in used]

            if not candidates:
                return False

            if best_candidates is None or len(candidates) < len(best_candidates):
                best_index = index
                best_candidates = candidates
                if len(best_candidates) == 1:
                    break

        shuffle(best_candidates)
        row, col = empties.pop(best_index)
        box = box_index(row, col)

        for num in best_candidates:
            board[row][col] = num
            rows[row].add(num)
            cols[col].add(num)
            boxes[box].add(num)

            if backtrack():
                return True

            # Undo the guess and try the next candidate.
            board[row][col] = 0
            rows[row].remove(num)
            cols[col].remove(num)
            boxes[box].remove(num)

        empties.insert(best_index, (row, col))
        return False

    backtrack()
    return board
