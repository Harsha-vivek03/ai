def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] + i == col + row or \
           board[i] - i == col - row:
            return False
    return True


def solve_n_queens_util(n, row, board, solutions):
    if row == n:
        solutions.append(board[:])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens_util(n, row + 1, board, solutions)


def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(n, 0, board, solutions)
    return solutions


def print_solution(solution):
    for board in solution:
        for row in range(len(board)):
            line = ""
            for col in range(len(board)):
                if col == board[row]:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


if __name__ == "__main__":
    while True:
        try:
            num_queens = int(input("Enter the number of queens: "))
            if num_queens < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    solutions = solve_n_queens(num_queens)

    if solutions:
        print(f"Solutions for {num_queens}-Queens Problem:")
        for idx, solution in enumerate(solutions):
            print("Solution", idx + 1)
            print_solution([solution])
    else:
        print("No solution exists")
