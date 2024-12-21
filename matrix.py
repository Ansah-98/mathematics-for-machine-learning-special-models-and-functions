
class Help_Funtion:
    def delete(self,matrix, col_index):
        #deleting the row and column to form a new matrix
        new_matrix = [row[:col_index] + row[col_index+1:] for row in matrix[1:]]
        return new_matrix
       
    
    def compute_determinant(self,matrix):
        #check for the two by two matrix and return its determinant
        if len(matrix) == 2:
            a = matrix[0][0] * matrix[1][1]
            b = matrix[0][1] * matrix[1][0]
            return a - b
        
        determinant = 0
        for i in range(len(matrix)):
                element   = matrix[0][i]

                new_matrix  = self.delete(matrix,i)
                #recursive function to trim down the matrix till its 2x2 and then we compute the determinant
                determinant += ((-1)**(i)) * element *self.compute_determinant(new_matrix )
                
        return determinant
                
class Matrix(Help_Funtion):
    row = 0
    column  = 0
    matrix  = []
    def make_matrix(self):
        for i in self.row:
            print("enter your matrix row by row")
            row = 0
            col = 0
            for i in range(self.row):
                row  = []
                for i in range(self.column):
                    element  = int(input(f"enter the element at row {i + 1},  column {col + 1}"))
                    row.append(element)
                self.matrix.append(row)

    def check_square_matrix(self):
        if len(self.row) == len(self.column)  and self.row !=0:
            return True

    def determinant(self,):
        pass
        
    #function to delete the rows and columns of the element including the element
    def form_matrix(matrix):
        pass
    #matrix.del()

model = Help_Funtion()
determinant  = model.compute_determinant([[1,2,4,8],[1,3,7,10],[3,4,5,18],[1,2,2,2]])
print(determinant)