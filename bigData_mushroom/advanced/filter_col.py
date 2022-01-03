import sys, pandas, pickle

from keyscraper.utils import TimeName

filename = "mushrooms_filtered_D-d292021_T-222723.csv"

dataframe = pandas.read_csv(filename, header = None)

def track_occurrence(dataframe, column):
    
    categories, numRow = {}, len(dataframe)
    
    for row in range(numRow):
        
        key = dataframe.loc[row, column]
        
        if (key in list(categories.keys())): categories[key] += 1
        
        else: categories[key] = 1
        
    return categories

def track_occurrences(dataframe):
    
    columnData, columns = [], dataframe.columns
    
    for col in columns: columnData.append(track_occurrence(dataframe, col))
    
    return columnData

def get_mapping(columnData, column):
    
    return {
        data[0] : index for index, data in list(enumerate(columnData[column].items()))      
    }
    
def get_mappings(columnData):
    
    return [
        get_mapping(columnData, col) for col, _ in enumerate(columnData)        
    ]
    
mapping = get_mappings(track_occurrences(dataframe))

print(list(enumerate(mapping)))

"""
with open(TimeName().get_name("mushroom_weights", ".json"), "wb") as WF:
    
    pickle.dump(mapping, WF, protocol = pickle.HIGHEST_PROTOCOL)
"""