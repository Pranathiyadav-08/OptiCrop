import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed_crop.csv")

print(df.head())

# Temperature
plt.figure()
sns.histplot(df['temperature'], kde=True)
plt.title("Temperature Distribution")
plt.show()

# Rainfall
plt.figure()
sns.histplot(df['rainfall'], kde=True)
plt.title("Rainfall Distribution")
plt.show()

# Season count
plt.figure()
sns.countplot(x='season', data=df)
plt.title("Season Distribution")
plt.show()
print("Graphs generated successfully.")