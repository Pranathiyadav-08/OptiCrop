import pandas as pd

def get_season(row):
    temp = row['temperature']
    rainfall = row['rainfall']

    if rainfall > 200 and temp > 25:
        return "Monsoon"
    elif rainfall < 100 and temp > 20:
        return "Summer"
    else:
        return "Winter"


def load_and_process():
    df = pd.read_csv("data/crop.csv")

    # Add season column
    df['season'] = df.apply(get_season, axis=1)

    print("\nFirst 5 rows:")
    print(df.head())

    # Save processed file
    df.to_csv("data/processed_crop.csv", index=False)

    return df


# MAIN ENTRY POINT (correct position)
if __name__ == "__main__":
    load_and_process()