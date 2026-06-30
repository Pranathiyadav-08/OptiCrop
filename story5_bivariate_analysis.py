import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# Load Processed Dataset
# ===============================
df = pd.read_csv("data/processed_crop.csv")

print("Dataset Loaded Successfully!\n")
print(df.head())

# ==========================================
# Temperature vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='temperature', data=df)
plt.title("Temperature vs Crop")
plt.xlabel("Crop")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Rainfall vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='rainfall', data=df)
plt.title("Rainfall vs Crop")
plt.xlabel("Crop")
plt.ylabel("Rainfall")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Nitrogen vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='N', data=df)
plt.title("Nitrogen vs Crop")
plt.xlabel("Crop")
plt.ylabel("Nitrogen")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Phosphorus vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='P', data=df)
plt.title("Phosphorus vs Crop")
plt.xlabel("Crop")
plt.ylabel("Phosphorus")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Potassium vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='K', data=df)
plt.title("Potassium vs Crop")
plt.xlabel("Crop")
plt.ylabel("Potassium")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Humidity vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='humidity', data=df)
plt.title("Humidity vs Crop")
plt.xlabel("Crop")
plt.ylabel("Humidity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Soil pH vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x='label', y='ph', data=df)
plt.title("Soil pH vs Crop")
plt.xlabel("Crop")
plt.ylabel("Soil pH")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# Season vs Crop
# ==========================================
plt.figure(figsize=(8,5))
sns.countplot(x='season', hue='label', data=df)
plt.title("Season vs Crop")
plt.xlabel("Season")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ==========================================
# Correlation Heatmap
# ==========================================
plt.figure(figsize=(8,6))

correlation = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nBivariate Analysis Completed Successfully!")