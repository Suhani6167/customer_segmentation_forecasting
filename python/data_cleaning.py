# data_cleaning.py

import pandas as pd

# Step 1: Load the dataset
file_path = "data/retail_data.xlsx"
df = pd.read_excel(file_path, sheet_name="Online Retail", engine="openpyxl")

# Step 2: Quick look at the data
print("Dataset shape:", df.shape)
print("Columns:", df.columns)

# Step 3: Removing rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Step 4: Removing negative or zero quantities (returns or errors)
df = df[df['Quantity'] > 0]

# Step 5: Removing zero or negative prices
df = df[df['UnitPrice'] > 0]

# Step 6: Striping spaces from string columns
df['Description'] = df['Description'].str.strip()
df['Country'] = df['Country'].str.strip()

# Step 7: removing duplicate rows
df = df.drop_duplicates()

# Step 8: Saving cleaned dataset
cleaned_path = "data/cleaned_retail_data.csv"
df.to_csv(cleaned_path, index=False)

print("Cleaned dataset saved at:", cleaned_path)
print("Cleaned dataset shape:", df.shape)
