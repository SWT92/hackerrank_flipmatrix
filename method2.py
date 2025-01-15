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
    matrixes = [[[1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 10, 10, 10],
                 [1, 1, 1, 10, 10, 10],
                 [1, 1, 1, 10, 10, 10]],
                [[1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 20, 20, 20, 20],
                 [1, 1, 1, 1, 20, 20, 20, 20],
                 [1, 1, 1, 1, 20, 20, 20, 20],
                 [1, 1, 1, 1, 20, 20, 20, 20]],
                [[30, 1, 1, 30, 1, 1, 1, 1, 30, 1],
                 [1, 1, 30, 1, 1, 30, 1, 1, 1, 30],
                 [1, 30, 1, 1, 1, 1, 30, 1, 1, 1],
                 [30, 1, 1, 1, 1, 30, 1, 30, 1, 1],
                 [1, 1, 1, 1, 1, 1, 30, 1, 30, 1],
                 [1, 1, 1, 1, 30, 1, 1, 30, 1, 30],
                 [1, 1, 1, 1, 1, 1, 30, 1, 30, 1],
                 [30, 1, 1, 1, 1, 30, 1, 30, 1, 1],
                 [1, 30, 1, 1, 1, 1, 30, 1, 1, 1],
                 [1, 1, 30, 1, 1, 30, 1, 1, 1, 1]],
                [[112, 42, 83, 119],
                 [56, 125, 56, 49],
                 [15, 78, 101, 43],
                 [62, 98, 114, 108]],
                [[107, 54, 128, 15],
                 [12, 75, 110, 138],
                 [100, 96, 34, 85],
                 [75, 15, 28, 112]]
                ]

    correctAnswer = [10*3*3, 20*4*4, 30*5*5, 414, 488]
    
    for i in range(len(matrixes)):
        print(f"---------------- MATRIX {i+1} ---------------")
        matrix = matrixes[i]
        
        myAnswer = flippingMatrix(matrix)
        print(f"correct answer is {correctAnswer[i]}, my answer is {myAnswer}")
        print(f"------------ END OF MATRIX {i+1} ------------ \n")  