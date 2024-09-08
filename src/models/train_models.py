from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_evaluate(X_train, X_val, y_train, y_val):
    models = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Support Vector Machines': SVC(),
        'Random Forest': RandomForestClassifier(),
        'Gradient Boosting': GradientBoostingClassifier()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        
        print(f"Model: {name}")
        print(f"Accuracy: {accuracy_score(y_val, y_pred)}")
        print(f"Classification Report:\n{classification_report(y_val, y_pred)}")
        print('-' * 30)