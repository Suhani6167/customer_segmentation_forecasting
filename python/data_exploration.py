import pandas as pd
from pathlib import Path

# Path to the dataset
path = Path(r"C:\Users\USER\Desktop\projects\customer_segmentation_forecasting\data\retail_data.xlsx")

# Load the Excel file
xls = pd.ExcelFile(path, engine="openpyxl")

# available sheet names
print("Available sheets:", xls.sheet_names)

# the right sheet
sheet = "Online Retail" if "Online Retail" in xls.sheet_names else xls.sheet_names[0]

# Load the sheet
df = pd.read_excel(path, sheet_name=sheet, engine="openpyxl")

# Display dataset info
print("\nLoaded sheet:", sheet)
print("Shape of dataset:", df.shape)

# first 10 rows
print("\nFirst 10 rows:")
print(df.head(10))

# column info
print("\nDataset Info:")
print(df.info())
