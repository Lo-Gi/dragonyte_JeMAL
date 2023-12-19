import pandas as pd

'''
data_files = ["Business_case/Data/Categories.csv", 
                "Business_case/Data/Company_Share_GBO_unit.csv", 
                "Business_case/Data/Company_Share_GBO_unit.csv", 
                "Business_case/Data/Locations.csv", 
                "Business_case/Data/Market_Sizes.csv", 
                "Business_case/Data/Subcategories.csv",]


for file in data_files:
    df = pd.read_csv(file)
    
    # Remove column with only same value
    for col in df.columns:
        if len(df[col].unique()) == 1:
            df.drop(col, axis=1, inplace=True)
    
    
    df.to_csv(file, index=False)
'''

# Read only the 'Unit' column from the CSV file
Unit_column = pd.read_csv("Business_case/Data/Company_Share_GBO_unit_Copy.csv", sep=';', usecols=['Unit'])

# Now, you can assign this 'Unit' column to your original DataFrame
df = pd.read_csv("Business_case/Data/Company_Share_GBO_unit.csv")
df['Unit'] = Unit_column['Unit']

# Perform the comma to dot replacement on the 'Unit' column
df['Unit'] = df['Unit'].str.replace(',', '.')

# Save the updated DataFrame to the CSV file
df.to_csv("Business_case/Data/Company_Share_GBO_unit.csv", index=False)