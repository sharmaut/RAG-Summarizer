import pandas as pd

def preprocess_guidelines(df):
    """Extract and clean relevant columns from WHO Guidelines."""
    required_columns = ["title", "link"] 

    # Ensure required columns exist
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Drop rows with missing values
    df = df.dropna(subset=required_columns)

    # Convert to dictionary format for easier retrieval
    guidelines = df[required_columns].to_dict(orient="records")

    print(f"Processed {len(guidelines)} guidelines.")
    return guidelines

if __name__ == "__main__":
    df = pd.read_csv("guidelines.csv")  
    guidelines = preprocess_guidelines(df)
    print(guidelines[:3])  
