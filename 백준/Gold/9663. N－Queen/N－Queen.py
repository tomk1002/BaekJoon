def solve_n_queens_bitmask(n):
    if n == 0:
        return 1

    count = 0
    
    def backtrack(row, cols, left_diagonals, right_diagonals):
        nonlocal count
        if row == n:
            count += 1
            return

        available_positions = ((1 << n) - 1) & ~(cols | left_diagonals | right_diagonals)

        while available_positions:
            position = available_positions & -available_positions
            
            available_positions -= position

            backtrack(
                row + 1,
                cols | position,
                (left_diagonals | position) >> 1,
                (right_diagonals | position) << 1,
            )

    backtrack(0, 0, 0, 0)
    return count

n = int(input())

result = solve_n_queens_bitmask(n)
print(result)