def firecracker(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    firstColIsZero = False
    firstRowIsZero = False

    for r in range(rows):
        if matrix[r][0] == 0:
            firstColIsZero = True
        for c in range(cols):
            if matrix[0][c] == 0:
                firstRowIsZero = True
            
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    for r in range(1, rows):
        for c in range(1, cols):
            if (matrix[r][0] == 0 or matrix[0][c] == 0):
                matrix[r][c] = 0

    if firstColIsZero:
        for r in range(rows):
            matrix[r][0] = 0
            if firstRowIsZero:
                for c in range(cols):
                    matrix[0][c] = 0

    return matrix

#Test Case #1
matrix = [[0, 0, 0, 4, 8], [7, 8, 10, 3, 9], [5, 7, 2, 3, 1], [0, 4, 6, 7, 2], [0, 1, 8, 5, 10]]
print(firecracker(matrix))

#Test Case #2
matrix = [[0, 3, 3, 4, 8], [7, 8, 10, 3, 9], [5, 7, 0, 3, 1], [3, 4, 6, 7, 2], [3, 1, 8, 5, 10]]
print(firecracker(matrix))
