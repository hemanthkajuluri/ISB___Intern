import pandas as pd

# Load the dataset, skipping the specified rows
df = pd.read_excel("dataa.xlsx", skiprows=[0, 1, 2, 3, 5, 40, 41, 42, 43, 44, 46, 80, 81, 82, 83, 85, 119, 120, 121, 122, 124, 158, 159, 160, 161, 163, 197, 198], header=0)

def process_string(s):
    """Remove numerical prefix followed by a dot and strip the string."""
    if '.' in s:
        parts = s.split('.', 1)
        if parts[0].isdigit():
            return parts[1].strip()
    return s

# Apply preprocessing to the CHARACTERISTICS column
df['CHARACTERISTICS'] = df['CHARACTERISTICS'].str.replace(r'\s+', ' ', regex=True).str.replace(r'\*$', '', regex=True).apply(process_string)

# Break the dataframe into segments based on the structure of your document
segments = [df[i:i+34].reset_index(drop=True) for i in range(0, len(df), 34)]

# Assuming the first row of each segment (after the first) contains column names
for i, segment in enumerate(segments):
    if i > 0:  # Skip the first segment
        # Update column names with the first row and then drop it
        segment.columns = segments[i].iloc[0]
        segments[i] = segments[i].drop(0).reset_index(drop=True)

# Merge segments by columns, ensuring no column duplication occurs in the process
df_final = pd.concat(segments, axis=1)
df_final = df_final.loc[:, ~df_final.columns.duplicated()]

# Transform the DataFrame from wide format to long format
df_long = pd.melt(df_final, id_vars=['CHARACTERISTICS'], var_name='Year', value_name='Value').dropna()

# Rename columns to match the final output requirement
df_long = df_long.rename(columns={'CHARACTERISTICS': 'Characteristic'})

# Output the final DataFrame to a CSV file
df_long.to_csv("final_processed_data.csv", index=False)

print("Data processing complete. Output saved to 'final_processed_data.csv'.")
