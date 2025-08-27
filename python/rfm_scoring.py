import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned_retail_data.csv")

# Ensure InvoiceDate is datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Step 1: Calculate Total Sales for Monetary Value
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Step 2: Calculate Recency, Frequency, Monetary
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm_df = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                  # Frequency
    'TotalSales': 'sum'                                      # Monetary
}).reset_index()

# Rename columns properly
rfm_df.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalSales': 'Monetary'
}, inplace=True)

# Step 3: Assign RFM Scores (1-5)
rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], 5, labels=[5,4,3,2,1], duplicates='drop')
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], 5, labels=[1,2,3,4,5], duplicates='drop')

# Step 4: Combine RFM Scores
rfm_df['RFM_Score'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)

# Step 5: Customer Segmentation
def segment_customer(rfm_code):
    r, f = rfm_code[0], rfm_code[1]
    if r == '5' and f == '5':
        return 'Champion'
    elif f == '5':
        return 'Loyal'
    elif r == '1':
        return 'At Risk'
    else:
        return 'Others'

rfm_df['Segment'] = (rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str)).apply(segment_customer)

# Step 6: Save Results
os.makedirs("data", exist_ok=True)
rfm_df.to_csv("data/rfm_results.csv")
rfm_df.to_csv("rfm_scores.csv", index=False)

# Step 7: Print Preview
print("✅ RFM scoring and segmentation completed!")
print(rfm_df.head())
