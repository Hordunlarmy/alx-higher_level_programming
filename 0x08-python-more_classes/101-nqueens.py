#!/usr/bin/python3
"""N-queens puzzle."""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [board_deepcopy(row) for row in board]
    return board


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board):
            board[r][c] = "x"
            r, c = r + dr, c + dc


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for s in solutions:
        print(s)
