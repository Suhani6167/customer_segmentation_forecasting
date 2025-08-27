# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = "data/retail_data.xlsx"
df = pd.read_excel(file_path, sheet_name="Online Retail", engine="openpyxl")

# Step 2: overview
print("Dataset shape:", df.shape)
print("\nColumns in the dataset:\n", df.columns)
print("\nDataset Info:\n")
print(df.info())
print("\nSummary Statistics:\n")
print(df.describe())

# Step 3: Checking missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Step 4: Unique countries
print("\n--- Unique Countries ---")
print(df['Country'].nunique())
print(df['Country'].value_counts().head(10))

# Step 5: Visualizations

# 5.1 Top 10 countries by transactions
top_countries = df['Country'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.index, y=top_countries.values)
plt.title("Top 10 Countries by Number of Transactions")
plt.ylabel("Number of Transactions")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.show()

# 5.2 Quantity distribution
plt.figure(figsize=(10,6))
sns.histplot(df['Quantity'], bins=50, kde=False)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.xlim(-50, 100)  # ignore extreme outliers
plt.show()

# 5.3 UnitPrice distribution
plt.figure(figsize=(10,6))
sns.histplot(df['UnitPrice'], bins=50, kde=False)
plt.title("UnitPrice Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.xlim(0, 100)  # ignore extreme outliers
plt.show()

# 5.4 Number of purchases per customer
customer_counts = df['CustomerID'].value_counts()
plt.figure(figsize=(10,6))
sns.histplot(customer_counts, bins=50, kde=False)
plt.title("Number of Purchases per Customer")
plt.xlabel("Number of Purchases")
plt.ylabel("Number of Customers")
plt.xlim(0, 200)
plt.show()
