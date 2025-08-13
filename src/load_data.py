import pandas as pd

def load_csv(file_path: str):
    """Load a CSV file into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    print("Loaded CSV with columns:", df.columns)
    return df

if __name__ == "__main__":
    df = load_csv("guidelines.csv")
    print(df.head())
