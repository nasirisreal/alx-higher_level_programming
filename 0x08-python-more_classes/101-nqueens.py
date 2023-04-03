import sys

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    cols = set()
    diag1 = set()
    diag2 = set()
    solutions = []
    def backtrack(queens, row):
        if row == n:
            solutions.append(queens)
            return
        for col in range(n):
            if col in cols or row-col in diag1 or row+col in diag2:
                continue
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            backtrack(queens+[col], row+1)
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)
    backtrack([], 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solutions = nqueens(n)
    for solution in solutions:
        print(' '.join(str(i) for i in solution))

