import pandas as pd

data_files = ["Business_case/Data/Categories.csv", 
                "Business_case/Data/Channel_Volume.csv", 
                "Business_case/Data/Company_Share_GBO_unit.csv", 
                "Business_case/Data/Locations.csv", 
                "Business_case/Data/Market_Sizes.csv", 
                "Business_case/Data/Subcategories.csv",]

'''
for file in data_files:
    df = pd.read_csv(file)
    
    # Remove column with only same value
    for col in df.columns:
        if len(df[col].unique()) == 1:
            df.drop(col, axis=1, inplace=True)
    
    
    df.to_csv(file, index=False)
'''

# print all columns who have only one value
for file in data_files:
    df = pd.read_csv(file)
    for col in df.columns:
        if len(df[col].unique()) == 1:
            print(col, file)
            
# Remove column with only same value


