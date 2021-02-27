class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = []

        for line in matrix_string.split("\n"):
            self.matrix.append([int(n) for n in line.split(' ')])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [r[index-1] for r in self.matrix]