from sklearn.model_selection import cross_val_score

def cross_validate_model(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    print(f'Cross-validation Accuracy: {scores.mean()}')