import pandas as pd

# Step 1: Load the cleaned dataset
file_path = r"C:\Users\USER\Desktop\projects\customer_segmentation_forecasting\data\cleaned_retail_data.csv"
df = pd.read_csv(file_path)

# Step 2: Select relevant columns for RFM analysis
# For RFM, we need: CustomerID, InvoiceDate, Quantity, UnitPrice
rfm_df = df[['CustomerID', 'InvoiceDate', 'Quantity', 'UnitPrice']].copy()

# Convert InvoiceDate to datetime if it's not already
rfm_df['InvoiceDate'] = pd.to_datetime(rfm_df['InvoiceDate'])

# Step 3: Calculate TotalPrice for each transaction
rfm_df['TotalPrice'] = rfm_df['Quantity'] * rfm_df['UnitPrice']

# Step 4: Calculate RFM metrics for each customer
import datetime as dt

# Define "snapshot" date (usually the day after the last invoice)
snapshot_date = rfm_df['InvoiceDate'].max() + pd.Timedelta(days=1)

print(rfm_df.columns)
print(rfm_df.head())

# Group by CustomerID to calculate RFM
rfm = rfm_df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'Quantity': 'count',  # Frequency: count of transactions per customer
    'TotalPrice': 'sum'    # Monetary
}).reset_index()

# Rename columns for clarity
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)

# Step 5: Quick check
print(rfm.head())
print("\nRFM shape:", rfm.shape)
