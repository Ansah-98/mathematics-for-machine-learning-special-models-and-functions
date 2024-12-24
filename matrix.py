import numpy as np

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


#make_simlar: used to create a similar function using the QR decomposition
#basically decomposing the matrix and finding  multiple similar matrices 
#leaving only the eigen values in the diagonal and forming an upper triangular matrix

    def make_similar(matrix):
        Q,R = np.linalg.qr(matrix) #generates a Q*R matrices which is similar to the input matrix
        sim_matrix = np.dot(R,Q)
        return sim_matrix 



#compute_eigenvalue:returns a list of all the eigen_values of a 
    def gen_eigenvalue(self , matrix):
        sim_matrix  = Help_Funtion.make_similar(matrix)
        leig = sim_matrix[-1,-1]#gets the last eigen value in the similar matrix 
        diff  = 1

        while diff > 1e-32: #iterate till the last eigen value's in the diagonal of the newest similar matrix
                            # precision is less than 10^-32 compared to the eigen value before 
            sim_matrix  = Help_Funtion.make_similar(sim_matrix)
            diff = abs(leig - sim_matrix[-1,-1])
            leig = sim_matrix[-1,-1]
        eigs = [float(sim_matrix[i,i]) for i in range(len(sim_matrix))]
        return eigs

class Matrix(Help_Funtion):
    row = None
    column  = None
    matrix  = []
    def make_matrix(self):
        self.row = int(input("enter the number of rows of the matrix"))
        self.column = int(input("enter the number of columns of the matrix"))
        
        print("enter your matrix row by row")
        for i in range(self.row):
            row  = []
            for j in range(self.column):
                element  = int(input(f"enter the element at row {i + 1},  column { j + 1}"))
                row.append(element)
            self.matrix.append(row)

    def check_square_matrix(self):
        if len(self.row) == len(self.column)  and (self.row !=0):
            return True
    #main function for the determinant
    def determinant(self):
        if len(self.matrix  == 1) and self.check_square_matrix():
            return self.matrix[0]
        if self.check_square_matrix():
            return self.compute_determinant(self.matrix)
    #function to delete the rows and columns of the element including the element

    def compute_eigenvalues(self):
        if self.check_square_matrix():
            return self.gen_eigenvalue(self.matrix)

model = Help_Funtion()
determinant  = model.compute_determinant([[1,2,3],[3,1,2],[0,0,1]])
eigen_values   = model.gen_eigenvalue(np.array([[1,2,3],[3,1,2],[0,0,1]]))
print(eigen_values)
print(np.linalg.eigvals([[1,2,3],[3,1,2],[0,0,1]]))
#print(eigen_values)