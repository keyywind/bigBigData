import pandas, sys
from chi_square import ChiSquare

filename = "mushrooms_formatted_D-d292021_T-231133.csv"

dataframe = pandas.read_csv(filename, header = None)

def list_to_dict(targetList): 
    
    return { value : 0 for value, _ in enumerate(targetList) }

mapping = [
    list_to_dict(["p", "e"]),
    
    list_to_dict(["b", "c", "x", "f", "k", "s"]),
    list_to_dict(["f", "g", "y", "s"]),
    list_to_dict(["n", "b", "c", "g", "r", "p", "u", "e", "w", "y"]),
    list_to_dict(["t", "f"]),
    list_to_dict(["a", "l", "c", "y", "f", "m", "n", "p", "s"]),
    
    list_to_dict(["a", "d", "f", "n"]),
    list_to_dict(["c", "w", "d"]),
    list_to_dict(["b", "n"]),
    list_to_dict(["k", "n", "b", "h", "g", "r", "o", "p", "u", "e", "w", "y"]),
    list_to_dict(["e", "t"]),
    
    list_to_dict(["b", "c", "u", "e", "z", "r"]),
    list_to_dict(["f", "y", "k", "s"]),
    list_to_dict(["f", "y", "k", "s"]),
    list_to_dict(["n", "b", "c", "g", "o", "p", "e", "w", "y"]),
    list_to_dict(["n", "b", "c", "g", "o", "p", "e", "w", "y"]),
    
    list_to_dict(["p", "u"]),
    list_to_dict(["n", "o", "w", "y"]),
    list_to_dict(["n", "o", "t"]),
    list_to_dict(["c", "e", "f", "l", "n", "p", "s", "z"]),
    list_to_dict(["k", "n", "b", "h", "r", "o", "u", "w", "y"]),
    
    list_to_dict(["a", "c", "n", "s", "v", "y"]),
    list_to_dict(["g", "l", "m", "p", "u", "w", "d"])
]
"""
def analyze_occurrence(dataframe):
    
    global mapping
    
    columns = dataframe.columns
    
    numRow, numCol = len(dataframe), len(columns)
    
    for col in range(numCol):
        
        for row in range(50):
            
            sys.stdout.write(f"\r({row},{col})")
            
            mapping[col][dataframe.loc[row, columns[col]]] += 1
            
            sys.stdout.flush()
            
analyze_occurrence(dataframe)
"""

X2 = ChiSquare(dataframe.loc[:4000], mapping)

history = X2.compute_X2()

#print(history)
