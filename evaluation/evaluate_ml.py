from sklearn.metrics import mean_absolute_error, r2_score

y_test = [80, 70, 90, 60, 85]
predictions = [78, 72, 88, 65, 82]

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("R2:", r2)