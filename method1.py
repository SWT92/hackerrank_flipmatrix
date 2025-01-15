def flippingMatrix(matrix):
    corner = sum(getCorners(matrix))
    edge = sum(getEdge(matrix))
    middle = getMiddle(matrix)
    remainder = sum(getRemainder(matrix))
    return corner + edge + middle + remainder

def getCorners(matrix):
    # if its 4 x 4 matrix, there is only one corner to check
    # if its 6 x 6 matrix, there is 2 corner to check
    # if its 8 x 8 matrix, there is 3 corner to check
    # if its 10 x 10 matrix, there is 4 corner to check
    # the pattern to find the amount of corners to check is length of matrix divided by 2 minus - 
    # (len(matrix) // 2) - 1
    #printMatrix(matrix)
    biggestCorners = []
    amountOfCorner = (len(matrix) // 2)-1
    limit = len(matrix)-1
    for i in range(amountOfCorner):
        topLeft = matrix[i][i]
        topRight = matrix[i][limit-i]
        bottomLeft = matrix[limit-i][i]
        bottomRight = matrix[limit-i][limit-i]
        #print(f"TL:{topLeft},TR:{topRight},BL:{bottomLeft},BR:{bottomRight}, limit:{limit}")
        biggestCorners.append(max(topLeft, topRight, bottomLeft, bottomRight))

    #print(f"The biggest corner value is {biggestCorners}, it should return list of integer base on the amount of corners.")
    #print(f"4x4 should return list of 1 integer, 6x6 should return list of 2 integer, 8x8 should return list of 3 integer")
    return biggestCorners

def getEdge(matrix):
    # if its 4 x 4 matrix, get max of ([0][1] [0][2] [limit][1] [limit][2]) and get max of ([1][0] [2][0] [1][limit] [2][limit]]) *** 1 EDGE * 2 ***
    # if its 6 x 6 matrix, get max of ([0][2] [0][3] [limit][2] [limit][3]) and get max of ([2][0] [3][0] [2][limit] [3][limit]]) *** 2 EDGE * 2 ***
    #                      get max of ([1][2] [1][3] [limit-1][2] [limit-1][3]) and get max of ([2][1] [3][1] [2][limit-1] [3][limit-1]])
    # if its 8 x 8 matrix, get max of ([0][3] [0][4] [limit][3] [limit][4]) and get max of ([3][0] [4][0] [3][limit] [4][limit]]) *** 3 EDGE * 2 ***
    #                      get max of ([1][3] [1][4] [limit-1][3] [limit-1][4]) and get max of ([3][1] [4][1] [3][limit-1] [4][limit-1]])
    #                      get max of ([2][3] [2][4] [limit-2][3] [limit-2][4]) and get max of ([3][2] [4][2] [3][limit-2] [4][limit-2]])
    # if its 10 x 10 matrix, get max of ([0][4] [0][5] [limit][4] [limit][5]) and get max of ([4][0] [5][0] [4][limit] [5][limit]]) *** 4 EDGE * 2 ***
    #                      ... too long 

    #printMatrix(matrix)
    biggestEdges = []
    ## the amount of edges is half the size of matrix minus 1 (because of the decimal and computer language conversion)
    middle = (len(matrix) // 2) -1
    limit = len(matrix)-1
    for i in range(middle):
        topLeftEdge = matrix[0+i][middle]
        topRightEdge = matrix[0+i][middle+1]
        bottomLeftEdge = matrix[limit-i][middle]
        bottomRightEdge = matrix[limit-i][middle+1]
        biggestEdges.append(max(topLeftEdge, topRightEdge, bottomLeftEdge, bottomRightEdge))
        #print(f"TL:{topLeftEdge},TR:{topRightEdge},BL:{bottomLeftEdge},BR:{bottomRightEdge}, limit:{limit-i}, middle:{middle}")
        leftTopEdge = matrix[middle][i]
        leftBottomEdge = matrix[middle][i+1]
        rightTopEdge = matrix[middle][limit-i]
        rightBottomEdge = matrix[middle+1][limit-i]
        biggestEdges.append(max(leftTopEdge, leftBottomEdge, rightTopEdge, rightBottomEdge))
        #print(f"TL:{topLeftEdge},TR:{topRightEdge},BL:{bottomLeftEdge},BR:{bottomRightEdge}, limit:{limit-i}, middle:{middle}")
    #print(f"The biggest edge is {biggestEdges}")
    #print("For 4 x 4 this should return list of 2 integers, 6x6 list of 4 integers, 8x8 list of 6 integers, 10x10 list of 8 integers")
    return biggestEdges
    
def getMiddle(matrix):
    # if its 4x4 matrix, get max value from the middle 4 elements, [1,1] [1,2] [2,1] [2,2]
    # if its 6x6 matrix, get max value from the middle 4 elements, [2,2] [2,3] [3,2] [3,3]
    # if its 8x8 matrix, get max value from the middle 4 elements, [3,3] [3,4] [4,3] [4,4]
    # if its 10x10 matrix, get max value from the middle 4 elements, [4,4] [4,5] [5,4] [5,5]
    #printMatrix(matrix)

    middle = len(matrix) // 2

    mTopLeft = matrix[middle-1][middle-1]
    mTopRight = matrix[middle-1][middle]
    mBottomLeft = matrix[middle][middle-1]
    mBottomRight = matrix[middle][middle]
    #print(f"mTL:{mTopLeft},mTR:{mTopRight},mBL:{mBottomLeft},mBR:{mBottomRight}, middle:{middle}")
    return max(mTopLeft, mTopRight, mBottomLeft, mBottomRight)
    
def getRemainder(matrix):
    # if its 4x4 matrix, there should be no remainder
    # if its 6x6 matrix, there should be 2 remainder value
    # if its 8x8 matrix, there should be 6 remainder value
    # if its 10x10 matrix, there should be 12 remainder value
    # if its 12x12 matrix, there should be 20 remainder value
    # quardEdge is because middle value is out, so mid value - 1
    #printMatrix(matrix)

    maxAmount = []
    quadEdge = len(matrix) // 2 - 1
    limit = len(matrix) - 1
    for row in range(quadEdge):
        for col in range(quadEdge):
            if row != col:
                topLeft = matrix[row][col]  
                topRight = matrix[row][limit-col]
                bottomLeft = matrix[limit-row][col]
                bottomRight = matrix[limit-row][limit-col]
                #print(f"TL:{topLeft},TR:{topRight},BL:{bottomLeft},BR:{bottomRight}, limit:{limit}, quadEdge:{quadEdge}, row:{row}, col:{col}")
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
