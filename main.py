from preprocessing import load_and_process

df = load_and_process()

print("\nSeasonal Crop Info:")
print(df.groupby('season')['label'].unique())

import matplotlib.pyplot as plt
import seaborn as sns

# Season count plot
sns.countplot(x='season', data=df)
plt.title("Season Distribution")
plt.show()