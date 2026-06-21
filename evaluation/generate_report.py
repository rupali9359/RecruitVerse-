import json

report = {
    "accuracy": 0.60,
    "precision": 0.67,
    "recall": 0.67,
    "f1": 0.67,
    "correlation": 0.98
}

with open(
    "reports/model_metrics.json",
    "w"
) as f:
    json.dump(
        report,
        f,
        indent=4
    )

print("Report Generated Successfully")