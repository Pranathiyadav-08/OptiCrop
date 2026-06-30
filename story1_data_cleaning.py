import pandas as pd

# ====================================
# Load Dataset
# ====================================
df = pd.read_csv("data/crop.csv")

print("===================================")
print("Original Dataset")
print("===================================")
print(df.head())

# ====================================
# Dataset Information
# ====================================
print("\nDataset Information")
print(df.info())

# ====================================
# Check for Missing Values
# ====================================
print("\nMissing Values in Each Column")
print(df.isnull().sum())

# ====================================
# Total Missing Values
# ====================================
print("\nTotal Missing Values:", df.isnull().sum().sum())

# ====================================
# Handle Missing Values
# ====================================

if df.isnull().sum().sum() == 0:
    print("\nNo missing values found.")
else:
    print("\nMissing values found.")

    # Fill numerical columns with mean
    numeric_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].mean())

    # Fill crop label with mode
    df['label'] = df['label'].fillna(df['label'].mode()[0])

    print("\nMissing values handled successfully.")

# ====================================
# Verify Again
# ====================================
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# ====================================
# Save Clean Dataset
# ====================================
df.to_csv("data/clean_crop.csv", index=False)

print("\nClean dataset saved successfully.")
print("File Name : clean_crop.csv")