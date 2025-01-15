def flippingMatrix(matrix):
    remainder = sum(getRemainder(matrix))
    return remainder

def getRemainder(matrix):
    maxAmount = []
    quadEdge = len(matrix) // 2
    limit = len(matrix) - 1
    for row in range(quadEdge):
        for col in range(quadEdge):
            topLeft = matrix[row][col]
            topRight = matrix[row][limit-col]
            bottomLeft = matrix[limit-row][col]
            bottomRight = matrix[limit-row][limit-col]
            maxAmount.append(max(topLeft, topRight, bottomLeft, bottomRight))
            maxAmount.sort()
    return maxAmount

def printMatrix(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    print("------------ MATRIX 1 [6 x 6] ------------")
    matrix  = [[1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 10, 10, 10],
               [1, 1, 1, 10, 10, 10],
               [1, 1, 1, 10, 10, 10]]
    
    myAnswer = flippingMatrix(matrix)
    print(f"correct answer is {10*3*3}, my answer is {myAnswer}")
    print("------------ END OF MATRIX 1 ------------")
    print()

    print("------------MATRIX 2 [8 x 8]------------")
    matrix  = [[1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 20, 20, 20, 20],
               [1, 1, 1, 1, 20, 20, 20, 20],
               [1, 1, 1, 1, 20, 20, 20, 20],
               [1, 1, 1, 1, 20, 20, 20, 20]]
    
    myAnswer = flippingMatrix(matrix)
    print(f"correct answer is {20*4*4}, my answer is {myAnswer}")
    print("------------ END OF MATRIX 2 ------------")
    print()
    print("------------MATRIX 3 [10 x 10]------------")
    matrix  = [[30, 1, 1, 30, 1, 1, 1, 1, 30, 1],
               [1, 1, 30, 1, 1, 30, 1, 1, 1, 30],
               [1, 30, 1, 1, 1, 1, 30, 1, 1, 1],
               [30, 1, 1, 1, 1, 30, 1, 30, 1, 1],
               [1, 1, 1, 1, 1, 1, 30, 1, 30, 1],
               [1, 1, 1, 1, 30, 1, 1, 30, 1, 30],
               [1, 1, 1, 1, 1, 1, 30, 1, 30, 1],
               [30, 1, 1, 1, 1, 30, 1, 30, 1, 1],
               [1, 30, 1, 1, 1, 1, 30, 1, 1, 1],
               [1, 1, 30, 1, 1, 30, 1, 1, 1, 1]]
    
    myAnswer = flippingMatrix(matrix)
    print(f"correct answer is {30*5*5}, my answer is {myAnswer}")
    print("------------ END OF MATRIX 3 ------------")

    print("------------MATRIX 4 [4 x 4]------------")
    matrix  = [[112, 42, 83, 119], [56, 125, 56, 49],[15, 78, 101, 43], [62, 98, 114, 108]]
    
    myAnswer = flippingMatrix(matrix)
    print(f"correct answer is {414}, my answer is {myAnswer}")
    print("------------ END OF MATRIX 4 ------------")

    print("------------MATRIX 5 [4 x 4]------------")
    matrix  = [[107, 54, 128, 15],
               [12, 75, 110, 138],
               [100, 96, 34, 85],
               [75, 15, 28, 112]]
    
    myAnswer = flippingMatrix(matrix)
    print(f"correct answer is {488}, my answer is {myAnswer}")
    print("------------ END OF MATRIX 5 ------------")   