import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_crop.csv")

# Season distribution graph
sns.countplot(x='season', data=df)
plt.title("Crop Distribution by Season")
plt.show()