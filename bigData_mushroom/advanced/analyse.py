import pickle, numpy

from keyscraper.utils import TimeName

chi_square_result, X2Name = [], "./mushroom_X2_D-d312021_T-193610.json"

with open(X2Name, "rb") as RF:
    
    chi_square_result = pickle.load(RF)
    
def get_freedom_value(chi_square_result, index):
    
    matrix = chi_square_result[index]
    
    return ((len(matrix) - 2) * (len(matrix[0]) - 2), matrix[-1][-1])

def get_freedoms_values(chi_square_result):
    
    numCol = len(chi_square_result)
    
    result = []
    
    for col in range(numCol):
        
        if (isinstance(chi_square_result[col], numpy.ndarray)):
            
            result.append(get_freedom_value(chi_square_result, col))
            
        else: 
            
            result.append(None)
            
    return result

freedoms_values = get_freedoms_values(chi_square_result)

print(freedoms_values)

with open(TimeName().get_name("mushrooms_X2_result", ".json"), "wb") as WF:
    
    pickle.dump(freedoms_values, WF, protocol = pickle.HIGHEST_PROTOCOL)