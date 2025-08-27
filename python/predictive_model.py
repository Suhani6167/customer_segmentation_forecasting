import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Load predictive dataset
data_path = "data/predictive_dataset.csv"
if not os.path.exists(data_path):
    print("❌ predictive_dataset.csv not found! Run predictive_dataset.py first.")
    exit()

df = pd.read_csv(data_path)
print("📌 Preview of Predictive Dataset:\n", df.head())

# Use only numeric features for training
X = df[['Recency', 'Frequency', 'Monetary']]
y = df['Segment_Label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\n🔹 Training Samples: {len(X_train)}")
print(f"🔹 Testing Samples: {len(X_test)}")

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n✅ Model Evaluation:")
print(f"🔹 Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\n🔹 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\n🔹 Classification Report:\n", classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
with open("models/predictive_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\n💾 Model saved successfully at: models/predictive_model.pkl")
