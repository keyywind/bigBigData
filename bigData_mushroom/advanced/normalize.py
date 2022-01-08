from tensorflow.keras import utils

from keyscraper.utils import TimeName

to_categorical = utils.to_categorical

import pandas, pickle, numpy, sys, time

filename = "./mushrooms_formatted_D-d312021_T-185729.csv"

weights, weightName = [], "./mushroom_weights_D-d312021_T-184650.json"

columns_to_eliminate = [
    18, 
    17, 
    8, 
    6, 
    2, 
    1        
]

def to_binary(data, bits): return [data >> i & 1 for i in range(bits - 1,-1,-1)]

with open(weightName, "rb") as RF: weights = pickle.load(RF)

print(weights)

dataframe = pandas.read_csv(filename, header = None)

columns = dataframe.columns

valid_columns = [ (0 if (col in columns_to_eliminate) else len(weights[col]) ) for col in range(len(weights)) ]

numRow, numCol = len(dataframe), len(columns)

dataframe = dataframe.values.tolist()

for col in range(numCol):
    
    for row in range(numRow):
        
        sys.stdout.write(f"\r({row}, {col})")
        
        if (col):
            
            dataframe[row][col] = to_binary(int(dataframe[row][col]), valid_columns[col].bit_length())
                        
            #print(len(dataframe), len(dataframe[row]), len(dataframe[row][col]), end = '\n')
            
            #time.sleep(2)
            
        else:
                   
            dataframe[row][col] = to_categorical(numpy.array(dataframe[row][col]), num_classes = valid_columns[col]).tolist()
            
            #print(len(dataframe), len(dataframe[row]), len(dataframe[row][col]), end = '\n')
            
            #time.sleep(2)
        
        sys.stdout.flush()
        
def get_arrays(dataframe, row):
    
    return tuple([ col for index, col in enumerate(dataframe[row]) if (valid_columns[index] > 1) ])
        
for row in range(numRow):
    
    dataframe[row] = numpy.concatenate(get_arrays(dataframe, row))
    
dataframe = numpy.stack(dataframe)

print(dataframe)

print(type(dataframe), len(dataframe), len(dataframe[0]))

with open(TimeName().get_name("mushroom_training_data", ".json"), "wb") as WF:
    
    pickle.dump(dataframe, WF, protocol = pickle.HIGHEST_PROTOCOL)