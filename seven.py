# Matrix Class: Create a Matrix class with attributes rows and columns. Implement methods add and multiply to perform matrix addition and multiplication.
# Example input: matrix1 = Matrix([[1, 2], [3, 4]]); matrix2 = Matrix([[5, 6], [7, 8]]); result = matrix1.add(matrix2); print(result.rows)
# Expected output: [[6, 8], [10, 12]]
# incorrect code works only for 2x2 Matrix
# class Matrix:
#         def __init__(self,*mtx) -> None:
#             self.matx = mtx

#         def show(self):
#              print(self.matx)

#         def add(self, mtx2):
#             y = mtx2.matx
#             x = self.matx
#             x = [[x[0][0]+ y[0][0], x[0][1]+ y[0][1]],
#                  [x[1][0]+ y[1][0], x[1][1]+ y[1][1]]]
#             return x
# a = Matrix([1,2],[2,3])
# b = Matrix([3,5],[7,0])
# # b.show()
# print(a.add(b))
# https://youtube.com/playlist?list=PLu0W_9lII9agqZuv_XJen_BEHycIh-FmG&si=ddjWYXZusxiUIdHU
class Matrix:
    def __init__(self, *matx) -> None:
        self.rows = matx
        self.columns = list(map(list, zip(*matx)))

    def show(self):
        print(self.rows)

    def add(self, mtx2):
        if len(self.matx) != len(mtx2.matx) or len(self.matx[0]) != len(mtx2.matx[0]):
            raise ValueError("Matrices must have the same dimensions for addition")

        result = []
        for i in range(len(self.matx)):
            row = []
            for j in range(len(self.matx[0])):
                row.append(self.matx[i][j] + mtx2.matx[i][j])
            result.append(row)

        return Matrix(*result)  # Create a new Matrix object for the result
    def multiply(self, other):
        if len(self.columns) != len(other.rows):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        result_rows = []
        for i in range(len(self.rows)):
            result_row = []
            for j in range(len(other.columns)):
                element = sum(self.rows[i][k] * other.columns[k][j] for k in range(len(self.columns)))
                result_row.append(element)
            result_rows.append(result_row)

        return Matrix(result_rows)

a = Matrix([1, 2], [2, 3])
b = Matrix([3, 5], [7, 0])
r = a.multiply(b)  # Output: [[4, 7], [9, 3]]
r.show()