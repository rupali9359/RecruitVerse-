import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("data/evaluation/matching_results.csv")

accuracy = accuracy_score(df["actual_match"], df["predicted_match"])
precision = precision_score(df["actual_match"], df["predicted_match"])
recall = recall_score(df["actual_match"], df["predicted_match"])
f1 = f1_score(df["actual_match"], df["predicted_match"])

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)