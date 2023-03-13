import random

def count_islands(matrix):
    """
            Function, whitch calculate islands.

            Inputs:
                    matrix
            Outputs:
                    count - integer number, count
    """
    def deep_first_search(row, col):
        """
            Recursion function, that make deep first search, and assigns 0s. 
        """
        # Check if current cell is within the matrix boundaries and is an island
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0:
            return
        matrix[row][col] = 0
        
        deep_first_search(row-1, col)
        deep_first_search(row+1, col) 
        deep_first_search(row, col-1)
        deep_first_search(row, col+1)  

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1
                deep_first_search(i, j)
    return count

# prevent wrong input
while True:
    try:
        # specifying arguments with space 
        M, N = input("Input: ").split()
        M = int(M)
        N = int(N)
        
        # updated to task version (in task matrix determined)
        matrix = [[random.randint(0, 1) for j in range(N)] for i in range(M)]

        for i in range(M):
            for j in range(N):
                print(matrix[i][j], end=" ")
            print()

        print("Output:", count_islands(matrix))
        break
    except ValueError:
        print("Wrong input value!")
