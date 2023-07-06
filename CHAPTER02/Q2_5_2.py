matrix = [
    ["●", "●", "●", "●"],
    ["●", "●", "●", "●"],
    ["●", "●", "●", "●"],
    ["●", "●", "●", "●"],
]

for i in range(4):
    matrix[i][i] = "○"

for row in matrix:
    print(" ".join(row))
