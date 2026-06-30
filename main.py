from preprocessing import load_and_process

df = load_and_process()

print("\nSeasonal Crop Info:")
print(df.groupby('season')['label'].unique())