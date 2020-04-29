class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[0 for y in range(n)] for x in range(m)]

    def add(self, matrix2):
        size = matrix2.get_size()
        if (self.m, self.n) != size:
            print("matrices are not the same size. Abort!")
            exit()
        row = 0
        col = 0

        # m = row, n = col
        ret_matrix = Matrix(self.m, self.n)
        while row < self.m:
            while col < self.n:
                ret_matrix.matrix[row][col] = self.matrix[row][col] * matrix2.matrix[row][col]
                col += 1
            row += 1
        return ret_matrix
            
    
    def insert(row, col, val):
        self.matrix[col][row] = val

    def get_size(self):
        return (self.m, self.n)

    def print_matrix(self):
        for r in self.matrix:
            for c in r:
                print(c, end=" ")
            print()


def main():
    matrix1 = Matrix(5, 4)
    matrix2 = Matrix(5, 4)

    matrix3 = matrix1.add(matrix2)
    matrix3.print_matrix()


if __name__ == '__main__':
    main()
