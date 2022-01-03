import pandas, sys
from keyscraper.utils import TimeName

filename = "./mushrooms_filtered_D-d292021_T-222723.csv"

filterData = pandas.read_csv(filename, header = None)

def list_to_dict(targetList): 
    
    return {  key : value for value, key in enumerate(targetList) }

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

def format_data(filterData):
    
    global mapping
    
    columns = filterData.columns
    
    numRow, numCol = len(filterData), len(columns)
    
    for row in range(numRow):
        
        for col in range(numCol):
            
            sys.stdout.write(f"\r({row}, {col})")
            
            filterData.loc[row, columns[col]] = mapping[col][
                filterData.loc[row, columns[col]]        
            ]
            
            sys.stdout.flush()
        
    return filterData

filterData = format_data(filterData)

print(filterData.describe())

filterData.to_csv(TimeName().get_name("mushrooms_formatted", ".csv"), header = False, index = False)