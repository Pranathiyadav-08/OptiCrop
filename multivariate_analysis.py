import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/processed_crop.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# Scatter Plot
plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="temperature",
    y="rainfall",
    hue="label",
    s=120
)

plt.title("Temperature vs Rainfall")
plt.show()

print("Scatter Plot Completed")