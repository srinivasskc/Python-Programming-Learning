# 2D Lists and Nested Loops in Python

# 2D Lists.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print Elements of the List
print(number_grid[1][1])

# For Loops
for row in number_grid:
    print(row)

# Nested For Loops
for row in number_grid:
    for column in row:
        print(column)
