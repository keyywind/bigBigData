from keyscraper.utils import TimeName
import pandas, sys

rawData = pandas.read_csv("./mushrooms.data", header = None)

print(rawData.describe())

def filter_missing(dataframe):
    
    columns = dataframe.columns
    
    (numCols, numRows) = (
        len(columns),
        len(dataframe)
    )
    
    for row in range(numRows - 1, -1, -1):
        
        missing = False
        
        for col in range(numCols):
            
            sys.stdout.write(f"\r({row}, {col})")
            
            data = dataframe.loc[row, columns[col]]
            
            sys.stdout.flush()
            
            if (data == "?"):
                
                missing = True
                
                break
            
        if (missing): 
            
            dataframe = dataframe.drop(row)
            
    return dataframe
  
print("ORI LEN: ", len(rawData))

rawData = filter_missing(rawData)
    
print("NEW LEN: ", len(rawData))

rawData.to_csv(TimeName().get_name("mushrooms_filtered", ".csv"), index = False, header = False)