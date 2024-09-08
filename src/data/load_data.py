import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

# Load the raw data
iris = load_data('./data/raw/IRIS.csv')
