# rfm_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load RFM results
rfm = pd.read_csv("rfm_scores.csv", index_col=0)


# Check first few rows
print("RFM Data Preview:")
print(rfm.head())

# -----------------------------
# 1️⃣ Customer Count by Segment
plt.figure(figsize=(8,5))
sns.countplot(data=rfm, x='Segment', order=rfm['Segment'].value_counts().index, palette='viridis')
plt.title('Customer Count by Segment')
plt.ylabel('Number of Customers')
plt.xlabel('Segment')
plt.tight_layout()
plt.show()

# -----------------------------
# 2️⃣ Total Monetary Value by Segment
plt.figure(figsize=(8,5))
sns.barplot(data=rfm, x='Segment', y='Monetary', estimator=sum, palette='magma')
plt.title('Total Revenue by Segment')
plt.ylabel('Total Monetary Value')
plt.xlabel('Segment')
plt.tight_layout()
plt.show()

# -----------------------------
# 3️⃣ Recency vs Frequency Scatter by Segment
plt.figure(figsize=(8,6))
sns.scatterplot(data=rfm, x='Recency', y='Frequency', hue='Segment', palette='Set2')
plt.title('Recency vs Frequency by Segment')
plt.xlabel('Recency (days)')
plt.ylabel('Frequency')
plt.legend(title='Segment')
plt.tight_layout()
plt.show()
