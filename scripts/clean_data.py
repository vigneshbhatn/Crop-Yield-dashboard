import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\mysol\PycharmProjects\Crop-Yield-dashboard\data\raw\crop_yield.csv')  # Replace with your actual file name

# Remove rows with any null values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the cleaned dataset
df.to_csv('cleaned_crop_data.csv', index=False)

print("Nulls and duplicates removed. Cleaned data saved as 'cleaned_crop_data.csv'.")
