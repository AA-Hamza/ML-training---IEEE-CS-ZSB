#import fractions

def print_matrix(matrix):
    for r in matrix:
        print(r)

def reduce_to_ref(matrix):     #make lower triangle zeros with diagnols of 1's
    _LEN = len(matrix)

    def get_max_of_column(c):
        value = abs(matrix[c][c])
        index = c
        for r in range(c+1, _LEN):
            if (value < abs(matrix[r][c])):
                index = r
        return index
        
    for a in range(_LEN):
        max_index = get_max_of_column(a)
        matrix[a], matrix[max_index] = matrix[max_index], matrix[a]     #swaping
        if (matrix[a][a] == 0):
            print("Dividing by Zero, your equations can't be solved or have many solutions")
            exit()
    
    for a in range(_LEN):
        for b in range(a+1, _LEN):
            if (matrix[a][a]):
                ratio = matrix[b][a]/matrix[a][a]
            else:
                print("Dividing by Zero, your equations can't be solved or have many solutions")
                exit()
            for c in range(a+1, _LEN+1):
                matrix[b][c] -= matrix[a][c]*ratio
            matrix[b][a] = 0    #out of the loop to solve float problems #TODO use fractions

def solve_ref(matrix):
    _LEN = len(matrix)
    solution = []
    for i in range(_LEN-1, -1, -1):
        for j in range(_LEN-1, i, -1):
            matrix[i][_LEN] -= matrix[i][j]
        solution.append(matrix[i][_LEN]/matrix[i][i])
        for r in range(i-1, -1, -1):
            matrix[r][i] *= solution[-1]
    solution.reverse()
    return solution

def main():
    num_of_vars = int(input("Enter the number of variables: "))

    matrix = []
    print("Enter equations cofficents row by row")

    counter = 0
    while (counter < num_of_vars):
        row = list(map(int, input().split()))
        if (len(row) != num_of_vars+1):
            print(f"re-enter row, pls enter {num_of_vars+1} cofficents")
            continue
        matrix.append(row)
        counter += 1
    reduce_to_ref(matrix)
    print(solve_ref(matrix))

if __name__ == "__main__":
    main()
