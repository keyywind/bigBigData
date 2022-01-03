import pandas, sys, pickle, numpy, copy

from keyscraper.utils import TimeName

weights, weightName = {}, "mushroom_weights_D-d312021_T-184650.json"

with open(weightName, "rb") as RF: weights = pickle.load(RF)

filename = "mushrooms_formatted_D-d312021_T-185729.csv"

dataframe = pandas.read_csv(filename, header = None)

def generate_matrix(numRow, numCol): return numpy.zeros(shape = (numRow, numCol))

def get_valid_columns(weights): return [ len(column) > 1 for column in weights ]

valid_columns = get_valid_columns(weights)

def get_occurrence_matrix(dataframe, columns, index):
    
    global weights
    
    numRow, numCol = len(weights[0]), len(weights[index])
    
    matrix = generate_matrix(numRow + 1, numCol + 1)
    
    for row in range(len(dataframe)):
        
        first, target = dataframe.loc[row, columns[0]], dataframe.loc[row, columns[index]]
        
        matrix[first][target] += 1
        
    for row in range(numRow):
        
        matrix[row][-1] = numpy.sum(matrix[row, :-1])
        
    for col in range(numCol + 1):
        
        matrix[-1][col] = numpy.sum(matrix[:-1, col])
        
    return matrix

def get_expected_matrix(occurrence_matrix):
    
    numRow, numCol = len(occurrence_matrix) - 1, len(occurrence_matrix[0]) - 1
    
    matrix = copy.deepcopy(occurrence_matrix)
    
    for row in range(numRow):
        
        for col in range(numCol):
            
            matrix[row][col] = matrix[-1][col] * matrix[row][-1] / matrix[-1][-1]
            
    return matrix
            
def get_chi_square(occurrence_matrix, expected_matrix):
    
    numRow, numCol = len(occurrence_matrix) - 1, len(occurrence_matrix[0]) - 1
    
    matrix = generate_matrix(numRow + 1, numCol + 1)
    
    for row in range(numRow):
        
        for col in range(numCol):
            
            matrix[row][col] = (occurrence_matrix[row][col] - expected_matrix[row][col]) ** 2 / expected_matrix[row][col]
            
            matrix[row][-1] += matrix[row][col]
            
            matrix[-1][col] += matrix[row][col]
            
    matrix[-1][-1] = numpy.sum(matrix[:, -1])
            
    return matrix

def get_chi_squares(dataframe):
    
    columns = dataframe.columns
    
    numCol = len(columns)
    
    array = []
    
    for col in range(1, numCol):
    
        #sys.stdout.write(f"\rOn column ({col}/{numCol - 1})")
        
        if (valid_columns[col]):
            
            occurrence_matrix = get_occurrence_matrix(dataframe, columns, col)
            
            print(f"{col} | occ\n", numpy.round(occurrence_matrix), 3)
            
            expected_matrix = get_expected_matrix(occurrence_matrix)
            
            print(f"{col} | exp\n", numpy.round(expected_matrix), 3)
            
            chi_square_matrix = get_chi_square(occurrence_matrix, expected_matrix)
            
            print(f"{col} | chi\n", numpy.round(chi_square_matrix, 3))
            
            array.append(chi_square_matrix)
            
            print("\n\n")
        else:
            
            array.append(None)
            
        #sys.stdout.flush()
            
    return array

numpy.set_printoptions(precision=2, suppress=True)

chi_squares = get_chi_squares(dataframe)

#print(chi_squares)

"""
with open(TimeName().get_name("mushroom_X2", ".json"), "wb") as WF:
    
    pickle.dump(chi_squares, WF, protocol = pickle.HIGHEST_PROTOCOL)
"""