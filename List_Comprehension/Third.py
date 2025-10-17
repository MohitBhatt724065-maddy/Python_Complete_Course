# Flattening the list of list.

Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([num for elem in Matrix for num in elem])

