import pandas as pd
import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    importance = pd.Series(model.feature_importances_, index=feature_names)
    importance.sort_values(ascending=False).plot(kind='bar')
    plt.title('Feature Importance')
    plt.xlabel('Feature')
    plt.ylabel('Importance')
    plt.show()