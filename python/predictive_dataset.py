# predictive_dataset.py

import pandas as pd
import os

# Load RFM scores data
rfm_path = "data/rfm_scores.csv"
if not os.path.exists(rfm_path):
    print("❌ Error: rfm_scores.csv not found! Please run rfm_scoring.py first.")
    exit()

rfm_df = pd.read_csv(rfm_path)

# Preview the data
print("\n📌 Preview of RFM Scores Data:")
print(rfm_df.head())

# Keep only relevant columns for modeling
predictive_df = rfm_df[['CustomerID', 'Recency', 'Frequency', 'Monetary', 'RFM_Score', 'Segment']].copy()

# Encode Segment labels into numbers for modeling
segment_mapping = {
    "Champion": 3,
    "Loyal": 2,
    "Potential Loyalist": 2,
    "At Risk": 1,
    "Hibernating": 0,
    "Lost": 0,
    "Others": 1
}

predictive_df['Segment_Label'] = predictive_df['Segment'].map(segment_mapping)

# Create "data" folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save predictive dataset inside the "data" folder
predictive_dataset_path = "data/predictive_dataset.csv"
predictive_df.to_csv(predictive_dataset_path, index=False)

print("\n✅ Predictive dataset created successfully!")
print(predictive_df.head())

# Optional: Also save a copy in the project root if needed
root_dataset_path = "predictive_dataset.csv"
predictive_df.to_csv(root_dataset_path, index=False)
print(f"✅ Predictive dataset saved at: {predictive_dataset_path}")
print(f"✅ Another copy saved at: {root_dataset_path}")
