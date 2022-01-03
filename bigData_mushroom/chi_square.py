import pandas, sys, copy, numpy

def make_matrix(numRow, numCol): return numpy.zeros(shape = (numRow, numCol))

class ChiSquare:
    
    def __init__(self, dataframe, dictionary):
        
        self.dataframe, self.dictionary = copy.deepcopy(dataframe), copy.deepcopy(dictionary)
        
    def compute_X2(self):
        
        columns = self.dataframe.columns
        
        numRow, numCol = len(self.dataframe), len(columns)
                    
        history = []
        
        for col in range(1, numCol):
            
            matrix = make_matrix(
                len(self.dictionary[0]) + 1,
                len(self.dictionary[col]) + 1
            )
            
            #print(matrix)
            
            for row in range(numRow):
                
                matrix[self.dataframe.loc[row, columns[0]]][self.dataframe.loc[row, columns[col]]] += 1
                
            for index in range(len(self.dictionary[0])):
                
                matrix[index][-1] = numpy.sum(matrix[index, :-1])
                
            print(matrix.tolist())
                
            for index in range(len(self.dictionary[col]) + 1):
                
                matrix[-1][index] = numpy.sum(matrix[:-1, index])
                
            expect = copy.deepcopy(matrix)
            
            for i in range(len(self.dictionary[0])):
                
                for j in range(len(self.dictionary[col])):
                    
                    expect[i][j] = matrix[-1][j] * matrix[i][-1] / matrix[-1][-1]
                    
            print(expect.tolist())    
                
            X2 = copy.deepcopy(expect)
            
            for i in range(len(self.dictionary[0])):
                
                for j in range(len(self.dictionary[col])):
                    
                    X2[i][j] = (expect[i][j] - matrix[i][j]) ** 2 / expect[i][j]
                    
            print(X2.tolist())
                    
            history.append([
                matrix.tolist(), expect.tolist(), X2.tolist()        
            ])
    
            break
    
        return history