import pandas as pd
import pickle
import os

# Load trained model
model_path = "models/predictive_model.pkl"
if not os.path.exists(model_path):
    print("❌ Model not found! Run predictive_model.py first.")
    exit()

with open(model_path, "rb") as file:
    model = pickle.load(file)
print("✅ Model loaded successfully!")

# New customers data
new_customers = pd.DataFrame({
    "Recency": [10, 120, 45],
    "Frequency": [50, 5, 20],
    "Monetary": [2000, 200, 800]
})

print("\n📌 New Customers Data:\n", new_customers)

# Predict segments
predictions = model.predict(new_customers)
new_customers['Predicted_Segment_Label'] = predictions

# Map back to segment names if needed
label_mapping = {0: "Hibernating/Lost", 1: "At Risk/Others", 2: "Loyal", 3: "Champion"}
new_customers['Predicted_Segment'] = new_customers['Predicted_Segment_Label'].map(label_mapping)

print("\n📌 Predictions:")
print(new_customers)
