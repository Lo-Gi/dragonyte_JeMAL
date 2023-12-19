import pandas as pd
from datetime import datetime

data_files = ["Business_case/Data/Categories.csv", 
                "Business_case/Data/Channel_Volume.csv", 
                "Business_case/Data/Company_Share_GBO_unit.csv", 
                "Business_case/Data/Locations.csv", 
                "Business_case/Data/Market_Sizes.csv", 
                "Business_case/Data/Subcategories.csv",]


# Load the CSV file
df = pd.read_csv('Business_case/Data/Company_Share_GBO_unit.csv')

# Define a function to parse dates and convert to dd/mm/yy format
def convert_to_dd_mm_yy(date_str):
    formats_to_try = [
        '%A, %d %b %Y', '%a, %d %B %Y', '%d %m %Y', '%m/%d/%Y', '%Y-%m-%d'
    ]
    for fmt in formats_to_try:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime('%d/%m/%y')
        except ValueError:
            pass
    return "Invalid format"

# Applying the function to the 'Year_date' column within the DataFrame
df['Year_date'] = df['Year_date'].apply(convert_to_dd_mm_yy)

# Displaying the standardized dates
print(df['Year_date'].unique())

# Save the updated DataFrame back to the CSV file
df.to_csv('Business_case/Data/Company_Share_GBO_unit.csv', index=False)

