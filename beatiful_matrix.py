matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_index, col_index = i, j

moves = abs(2 - row_index) + abs(2 - col_index)
print(moves)
