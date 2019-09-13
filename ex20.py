def fun02():
    # matrix of 4x3 
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]		
    ]	
    print("Original Matrix 3x4 ",matrix)
    row = matrix[0] # get the first row
    length_of_row = len(row) # length of the first row of matrix
    matrix2 = [[row[i] for row in matrix] for i in range(length_of_row)]

    print("Converted matrix 4x3 ",matrix2)

fun02()
