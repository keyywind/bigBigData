import pandas, sys, pickle

from keyscraper.utils import TimeName

weightName, weights = "mushroom_weights_D-d312021_T-184650.json", {}

with open(weightName, "rb") as RF: weights = pickle.load(RF)
    
filename = "mushrooms_filtered_D-d292021_T-222723.csv"

print(weights)


"""
dataframe = pandas.read_csv(filename, header = None)

def format_column(dataframe, columns, index):
    
    global weights
    
    return dataframe.loc[:,columns[index]].map(weights[index])

def format_columns(dataframe):
    
    columns = dataframe.columns
    
    for index, _ in enumerate(columns):
        
        dataframe.loc[:,columns[index]] = format_column(dataframe, columns, index)
        
    return dataframe

dataframe = format_columns(dataframe)

print(dataframe.describe())

dataframe.to_csv(TimeName().get_name("mushrooms_formatted", ".csv"), header = False, index = False)
"""