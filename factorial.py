def trial(matrix):
    determinant = 0 
    for i in range(len(matrix)):
        determinant += matrix[i]
    return determinant 

model = trial([1,2,3])
print(model )